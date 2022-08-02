# Importing all Modules one by one
import shutil
import pyttsx3 as tts  # For text-to-speech
import speech_recognition as sr  # For Recognizing the user voice
import datetime as dt  # For printing the time
import wikipedia as wk  # For Searching on Wikipedia
import webbrowser as wb  # For running web queries within python
import os as os  # For accessing the system directories
import smtplib as smtp  # For accessing smtp server of gmail
import pyjokes as pyj # For Telling joke to user

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

    speak("Hi sir I\'m Alpha 1 point o, the friendly assistant. Speed 1 terahertz, memory 1 zigabyte. ")

# Username Function for Deciding name for the user


def username():
    speak("What should i call you, sir?")
    uname = takeCommand()
    print("###############################")
    speak(f"Welcome Mr. {uname}")
    print("###############################")
    print()
    speak("How can i help you, sir?")

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
    # Enable Low Secure App Access
    server.login("your-email-address", "your-password")
    server.sendmail("your-email-address", to, content)
    server.close()


# Main Method of the Program
if __name__ == "__main__":
    def clear(): return os.system("cls")  # Clear Any Command Before

    clear()
    greetMe()
    username()

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
            speak("Here you go to Youtube")
            wb.open_new_tab("http://www.youtube.com")

        elif "open google" in query:
            speak("Here you go to Google")
            wb.open_new_tab("http://www.google.com")

        elif "open netflix" in query:
            speak("Here you go to Netflix")
            wb.open_new_tab("http://www.netflix.com")

        elif "open github" in query:
            speak("Here you go to Github")
            wb.open_new_tab("http://www.github.com")

        elif "open gmail" in query:
            speak("Here you go to your Gmail Inbox")
            wb.open_new_tab("http://www.gmail.com")

        # Local Time Query
        elif "the time" in query:
            strTime = dt.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is - {strTime}")

        # VS Code Startup Query
        elif "open vs code" in query:
            speak("Here you go to Visual Studio Code. Happy Coding")
            os.system("code")

        # Music Play Query
        elif ("play songs" in query) or ("play song" in query) or ("play music" in query):
            speak("Here You go with music:")
            print()
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
            speak("Hii sir, I am Alpha 1 point o. I am a virtual assistant who can do some mini tasks like playing songs, sending email, searching google, youtube, wikipedia and many more. I have been created by Harshal using core python. You can find me on github at profile @harshal-k612")

        elif "tell me about yourself" in query:
            speak("Hii sir, I am Alpha 1 point o. I am a virtual assistant who can do some mini tasks like playing songs, sending email, searching google, youtube, wikipedia and many more. I have been created by Harshal using core python. You can find me on github at profile @harshal-k612")

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
        elif ("shutdown" in query) or ("shut down" in query):
            speak("Shutting Down sir,Have a Good Day !")
            exit()

        elif "quit" in query:
            speak("Quitting sir,Have a Good Day !")
            exit()

        # Sending Email Query only for harshal
        elif ("send email to harshal" in query) or ("send mail to harshal" in query):
            try:

                speak("What should i say, Sir?")
                content = takeCommand()
                to = "harshalkakaiya61@gmail.com"  # My Email Address
                sendEmail(to, content)
                speak("Email has been sent successfully sir")

            except Exception as e:
                speak("Sorry Sir.I am not able to send this email this moment")

        # General Email Sending Query
        elif ("send email" in query) or ("send mail" in query):
            try:

                speak("What should i say, Sir?")
                content = takeCommand()
                speak("Whome should i send the mail?")
                to = input()  # Destination Email Address
                sendEmail(to, content)
                speak("Email has been sent successfully sir")

            except Exception as e:
                speak("Sorry Sir.I am not able to send this email this moment")

        # Interaction Queries
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        # Name Query
        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me Alpha")

        # Creator Query 

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Harshal.")
        
        # Joke Query
        elif 'joke' in query:
            speak(pyj.get_joke())

        # Some Other Queries for Fun XD

        elif "who i am" in query:
            speak("If you talk then definitely your human X D.")

        elif "why you came to world" in query:
            speak("Thanks to Harshal. further It's a secret")

        elif "who are you" in query:
            speak("I am your virtual assistant created by Harshal")

        elif 'reason for you' in query:
            speak("I was created as a Minor project by Mister Harshal ")
        
        # When no query runs
        else:
            speak("Nothing Happens Sir...Please Try Again")
