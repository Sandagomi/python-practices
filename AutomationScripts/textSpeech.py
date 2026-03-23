import pyttsx3

def speak(text):
    engine = pyttsx3.init()   # re-init every time
    engine.setProperty('rate', 165)
    engine.say(text)
    engine.runAndWait()

# Jarvis-style interaction
speak("Hello boss. I am your Python assistant.")

user_input = input("Type your command: ")

speak(f"You said: {user_input}")
speak("Task completed successfully.")

#changes