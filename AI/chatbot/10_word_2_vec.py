from bs4 import BeautifulSoup
import nltk
import re
from gensim.models import word2vec
from gensim.models import KeyedVectors


with open('./data/alice.txt') as fo:
    txt_raw = fo.read()

txt_bs = BeautifulSoup(txt_raw, 'lxml').get_text()

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
sentences_raw = tokenizer.tokenize(txt_bs)

sntncs = []
stops = set(nltk.corpus.stopwords.words('english'))

for sntnc in sentences_raw:
    lttr_only = re.sub('[^a-zA-z]', " ", sntnc)
    wrds = lttr_only.lower().split()
    wrds_mnng = [w for w in wrds if not w in stops]
    sntncs += [wrds_mnng]


num_features = 1000
min_word_count = 10
num_workers = 4
size = 256
window = 5

model = word2vec.Word2Vec(sntncs, workers=num_workers,
                          size=num_features, min_count=min_word_count,
                          window=window)
print(model['feet'])

model.save('lol.save')


# 有没有发现哪些点可以给最简单的Rule-base机器人进行升级

# 可以用word2vec来把句子转成向量
# 无监督聚类方式来看句子是否可以聚到同一类别中，就是同一个intent
# 有监督的给句子打标签，然后使用机器学习训练模型，来新的句子给出intent


