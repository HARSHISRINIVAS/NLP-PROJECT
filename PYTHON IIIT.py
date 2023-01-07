import speech_recognition as kt
def main():
    h = kt.Recognizer()
    with kt.Microphone()as source:
        h.adjust_for_ambient_noise(source)
        print("please say something")
        audio = h.listen(source)
        print("Recognizing now.....")
        try:
            print("you have said\n"+h.recognize_google(audio))
            print("Audio recorder successfully\n")
        except Exception as e:
            print("Error:"+str(e))
        with open("recorded.wave","wb")as f:
            f.write(audio.get_wav_data())
if __name__== "__main__":
    main()
