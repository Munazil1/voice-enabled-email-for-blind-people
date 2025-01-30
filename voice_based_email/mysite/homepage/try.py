import speech_recognition as sr
import playsound

def speechtotext(duration):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        playsound.playsound('speak.mp3')
        print("Listening...")
        audio = r.listen(source, phrase_time_limit=duration)
    try:
        response = r.recognize_google(audio)
        print("You said: " + response)  # Display the captured text
    except sr.UnknownValueError:
        response = 'N'
        print("Could not understand audio")
    except sr.RequestError as e:
        response = 'N'
        print(f"Could not request results; {e}")
    return response

r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration=1)
    playsound.playsound('speak.mp3')
    audio = r.listen(source, phrase_time_limit=20)
    playsound.playsound(audio)