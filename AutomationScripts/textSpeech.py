import pyttsx3
#make sure to install pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 165)
    engine.say(text)
    engine.runAndWait()
    

speak("Hey Boss, Im Jarvis")

#lets take an input

user_input = input("What do you want me to say?: ")

speak(f"You said: {user_input}")
speak("Task completed, Boss")



