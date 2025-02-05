import requests
import json
import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def latestnews():
    api_dict = {"business" :"3e4f19732f514ddebd4a7b7e2ff2ba66" ,#Enter Your OWN API ,
            "entertainment" : "3e4f19732f514ddebd4a7b7e2ff2ba66",#Enter Your OWN API ,
            "health" : "3e4f19732f514ddebd4a7b7e2ff2ba66",#Enter Your OWN API,
            "science" :"3e4f19732f514ddebd4a7b7e2ff2ba66",#Enter Your OWN API,
            "sports" :"3e4f19732f514ddebd4a7b7e2ff2ba66",#Enter Your OWN API,
            "technology" :"3e4f19732f514ddebd4a7b7e2ff2ba66"#Enter Your OWN API
}

    content = None
    url = None
    speak("Which field news do you want, [business] , [health] , [technology], [sports] , [entertainment] , [science]")
    field = input("Type field news that you want: ")
    for key ,value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("url was found")
            break
        else:
            url = True
    if url is True:
        print("url not found")

    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news.")

    arts = news["articles"]
    for articles in arts :
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"for more info visit: {news_url}")

        a = input("[press 1 to cont] and [press 2 to stop]")
        if str(a) == "1":
            pass
        elif str(a) == "2":
            break
        
    speak("thats all")

