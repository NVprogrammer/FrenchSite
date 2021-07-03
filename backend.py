import pandas as pd
import random as r
import speech_recognition as speech_recog
import pyttsx3
def word_get_pair():
    verbs=pd.DataFrame()
    verbs=pd.read_excel('files/france.xlsx',sheet_name='Глаголы')
    to_drop=[i for i in verbs.columns if i.__contains__('Unnamed')]
    verbs=verbs.drop(labels=to_drop,axis=1)
    g1=verbs.iloc[:,[0]]
    p1=verbs.iloc[:,[1]]
    g2=verbs.iloc[:,[2]]
    p2=verbs.iloc[:,[3]]
    g3=verbs.iloc[:,[4]]
    p3=verbs.iloc[:,[5]]
    g1 = g1.dropna()
    p1 = p1.dropna()
    g2 = g2.dropna()
    p2 = p2.dropna()
    g3 = g3.dropna()
    p3 = p3.dropna()
    def pair(g,p):
        num=r.randint(0,len(g)-1)
        return g.iloc[num,0],p.iloc[num,0]
    word=r.choice([pair(g1,p1),pair(g2,p2),pair(g3,p3)])
    print( word[0],word[1])
    return word[0],word[1]

def speech_rec():
    mic = speech_recog.Microphone(device_index=2)
    recog = speech_recog.Recognizer()
    for index, name in enumerate(speech_recog.Microphone.list_microphone_names()):
        print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
    try:
        with mic as audio_file:
            recog.adjust_for_ambient_noise(audio_file,duration=0.5)
            print("Speak Please")
            audio = recog.listen(audio_file)
            print('after')
            return recog.recognize_google(audio,language='fr-Fr')
    except speech_recog.RequestError:
            # API was unreachable or unresponsive
            print('Unrespons')
    except speech_recog.UnknownValueError:
        # speech was unintelligible
        print('Unable to recognize speech')
# print(speech_rec())
