from nltk.corpus import brown
import nltk

# 读取数据集
"""
print(brown.categories())
print(len(brown.sents()))
print(len(brown.words()))


# 分词
sentence = "hello, world"
tokens = nltk.word_tokenize(sentence)
print(tokens)


import jieba
seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
print("Full Mode:", "/".join(seg_list))
seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
print("Default Mode:", "/".join(seg_list))
seg_list = jieba.cut_for_search("我来到北京清华大学")
print(",".join(seg_list))


from nltk.tokenize import word_tokenize

tweet = 'RT @angelababy: love you baby! :D http://ah.love #168cm'
print(word_tokenize(tweet))


from nltk.stem.porter import PorterStemmer

porter_stemmer = PorterStemmer()
print(porter_stemmer.stem('maximum'))
print(porter_stemmer.stem('presumably'))
print(porter_stemmer.stem('multiply'))
print(porter_stemmer.stem('provision'))

p = PorterStemmer()
print(p.stem('went'))
print(p.stem('wenting'))

# Stem
from nltk.stem import SnowballStemmer

snowball_stemmer = SnowballStemmer('english')
print(snowball_stemmer.stem('maximum'))
print(snowball_stemmer.stem('presumably'))


from nltk.stem.lancaster import LancasterStemmer

lancaster_stemmer = LancasterStemmer()
print(lancaster_stemmer.stem('maximum'))
print(lancaster_stemmer.stem('presumably'))


# Lemma，语言学家，建立词汇表，taxonomy
from nltk.stem import WordNetLemmatizer

wordnet_lemmatizer = WordNetLemmatizer()
print(wordnet_lemmatizer.lemmatize('dogs'))
print(wordnet_lemmatizer.lemmatize('churches'))
print(wordnet_lemmatizer.lemmatize('aardwolves'))
print(wordnet_lemmatizer.lemmatize('abaci'))
print(wordnet_lemmatizer.lemmatize('hardrock'))
print(wordnet_lemmatizer.lemmatize('are'))
print(wordnet_lemmatizer.lemmatize('is'))
print(wordnet_lemmatizer.lemmatize('are', pos='v'))
print(wordnet_lemmatizer.lemmatize('is', pos='v'))

import nltk
text = nltk.word_tokenize('what does the fox say')
print(text)
print(nltk.pos_tag(text))

"""
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

tweet = '我 爱 中国'
word_list = word_tokenize(tweet)
# 先token一把，然后再做
filtered_words = [word for word in word_list if word not in stopwords.words('chinese')]
print(filtered_words)
# nltk不支持中文，corenlp






