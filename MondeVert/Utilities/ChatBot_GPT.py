# Import the OpenAI library
import os
import platform
import subprocess

import requests
import random
import string
import openai
import pyttsx3
# Import the speech recognition library
import speech_recognition as sr
from dotenv import load_dotenv
from MondeVert.SHAINE_MonderVert.DoNotCommit import API_Key
# from git import Repo
#
# Repo.clone_from('https://gitlab.com/sfoerster/openai', master)
#






# Set up the model (more models, visit https://beta.openai.com/playground)


# Load your API key from an environment variable or secret management service
#openai.api_key = openai.api_key


def makeArt():
    print()
    prompt = input("Text prompt for image generation (e.g. 'A blue eagle flying over a desert at sunset'): ")
    print()

    # Set up the OpenAI API client :
    openai.api_key = API_Key
    print("Sending to OpenAI...")
    print()

    response = openai.Image.create(
      prompt=prompt,
      n=1,
      size="1024x1024"
    )

    image_url = response['data'][0]['url']

    print(f"Image URL: {image_url}")
    print()

    # URL of the image to be downloaded is defined as image_url
    r = requests.get(image_url) # create HTTP response object

    # send a HTTP request to the server and save
    # the HTTP response in a response object called r
    fname = f"{''.join([c for c in prompt.strip().replace(' ','_') if c.isalnum() or c == '_'])}.png"

    if not os.path.exists("images"):
        os.mkdir("images")

    if os.path.isfile(os.path.join("images", fname)):
        fname = fname.split(".")[0] + f".{''.join(random.choice(string.ascii_letters) for x in range(5))}.png"

    fname = os.path.join("images", fname)
    print(f"Filename: {fname}")
    with open(fname, 'wb') as f:

        # Saving received content as a png file in
        # binary format

        # write the contents of the response (r.content)
        # to a new file in binary mode.
        f.write(r.content)

    if platform.system() == 'Darwin':       # macOS
        subprocess.call(('open', fname))
    elif platform.system() == 'Windows':    # Windows
        os.startfile(fname)
    else:                                   # linux variants
        subprocess.call(('xdg-open', fname))
















# Define a function that sends a message to ChatGPT
def chat_query(prompt):
    model_engine = "text-davinci-003"
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=2048,
        n=1,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message


# Define a function that handles the conversation
def conversation_handler(prompt):
    # Send the prompt to ChatGPT


    load_dotenv()
    # Set up the OpenAI API client :
    openai.api_key = API_Key
    response = chat_query(prompt)
    print(f"ChatGPT: {response}")

    # End the conversation if ChatGPT says goodbye
    if "goodbye" in response.lower():
        return

    # Otherwise, get user input and continue the conversation
    prompt = input("You: ")
    conversation_handler(prompt)








def ChatGPTDA():
    # Import the OpenAI library

    # Set up the OpenAI API client :
    openai.api_key = API_Key


    # Set up the recognizer
    r = sr.Recognizer()

    # Import the text to speech synthesis library

    engine = pyttsx3.init()
    engine.setProperty('rate', 180)            # setting up new voice rate
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)  # changing index, changes voices. 1 for female

    # Record the audio
    engine.say(" Do you have any questions to ask Chat GPT?")
    engine.runAndWait()
    print('---------------------Please speak now, recording start-----------------------')
    with sr.Microphone() as source:
        audio = r.listen(source)
    print('---------------------Recording finished---------------------------------------')

    # Convert the audio to text
    prompt = r.recognize_google(audio)
    print(prompt)

    # check if the reply contains 'yes'
    while 'YES' in prompt.upper() or 'QUESTION' in prompt.upper():

        # Record the audio
        engine.say(" Please ask your question and get help from Chat GPT?")
        engine.runAndWait()
        print('---------------------Please speak now, recording start-----------------------')
        with sr.Microphone() as source:
            audio = r.listen(source)
        print('---------------------Recording finished---------------------------------------')

        # Convert the audio to text
        prompt = r.recognize_google(audio)

        # Generate text
        completions = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=2048,
            n=1,
            stop=None,
            temperature=0.5,
        )

        # Print the generated text
        message = completions.choices[0].text
        print(message)

        # generate the feedback
        engine.say(message)
        engine.runAndWait()
        # engine.stop()

        # Record the audio
        engine.say(" Any other questions to ask Chat GPT?")
        engine.runAndWait()
        print('---------------------Please speak now, recording start-----------------------')
        with sr.Microphone() as source:
            audio = r.listen(source)
        print('---------------------Recording finished---------------------------------------')

        # Convert the audio to text
        prompt = r.recognize_google(audio)
        print(prompt)




# Main program starts here:
if __name__ == "__main__":
    #ChatGPTDA()

    #makeArt()
    # Example of prompt to query
    prompt = input("What Do you want to Know?: ")
    #
    # # Start the conversation
    conversation_handler(prompt)

    #makeArt()