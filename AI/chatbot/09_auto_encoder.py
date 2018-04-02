# 很好的避免人类惯性思维，来表达向量抽象特征

# gensim  https://radimrehurek.com/gensim/
# keras

from keras.layers import Input
from keras.layers import Dense
from keras.models import Model
from sklearn.cluster import KMeans

# i love you
# ASCII [104, 125, 199]
# 中文可以用unicode来编码，然后可以用索引来表达，电报码


class ASCIIAutoencoder():
    """基于字符的Auto encoder"""

    def __init__(self, sen_len=512, encoding_dim=32, epoch=50, val_ratio=0.3):
        """
        Init.

        :param sen_len: 把sentences pad成相同的长度
        :param encoding_dim: 压缩后的维度dim
        :param epoch: 要跑多少轮次
        :param kmeanmodel: clustering模型，在encoder之后做什么
        """
        self.sen_len = sen_len
        self.encoding_dim = encoding_dim
        self.autoencoder = None
        self.encoder = None
        self.kmeanmodel = KMeans(n_clusters=2)
        self.epoch = epoch

    # 构建模型
    def fit(self, x):
        # 把所有的trainset都做成同一个size，并把每一个字符都换成ascii码
        # 进去是原文件，方法进行完出来是[list]，每篇文章来补全维度512个
        x_train = self.preprocess(x, length=self.sen_len)
        # 然后给input预留好位置
        input_text = Input(shape=(self.sen_len,))
        # encoded 每经过一层，都被刷新成小一点的 压缩后表达式
        encoded = Dense(1024, activation='tanh')(input_text)
        encoded = Dense(512, activation='tanh')(encoded)
        encoded = Dense(128, activation='tanh')(encoded)
        encoded = Dense(self.encoding_dim, activation='tanh')(encoded)

        # decoded 就是把刚刚压缩完的东西，给反过来还原成input_text
        decoded = Dense(128, activation='tanh')(encoded)
        decoded = Dense(512, activation='tanh')(decoded)
        decoded = Dense(1024, activation='tanh')(decoded)
        decoded = Dense(self.sen_len, activation='tanh')(decoded)

        # 整个从大到小再到大的过程，叫做autoencoder
        self.autoencoder = Model(inputs=input_text, outputs=decoded)

        # 那么，只从大到小就叫做encoder
        self.encoder = Model(inputs=input_text, outputs=encoded)

        # compile
        self.autoencoder.compile(optimizer='adam', loss='mse')
        # 运行训练
        self.autoencoder.fit(x_train, x_train,
                             nb_epoch=self.epoch,
                             batch_size=1000,
                             shuffle=True)
        # 抽取特征
        x_train = self.encoder.predict(x_train)
        self.kmeanmodel.fit(x_train)

    def preprocess(self):
        return None

    def predict(self, x):
        # 第一步，把来的都给搞成ASCII化，并且长度相同
        x_test = self.preprocess(x, length=self.sen_len)
        # 然后用encoder把test集给压缩
        x_test = self.encoder.predict(x_test)
        # 利用训练好的kmeans来做预测类别
        preds = self.kmeanmodel.predict(x_test)
        return preds

# autoencoder在工业中用的并不多，降维可能会用到，更好的是word2vec

