from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


Chinese_bot = ChatBot("Training demo")
Chinese_bot.set_trainer(ListTrainer)
Chinese_bot.train([
    '你好',
    '你好',
    '有什么能帮你的',
    '想买数据科学的书',
    '具体是数据科学哪块呢？',
    '机器学习',
])

# 测试
question = '你好'
print(question)
response = Chinese_bot.get_response(question)
print(response)

print('\n')

question = '请问哪里能买到数据科学的书？'
print(question)
response = Chinese_bot.get_response(question)
print(response)














