# 升级
# 任何行业，都分为前端后端，我们这里讲的算法，都是后端跑的
# 为了做一个靠谱的前端，很多项目往往也需要一个简单易用靠谱的前端
# 利用Google的API，写一个类似钢铁侠Tony的语音小秘书Jarvis:
# 利用gTTs(Google Text-to-Speech API)把文本转化为音频
"""
from gtts import gTTS
from playsound import playsound

tts = gTTS(text='您好，我是您的私人助手，我叫小辣椒', lang='zh-cn')
tts.save("hello.mp3")
# mpg321需要安装
# os.system("mpg321 hello.mp3 &")
playsound("hello.mp3")
"""
# 有了文本到语音的功能，我们还可以使用Google API读出Jarvis的回复
# 这里需要安装几个库，SpeechRecognition，PyAudio，PySpeech


import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
from playsound import playsound
import random


# 讲出来AI的话
def speak(audio_string):
    print(audio_string)
    tts = gTTS(text=audio_string, lang='zh-cn')
    # creating a super random named file
    r1 = random.randint(1, 10000000)
    r2 = random.randint(1, 10000000)
    randfile = "./temp/" + str(r2) + "randomtext" + str(r1) + ".mp3"
    tts.save(randfile)
    playsound(randfile)


# 录下来你讲的话
def recordAudio():
    # 用麦克风记录下你的话
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

    # 用google API转化音频
    data = ""
    try:
        data = r.recognize_google(audio, language="cmn-Hans-CN")
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service: {0}".format(e))

    return data


# 自带的对话技能(rules)
def jarvis():
    while True:
        data = recordAudio()
        if "你好吗" in data:
            speak("还不错")
        if "几点" in data:
            speak(ctime())
        if "北京地图" in data:
            # data = data.split(" ")
            # location = data[2]
            speak("稍等, 我将会展示给你北京在哪里.")
            # os.system("open -a Safari https://www.google.com/maps/place/" + location + "/&anp;")
            os.system('"C:/Program Files/Internet Explorer/iexplore.exe" '
                      'http://www.google.com/maps/place/' + 'beijing' + '/')
        if "再见" in data:
            speak("拜拜")
            break


# 初始化
time.sleep(2)
# speak("我是您的助手，有什么吩咐？")
speak("我是您的助手，有什么吩咐？")

jarvis()












