# 升级
# 之前的rule太弱智了，我们需要更好一点的“精准对答”
# 比如：
# 透过关键词来判断这句话的意图是什么（intents）

from nltk import word_tokenize
import random

# 打招呼
greetings = ["hola", "hello", "hi", "Hi", "hey!", "hey"]
# 回复打招呼
random_greeting = random.choice(greetings)

# 对于“假期”的话题关键词
question = ["break", "holiday", "vacation", "weekend"]
# 回复假期话题
responses = ["It was nice! I went to Paris", "Sadly, I just stayed at home"]
# 随机选择一个回复
random_response = random.choice(responses)

# 机器人聊起来
while True:
    userInput = input(">>> ")
    cleaned_input = word_tokenize(userInput)
    # 这里，我们比较一下关键词，确定他属于哪个问题
    if not set(cleaned_input).isdisjoint(greetings):
        print(random_greeting)
    elif not set(cleaned_input).isdisjoint(question):
        print(random_response)
    # 除非你说拜拜
    elif userInput == 'bye':
        break
    else:
        print("I did not understand what you said")

# 比如其他的日后再说，word2vec之类的embedding方法升级，
# 通过词之间关系，比较远近距离来判断它们是否属于同一个语义








