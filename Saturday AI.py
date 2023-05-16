## For a Speaker ##
import win32com.client
## For taking command via voice ##
import speech_recognition as sr
## For surfing through websites
import webbrowser as wb
## For the time ## ## not added but can be added appropriately ##
import datetime
## For hardware system ## # For files and all #
import os
## For sending whatsapp messages ##
import pywhatkit as pwk

## Speaker david voice ##
speaker = win32com.client.Dispatch("SAPI.SpVoice")

## For the Microphone ##
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold = 0.6``
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User said : {query}")
            return query
        except Exception as e:
            return "Some error occured! Sorry for the Inconvinience"

speaker.speak("AI :  Hi how can I assist you today ?")
print("Listening")

## Returning cammand and using it in text ##
text = takeCommand()

## Can be added more websites ##
websites = {"Youtube": "https://www.youtube.com", "Wikipedia": "https://www.wikipedia.com",
            "Google": "https://www.google.com", "Github": "https://github.com/Sparsh-06"}

for i in websites:
    if f"open {i}".lower() in text.lower():
        wb.open(websites[i])

    ## Can use OS module for using local music App ##
    elif "play music".lower() in text.lower():
        wb.open("https://music.youtube.com")

    ## A website where you can play games ##
    elif "Play games".lower() in text.lower():
        wb.open("https://crazygames.com")

    ## YOU CAN ADD MORE ##

## If not in above search ## ## search for seperately in google ##
if f"search for {text[10,]}" in text.lower():
    wb.open(f"https://www.google.com/search?q={text[10,]}")

## FOR MESSAGING SOMEONE##
cont = {"Person1" : "+919312XXXXXX" , "Person2" : "+916758XXXXXX"} ## Can add more contacts ##
for j in cont:
    if f"message {j}".lower() in text.lower():
        v = ""
        for s in range(7+len(j)+1,len(text.lower())):
            v+=text[s]
        pwk.sendwhatmsg_instantly(cont[j], f"{v}")

## USe os module here ##



