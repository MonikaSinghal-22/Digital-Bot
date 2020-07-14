import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

#microsoft package for taking voice
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    speak("Hello Monika")
    hour = int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("good morning!")
    elif(hour>=12 and hour<18):
        speak("good afternoon!")
    else:
        speak("good evening!")

    speak("I am jarvis madam Please tell me how may I help you")

def takeCommand():
    #it takes microphone input from the user and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        #r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing........")
        query=r.recognize_google(audio)
        print(f"user said: {query}\n")
    except Exception as e:
        print(e)
        print("say that again please..")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('poojasinghal2206@gmail.com','pooja2206')
    server.sendmail('poojasinghal2206@gmail.com',to,content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True: 
        query=takeCommand().lower()
        #logic for executing task
        if 'wikipedia' in query:
            speak('searching wikipedia....')
            query=query.replace('wikipedia',' ')
            results=wikipedia.summary(query,sentences=2)
            speak('according to wikipedia')
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open('https://www.youtube.com/')
        elif 'open google' in query:
            webbrowser.open('https://www.google.com/')
        elif 'open stackoverflow' in query:
            webbrowser.open('https://stackoverflow.com/')
        
        elif 'play music' in query:
            music_dir='C:\\Users\\Monika\\Music\\Video Projects'
            songs=os.listdir(music_dir)
            print(songs)
            #write for random song number
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(strTime)
        elif 'open code' in query:
            codePath="C:\\Program Files\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'email to monika' in query:
            try:
                speak("What should I say")
                content=takeCommand()
                to="monikassinghal1996@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("sorry I am not able to send this email")
        

        '''
        1-store remainders in csv and use panda
        2-use send email as key (email id dictionary ) 
        '''