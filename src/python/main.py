'''
    this is a virtual assistant program that gets the date, current time, gets the current time, responds back
    with a random greeting, and return information on a person.
'''

# pip install pyaudio
# pip install SpeechRecognition
# pip install gTTS
# pip install wikipedia

# import the libraries
import speech_recognition as sr

import os
from gtts import gTTS
import datetime
import warnings

import calendar
import random
import wikipedia

# ignore any warning messages
warnings.filterwarnings('ignore')


# record audio and return it as a string
def recordAudio():
    # record the audio
    r = sr.Recognizer()  # creating a recognizer object

    # open the microphone and start recording
    with sr.Microphone() as source:
        print("Say something...")
        audio = r.listen(source)

    # use Google's speech recognition
    data = ''
    try:
        data = r.recognize_google(audio)
        print('You said ' + data)
    except sr.UnknownValueError:  # check for unknowns errors
        print('Google speech recognition could not understand the audio, unknown error')
    except sr.RequestError as e:
        print('Request results from Google Speech Recognition service error ' + e)

    return data


# get the virtual assistant response
def assistantResponse(text):
    print(text)

    # convert the text to speech
    myobj = gTTS(text=text, lang='en', slow=False)

    # save the converted audio to a file
    myobj.save('assistant_response.mp3')

    # play the converted file
    os.system('start assistant_response.mp3')


# a function for wake word(s) or phrase
def wakeWord(text):
    WAKE_WORDS = ['hey computer', 'okay computer']  # that's the list of wake words

    text = text.lower()  # converting the text to all lower case words

    # check to see if the user's command/text contains a wake word
    for phrase in WAKE_WORDS:
        if phrase in text:
            return True

    # if the wake word isn't found in the text from the loop
    return False


# get the current date
def getDate():
    now = datetime.datetime.now()
    today = datetime.datetime.today()
    weekday = calendar.day_name[today.weekday()]
    monthNumber = now.month
    dayNum = now.day

    # list of months
    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
                   'October', 'November', 'December']
    ordinal_numbers = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th',
                       '11th', '12h', '13h', '14th', '15th', '16th', '17th', '18th', '19th', '20th',
                       '21st', '22nd', '23rd', '24th', '25th', '26th', '27th', '28th', '29th', '30th' '31st']

    return 'Today is ' + weekday + ' ' + month_names[monthNumber - 1] + ' the ' + ordinal_numbers[dayNum - 1] + '.'


# get a random greeting response
def greeting(text):
    # Greeting inputs
    GREETING_INPUTS = ['hi', 'hey', 'hello', 'greetings', 'wassup']

    # Greeting responses
    GREETING_RESPONSES = ['howdy', 'whats good', 'hello', 'hey there']

    # if the users input is a greeting, then return a randomly chosen greeting response
    for word in text.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES) + '.'

    # if no greeting was detected, then return an empty string
    return ''


# get a person first and last name
def getPerson(text):
    wordList = text.split()

    for i in range(0, len(wordList)):
        if i + 3 <= len(wordList) -1 and wordList[i].lower() == 'who' and wordList[i+1].lower() == 'is':
            return wordList[i+2] + ' ' + wordList[3]


while True:
    # record the audio
    text = recordAudio()
    response = ''

    # check for the wake word(s) / phrase(s)
    if (wakeWord(text) == True):
        # check for greetings by the user
        response = response + greeting(text)

        # check for date question by the user
        if ('date' in text):
            get_date = getDate()
            response = response + ' ' + get_date

        if('time' in text):
            now = datetime.datetime.now()
            meridiem = ''
            if(now.hour > 12):
                meridiem = 'p.m.'
                hour = now.hour - 12
            else:
                meridiem = 'a.m.'
                hour = now.hour

            # convert minute in a proper string
            if now.minute < 10:
                minute = '0' + str(now.minute)
            else:
                minute = str()

            response = response + {'local'}
        # check to see if the user said 'who is'
        if('who is' in text):
            person = getPerson(text)
            wiki = wikipedia.summary(person, sentences=2);
            response = response + ' ' +  'It is ' + str(hour) + ';' + minute + ' ' + meridiem + '. '

            # have the assistant respond back using  audio and text from response
            assistantResponse(response)


print(getDate())



text = 'this is a test'
# assistantResponse(text)
