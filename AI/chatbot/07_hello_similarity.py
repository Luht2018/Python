import nltk
from nltk import FreqDist

# 特征工程
# 做个词库先
corpus = 'this is my sentence '\
            'this is my life '\
            'this is the day'

# 随便tokenize一下
# 显然，正如上文提到，这里可以根据需要做任何的preprocessing：
# stopwords, lemma, stemming, etc.
tokens = nltk.word_tokenize(corpus)
print(tokens)

# 得到token好的word list
# ['this', 'is', 'my', 'sentence', 'this', 'is', 'my', 'life', 'this', 'is', 'the', 'day']

# 借用NLTK的FreqDist统计一下文字出现的频率
fdist = FreqDist(tokens)
print(fdist)

# 它就类似于一个字典，带上某个单词，可以看到它在整个文章中出现的次数
print(fdist['is'])

# 我们可以把最常用的50个单词拿出来，为什么需要拿出来？
# 因为一些非常冷门的单词对判断没有影响，比如人名，多了会无形中多了一个维度
standard_freq_vector = fdist.most_common(50)
size = len(standard_freq_vector)
print(size)
print(standard_freq_vector)


# 记录下每个单词的位置，构建词的索引
def position_lookup(v):
    res = {}
    counter = 0
    for word in v:
        res[word[0]] = counter
        counter += 1
    return res


# 把标准的单词位置记录下来，得到一个对照表
standard_position_dict = position_lookup(standard_freq_vector)
print(standard_position_dict)

# 这时，如果我们有个新句子
sentence = 'this is cool'
# 先建立一个跟我们的标准vector同样大小的向量
freq_vector = [0] * size
# 简单的preprocessing
tokens = nltk.word_tokenize(sentence)
# 对于这个新句子里的每一个单词
for word in tokens:
    try:
        # 如果在我们的词库里出现过，那么就标注1
        freq_vector[standard_position_dict[word]] += 1
    except KeyError:
        # 如果是个新词，就pass掉
        continue

print(freq_vector)
# 第一个位置代表is，第二个位置代表this，出现了一次
# 初始语料不够，会出问题
# 接着来用余弦相似度就可以来求相似度了



