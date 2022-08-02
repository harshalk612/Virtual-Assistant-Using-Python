# Importing all Modules one by one
import pyttsx3 as tts  # For text-to-speech
import speech_recognition as sr  # For Recognizing the user voice
import datetime as dt  # For printing the time
import wikipedia as wk  # For Searching on Wikipedia
import webbrowser as wb  # For running web queries within python
import os as os  # For accessing the system directories
import smtplib as smtp  # For accessing smtp server of gmail

# Initializing the voice engine
engine = tts.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

# Function Speak for Speaking


def speak(audio):
    engine.say(audio)
    print("Alpha:", audio)
    engine.runAndWait()

# WishMe Function for Greeting the User


def greetMe():
    hour = dt.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!")

    elif hour >= 12 and hour < 17:
        speak("Good Afternoon Sir!")

    else:
        speak("Good Evening Sir!")

    speak("Hi sir I\'m your friendly Assistant Version 1 point 0. Speed 1 terahertz, memory 1 zigabyte. ")

# TakeCommand Function for Taking command from the User


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User Said: {query}\n")

    except Exception as e:
        print("Please say that again...")
        return "None"
    return query

# Function to search on Google Anything


def googleSearch(topic):  # this will be open in default Browser
    d = "https://www.google.com/search?q="
    search_list = topic.split()
    search_list = search_list[1:len(search_list)-2]
    topic = "+".join(search_list)
    os.system("start " + d + str(topic))


def youtubeSearch(topic):  # this will be open in default Browser
    d = "https://www.youtube.com/results?search_query="
    search_list = topic.split()
    search_list = search_list[1:len(search_list)-2]
    topic = "+".join(search_list)
    os.system("start " + d + str(topic))


# Email Sending Function - sendEmail


def sendEmail(to, content):
    server = smtp.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("your-email-address", "your-password")
    server.sendmail("your-email address", to, content)
    server.close()


# Main Method of the Program
if __name__ == "__main__":
    greetMe()

    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if "wikipedia" in query:
            speak("Searching Wikipedia...Please wait")

            query = query.replace("wikipedia", "")
            results = wk.summary(query, sentences=2)
            speak("Alright!")
            speak("According to Wikipedia-")
            speak(results)

        # Internet Queries
        elif "open youtube" in query:
            speak("Opening Youtube")
            wb.open_new_tab("http://www.youtube.com")

        elif "open google" in query:
            speak("Opening Google...")
            wb.open_new_tab("http://www.google.com")

        elif "open netflix" in query:
            speak("Opening Netflix...")
            wb.open_new_tab("http://www.netflix.com")

        elif "open github" in query:
            speak("Opening Github...")
            wb.open_new_tab("http://www.github.com")

        elif "open gmail" in query:
            speak("Opening Gmail...")
            wb.open_new_tab("http://www.gmail.com")

        # Local Time Query
        elif "the time" in query:
            strTime = dt.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is - {strTime}")

        # VS Code Startup Query
        elif "open vs code" in query:
            speak("Sir, opening vs code...")
            os.system("code")

        # Music Play Query
        elif "play songs" in query:
            music_dir = "F:\\Favourite Songs"
            songs = os.listdir(music_dir)
            print("Available Songs are below : ")
            print()
            # For Displaying Songs in Order
            for i in range(len(songs)):
                print(f"{i+1}.", songs[i].replace(".mp3", ""))
            print()
            user_choice = int(
                input("Enter the number of song u want to play: "))
            print()
            song = songs[user_choice-1].replace(".mp3", "")
            print(f"(Now Playing)  {song}")
            os.startfile(os.path.join(music_dir, songs[user_choice-1]))

        # Introduction Query

        elif "who are you" in query:
            speak("Hii sir, I am Alpha. Speed 1 Terahertz, memory 1 Zegabyte. I am a desktop assistant who can do some mini tasks like playing songs, searching google, youtube and many more. I have been developed by Harshal aka Smashy. You can find me on github at profile @harshal-k612")

        elif "tell me about yourself" in query:
            speak("Hii sir, I am Alpha. Speed 1 Terahertz, memory 1 Zegabyte. I am a desktop assistant who can do some mini tasks like playing songs, searching google, youtube and many more. I have been developed by Harshal aka Smashy. You can find me on github at profile @harshal-k612")

        # Open Query ( Under Developing )
       
        elif ("note" in query) or ("notes" in query) or ("notepad" in query) or ("editor" in query):
            speak("Opening Notepad...")
            os.system("Notepad")

        # Search Queries

        elif "search" and "google" in query:
            googleSearch(query)

        elif "search" and "youtube" in query:
            youtubeSearch(query)

        # For Shutting Down Alpha
        elif "shutdown" in query:
            speak("Shutting Down sir,Have a Good Day !")
            exit()

        elif "quit" in query:
            speak("Quitting sir,Have a Good Day !")
            exit()

        # Sending Email Query
        elif "send email to harshal" in query:
            try:

                speak("What should i say, Sir?")
                content = takeCommand()
                to = "receiver-email-address"  # Destination Email Address
                sendEmail(to, content)
                speak("Email has been sent successfully sir")

            except Exception as e:
                speak("Sorry Sir.I am not able to send this email this moment")

        # When no query runs
        else:
            speak("Nothing Happens Sir...Please Try Again")
