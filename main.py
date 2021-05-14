import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

audio = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = audio.listen(source)
            info = audio.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('adongoaustin14@gmail.com', 'austin123fortoday')
    email = EmailMessage()
    email['From'] = 'adongoaustin14@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)



email_list = {
    'jacob': 'jomondi813@gmail.com',
    'father': 'gmakajuma@gmail.com',
    'mother': 'mercywesonga.ouma@gmail.com',
    'annmarie': 'annmarie.adongo@gmail.com',
    'myself': 'austin.adongo@outlook.com',
}


def get_email_info():
    talk("Hello Austin! I am Swift your Email Assistant")
    talk('To Whom do you want to send an email??')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of your email?')
    subject = get_info()
    talk('Tell me the text in your email')
    message = get_info()
    send_email(receiver, subject, message)
    talk('Hey Austin. Your email is sent')
    talk('Do you want to send more email?')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()

    if 'no' in send_more:
        talk("Okay! Good bye!")
        exit()


get_email_info()