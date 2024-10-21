//Task5 and 6 Create a menu-driven program using Python for Notepad, Chrome, WhatsApp, 6. Email, SMS, ChatGPT, geolocation, or retrieving current trending topics on Twitter.
import os
import webbrowser
import smtplib
from email.mime.text import MIMEText
import openai
from geopy.geocoders import Nominatim
import tweepy

print("Hey, I am your assistant.")

def open_calendar():
    print("Opening calendar...")
    os.system("start outlookcal:")

def open_chrome():
    print("Opening Chrome...")
    os.system("start chrome")

def open_file_explorer():
    print("Opening File Explorer...")
    os.system("start explorer")
    
def open_notepad():
    print("Opening Notepad...")
    os.system("start notepad")

def open_command_prompt():
    print("Opening Command Prompt...")
    os.system("start cmd")

def open_control_panel():
    print("Opening Control Panel...")
    os.system("start control")
    
def open_task_manager():
    print("Opening Task Manager...")
    os.system("start taskmgr")

def open_system_settings():
    print("Opening System Settings...")
    os.system("start ms-settings:")

def open_whatsapp():
    print("Opening WhatsApp Web...")
    webbrowser.open("https://web.whatsapp.com/")

def send_email():
    sender_email = input("Enter your email: ")
    sender_password = input("Enter your email password: ")
    recipient_email = input("Enter recipient email: ")
    subject = input("Enter email subject: ")
    body = input("Enter email body: ")

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
            smtp_server.login(sender_email, sender_password)
            smtp_server.sendmail(sender_email, recipient_email, msg.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

def send_sms():
    print("SMS functionality requires additional setup with a service provider.")
    print("For demonstration, we'll just print the message.")
    recipient = input("Enter recipient phone number: ")
    message = input("Enter SMS message: ")
    print(f"SMS sent to {recipient}: {message}")

def chat_with_gpt():
    openai.api_key = input("Enter your OpenAI API key: ")
    user_input = input("Enter your message to ChatGPT: ")
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=user_input,
            max_tokens=150
        )
        print("ChatGPT response:", response.choices[0].text.strip())
    except Exception as e:
        print(f"Error communicating with ChatGPT: {e}")

def get_geolocation():
    geolocator = Nominatim(user_agent="myGeocoder")
    location = input("Enter a location to geocode: ")
    try:
        location = geolocator.geocode(location)
        print(f"Address: {location.address}")
        print(f"Latitude: {location.latitude}, Longitude: {location.longitude}")
    except Exception as e:
        print(f"Error getting geolocation: {e}")

def get_twitter_trends():
    print("To use this feature, you need to set up Twitter API credentials.")
    consumer_key = input("Enter your Twitter API consumer key: ")
    consumer_secret = input("Enter your Twitter API consumer secret: ")
    access_token = input("Enter your Twitter access token: ")
    access_token_secret = input("Enter your Twitter access token secret: ")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    try:
        trends = api.get_place_trends(1)  # 1 is the woeid for worldwide
        print("Current Twitter Trends:")
        for trend in trends[0]["trends"][:10]:
            print(trend["name"])
    except Exception as e:
        print(f"Error fetching Twitter trends: {e}")

def assistance():
    print("\nWhat would you like to do?")
    print("1. Open Calendar")
    print("2. Open Chrome")
    print("3. Open File Explorer")
    print("4. Open Notepad")
    print("5. Open Command Prompt")
    print("6. Open Control Panel")
    print("7. Open Task Manager")
    print("8. Open System Settings")
    print("9. Open WhatsApp")
    print("10. Send Email")
    print("11. Send SMS")
    print("12. Chat with GPT")
    print("13. Get Geolocation")
    print("14. Get Twitter Trends")
    print("15. Exit")
    return input("Enter your choice (1-15): ")

while True:
    choice = assistance()

    if choice == '1':
        open_calendar()
    elif choice == '2':
        open_chrome()
    elif choice == '3':
        open_file_explorer()
    elif choice == '4':
        open_notepad()
    elif choice == '5':
        open_command_prompt()
    elif choice == '6':
        open_control_panel()
    elif choice == '7':
        open_task_manager()
    elif choice == '8':
        open_system_settings()
    elif choice == '9':
        open_whatsapp()
    elif choice == '10':
        send_email()
    elif choice == '11':
        send_sms()
    elif choice == '12':
        chat_with_gpt()
    elif choice == '13':
        get_geolocation()
    elif choice == '14':
        get_twitter_trends()
    elif choice == '15':
        print("Thank you, bye.")
        break
    else:
        print("Invalid choice. Please try again.")
