import speech_recognition as sr
import pyttsx3 

# Initialize recognizer
r = sr.Recognizer()

# Function to convert text to speech
def SpeakText(command):
    
    #Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
    
# Use mic as source for input
with sr.Microphone() as source2:
    # while True:
        # wait for a second to let recognizer adjust the energy threshold based on surrounding noise level
    r.adjust_for_ambient_noise(source2, duration=0.2)
        
        #listens for user input
    audio2 = r.listen(source2)
        
        # using google to recognize audio
        
    MyText = r.recognize_google(audio2)
    MyText = MyText.lower()
        
    print('Did you say ' + MyText)
    SpeakText(MyText)
        # if 'quit' in MyText:
        #     break