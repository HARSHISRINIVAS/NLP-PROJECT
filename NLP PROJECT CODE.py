import speech_recognition as sr
def main():

    r = sr.Recognizer()

    with sr.Microphone()as source:
        r.adjust_for_ambient_noise(source)

        print("please say something")

        audio = r.listen(source)

        print("Recognizing now.....")

        #recognize speech using google

        try:
            print("you have said\n"+r.recognize_google(audio))
            print("Audio recorder successfully\n")


        except Exception as e:
            print("Error:"+str(e))
        # write audio

        with open("recorded.wave","wb")as f:
            f.write(audio.get_wav_data())



if __name__== "__main__":
    main()
