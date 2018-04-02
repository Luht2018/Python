from chatterbot import ChatBot


# 构建ChatBot并指定Adapter
bot = ChatBot(
    'Default Response Example Bot',
    # storage_adapter='chatterbot.storage.JsonFileStorageAdapter',
    logic_adapters=[
        {
            # 编辑距离
            'import_path': 'chatterbot.logic.BestMatch'
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.65,
            'default_response': 'I am sorry, but I do not understand.'
        }
    ],
    # 训练时候给的语料库是一个列表，一个一问一答的列表
    trainer='chatterbot.trainers.ListTrainer'
)

# 手动给定一点语料用于训练
bot.train([
    'How can I help you?',
    'I want to create a chat bot',
    'Have you read the documentation',
    'No, I have not',
    'This should help get you started: http://chatterbot.rtfd.org/en/latest/quickstart.html'
])

# 给定问题并取回结果
question = 'How do I make an omelette?'
print(question)
response = bot.get_response(question)
print(response)

print("\n")
question = 'how to make a chat bot?'
print(question)
response = bot.get_response(question)
print(response)












