import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
command = pyttsx3.init()

def talk_function(text):
    command.say(text)
    command.runAndWait()


def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        print("Sorry But I can't Listen you!")




def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('meenalphartiyal.project@gmail.com', 'Meenal1703#')
    email = EmailMessage()
    email['From'] = 'meenalphartiyal.project@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'father': 'gopalsingh.phartiyal@gmail.com',
    'myself': 'meenalphartiyal.project@gmail.com',
    'mother': 'meghaphartiyal@gmail.com',
    'mridul': 'mridulrastogi100@gmail.com',
    'ayush': 'ayush.aj.789@gmail.com'
}


def get_email_info():
    talk_function('Welcome to Voice Based Email Service')
    talk_function('Please say the name of the Receiver')
    name = get_info()
    receiver = email_list[name]
    print("From: meenalphartiyal.project@gmail.com")
    print("To: " + receiver)
    talk_function('Please say the subject of your email')
    subject = get_info()
    talk_function('Your message is ')
    message = get_info()
    send_email(receiver, subject, message)
    talk_function('You Mail is sent')
    talk_function('Do you want to send another mail?')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()



get_email_info()
