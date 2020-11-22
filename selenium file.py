import speech_recognition as sr
import win32com.client as w
import webbrowser
from selenium import webdriver
from selenium.webdriver import ActionChains
speak=w.Dispatch("SAPI.SpVoice")
r=sr.Recognizer()
driver=webdriver.Chrome()
z=0
driver.maximize_window()
driver.get('http://127.0.0.1:5000/')
while(1):
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2,duration=0.2)
            speak.Speak("listening to the source audio")
            audio2=r.listen(source2)
            data=r.recognize_google(audio2)
            print(data)
            if('open' in data):
                webbrowser.open('http://127.0.0.1:5000/')
            elif('username' in data):
                try:
                    with sr.Microphone() as source2:
                        r.adjust_for_ambient_noise(source2,duration=0.2)
                        speak.Speak("Speak the username")
                        audio2=r.listen(source2)
                        string=r.recognize_google(audio2)
                        driver.find_element_by_name("username").send_keys(string)
                        z=1
                except sr.RequestError as e:
                    speak.Speak("Unknown Value!")
                except sr.UnknownValueError:
                    speak.Speak("Unknown error occured!")
            elif(('password' in data) and (z==1)):
                try:
                    with sr.Microphone() as source2:
                        r.adjust_for_ambient_noise(source2,duration=0.2)
                        speak.Speak("Speak password")
                        audio2=r.listen(source2)
                        another=r.recognize_google(audio2)
                        driver.find_element_by_name("password").send_keys(another)
                except sr.RequestError as e:
                    speak.Speak("Unknown Value!")
                except sr.UnknownValueError:
                    speak.Speak("Unknown error occured!")
            elif(('submit' in data) and  ('button' in data)):
                ActionChains('Chrome').click("button").perform()
                z+=1
            elif((z==2) and ('like' in data)):
                speak.Speak("you liked the post")
                        
                ActionChains('Chrome').click("another_button").perform()
                z+=1
            elif((z==3) and ('comment' in data)):
                try:
                    with sr.Microphone() as source2:
                        r.adjust_for_ambient_noise(source2,duration=0.2)
                        speak.Speak("Speak to comment on this particular post")
                        audio2=r.listen(source2)
                        another_value=r.recognize_google(audio2)
                        driver.find_element_by_name("comment").send_keys(another_value)
                except sr.RequestError as e:
                    speak.Speak("Unknown Value!")
                except sr.UnknownValueError:
                    speak.Speak("Unknown error occured!")
    except sr.RequestError as e:
        speak.Speak("Unknown Value!")
    except sr.UnknownValueError:
        speak.Speak("Unknown error occured!")