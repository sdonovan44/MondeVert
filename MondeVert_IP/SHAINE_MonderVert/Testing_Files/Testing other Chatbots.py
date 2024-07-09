import pyttsx3
import speech_recognition as sr
import requests


def ask_question():
    # Initialize text-to-speech engine
    engine = pyttsx3.init()

    # Initialize speech recognition
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    # Ask a question
    engine.say("What would you like to ask Jasper?")
    engine.runAndWait()

    # Record user's question
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # Convert speech to text
    try:
        question = recognizer.recognize_google(audio)
        print("You asked:", question)

        # Send the question to Jasper
        jasper_url = "http://<jasper_server_ip>/api/ask"
        params = {"question": question}
        response = requests.get(jasper_url, params=params)

        # Retrieve the answer from Jasper's response
        answer = response.json().get("answer")
        print("Jasper answered:", answer)

        # Speak the answer
        engine.say(answer)
        engine.runAndWait()

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand your question.")
    except sr.RequestError as e:
        print("Sorry, an error occurred while processing your request:", str(e))



import requests

# Set the API endpoint URL
url = "https://api.taskade.com/v1/your-endpoint"

# Set the headers with your Personal Access Token
headers = {
    "Authorization": "Bearer YOUR_PERSONAL_ACCESS_TOKEN"
}

# Make a GET request to retrieve data
response = requests.get(url, headers=headers)

# Process the response
if response.status_code == 200:
    data = response.json()
    # Process the data as needed
else:
    print("Error:", response.status_code)