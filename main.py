#Alexa Bot

import speech_recognition as sr
import pyttsx3
import pywhatkit
import random
import datetime
import wikipedia


fortunes=["A beautiful, smart, and loving person will be coming into your life",
          "Don't be pushed around by the fears in your mind",
          "Be yourself; everyone else is already taken",
          "Be yourself, but always your better self",
          "Follow your own star","Just be yourself, there is no one better.",
          "you are an amazing person","you are an masterpiece","you are so handsome",
          "you are so beautiful","As you know, life is an echo; we get what we give"]

loves_in=["im so glad to here that, you are my friend  ","how sweet , I treasure our friendship ",
          "Im so happy ","Love you always my friend ","Lots of love "]

listener=sr.Recognizer()

engine=pyttsx3.init()
#below two lines for getting female voice
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        #getting users voice as a source
      with sr.Microphone() as source:
          print("Listening....")
          #listening to the source
          voice=listener.listen(source)
          #recognizing the voice
          command=listener.recognize_google(voice).lower()
          #it will work only when users says mikey
          if 'alexa' in command:
              #replacig mikey str to not repeat again
              command=command.replace('alexa','')
    except:
        pass
    return command

def run_alexa():
    #taking take_command function  as command
    command=take_command()
    #checking that play str is there in command
    if 'play' in command:
        #replacing play str to not repeat again
        song=command.replace('play ','')
        talk(f'playing {song}')
        #pywhatkit will go to youtube and playing song that you want
        pywhatkit.playonyt(song)
        print(f"Successfully played  🎧")

    elif 'tell about' in command:
        you=command.replace('tell about','')
        #telling random one in the random_fortunes list every single time you run
        random_fortunes=random.choice(fortunes)
        talk(f" {you} {random_fortunes} " )
        print(f"{you} {random_fortunes}❤️ ")

    elif 'i love you' in command:
        #telling random one in the choice_in list every single time you run
        choice_in=random.choice(loves_in)
        talk(f"{choice_in} ")
        print(f"{choice_in}❤️")

    elif 'time' in command:
        #%I for 12 hours format and %m for minutes and %p for AM or PM
        time_now=datetime.datetime.now().strftime('%I:%m %p')
        #%a is for day.Ex mon,tue......
        day=datetime.datetime.now().strftime('%a')
        talk(f"Current time is {time_now} and today day is {day}")
        print(f"Current time is {time_now} 🕘 and today day is {day}")

    elif 'who is ' in command:
        person=command.replace('who is','')
        #wikipedia gets the information from websites you want
        detail=wikipedia.summary(person,1)
        talk(detail)
        print(detail)
        print("\n Successfully searched 🦥 ")

    elif 'go for a date' in command:
        talk("Sorry,i can't do that,but im always there for you  ")
        print("Sorry,i can't do that,but im always there for you ☃️ ")

    elif 'are you single' in command:
        talk("no! i'm in love with Pandas ")
        print("no! i'm in love with Pandas 🐼")

    elif 'google' in command:
        google_search=command.replace('google','')
        talk(f"Searching {google_search}")
        #pywhatkit will take you to the google website and search for what you want
        pywhatkit.search(google_search)
        print("Successfully searched  🦥")


run_alexa()