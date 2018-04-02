from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.datasets import fetch_20newsgroups

# 比前面案例更好的方式是，TF-IDF，前面频率统计用的不多

newsgroups_train = fetch_20newsgroups(data_home="./data", subset='train')
newsgroups_test = fetch_20newsgroups(data_home="./data", subset='test')

# Convert data to tf-idf

vectorizer = TfidfVectorizer(min_df=0.01, max_df=0.95)
train_data = vectorizer.fit_transform(newsgroups_train.data)
test_data = vectorizer.transform(newsgroups_test.data)
train_data = train_data.todense()
print(train_data)
test_data = test_data.todense()
print(test_data)
train_labels = newsgroups_train.target
test_labels = newsgroups_test.target

# 接下来，机器学习，可能的ML模型
# SVM、LR、RF、MLP、LSTM、RNN
# 就可以来做文本分类了









