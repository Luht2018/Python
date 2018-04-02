# NLTK完成简单的情感分析
'''
sentiment_dictionary = {}
for line in open('data/AFINN-111.txt'):
    word, score = line.split("\t")
    sentiment_dictionary[word] = int(score)

# 把这个打分表记录在一个Dict上以后
# 跑一遍整个句子，把对应的值相加
total_score = sum(sentiment_dictionary.get(word, 0) for word in words)
# 有值就是Dict中的值，没有就是0
'''
# 于是你就得到了一个 sentiment score，任何rule-based都很稳定，但是比较low的，
# 如果我们可以配上一些ML机器学习方面，使得情感分析更好

from nltk.classify import NaiveBayesClassifier

# 随手制造点训练集
s1 = 'this is a good book'
s2 = 'this is a awesome book'
s3 = 'this is a bad book'
s4 = 'this is a terrible book'


def preprocess(s):
    # 句子处理，简单用了split()，把句子中每个单词分开
    # {'this': True, 'is': True, 'book': True, 'a': True, 'good': True}
    # 其中，前一个叫fname，对应每个出现的文本单词
    # 后一个叫fval，指的是每个文本单词对应的值
    # 这里我们用最简单的True来表示这个词出现在当前句子中
    # 以后我们可以升级这个逻辑，让它带有更牛逼的fval，比如word2vec
    return {word: True for word in s.lower().split()}


# 把训练集给做成标准形式
training_data = [
    [preprocess(s1), 'pos'],
    [preprocess(s2), 'pos'],
    [preprocess(s3), 'neg'],
    [preprocess(s4), 'neg']
]

# 喂给model吃
model = NaiveBayesClassifier.train(training_data)

# 打印出结果
print(model.classify(preprocess('this is a good car')))

# 找情感分析语料库可以不人工去打标签
# 句子，标签/打分



