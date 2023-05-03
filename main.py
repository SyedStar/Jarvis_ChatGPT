import os
import openai
import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()
openai.api_key = ("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")
engine = pyttsx3.init()

def SpeakText(command):
  engine = pyttsx3.init()
  engine.say(command)
  engine.runAndWait()

while True:
  try:

    # use the microphone as source for input.
    with sr.Microphone() as source2:
      SpeakText("Hi waiting for your input")
      # wait for a second to let the recognizer
      # adjust the energy threshold based on
      # the surrounding noise level
      r.adjust_for_ambient_noise(source2, duration=0.2)

      # listens for the user's input
      audio2 = r.listen(source2)

      # Using google to recognize audio
      MyText = r.recognize_google(audio2)
      MyText = MyText.lower()
      #MyText = "how are you"

      print("Question", MyText)
      print("Did you Asked"+MyText)

  except sr.RequestError as e:
    print("Could not request results; {0}".format(e))

  except sr.UnknownValueError:
    print("unknown error occurred")

  ask = MyText
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=ask,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
  )
  text = response['choices'][0]['text']
  engine.say(text)
  print('Reply: '+text)
  engine.runAndWait()