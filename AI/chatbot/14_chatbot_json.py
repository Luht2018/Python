from chatterbot import ChatBot

"""
如果一个已经训练好的chatbot，你想取出它的语料，用于别的chatbot构建，可以这么做
"""

chatbot = ChatBot(
    'Export Example Bot',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

# 训练一下
chatbot.train('chatterbot.corpus.chinese')

# 把语料到处到json文件中
chatbot.trainer.export_for_training('./my_export_chinese.json')











