import speech_recognition as SPR

sr = SPR.Recognizer()
print("Please ask...!!!!")
with SPR.Microphone() as m :
    audio = sr.listen(m)
    query = sr.recognize_google(audio , language='eng-in')
    print(query)