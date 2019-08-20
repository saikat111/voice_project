import speech_recognition as sr
import webbrowser as wb

chrome_path = 'C:/Users/HP/AppData/Local/Google/Chrome/Application/chrome.exe %s'

r = sr.Recognizer()
with sr.Microphone() as source:
    print("say")
    audio = r.listen(source)
    print ("done")

try :
    text = r.recognize_google(audio)
    print("you  say:" + text)
    f_text ='https://web.facebook.com/search/str/'+ text +'/keywords_search'
    wb.get(chrome_path).open(f_text)

except Exception as e:
    print(e)
