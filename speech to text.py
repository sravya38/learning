import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
      print("say something..")
      audio=(r.listen(source))
print(r.recognize_google(audio,language="te-IN"))