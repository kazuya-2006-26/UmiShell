import assets.help_command as help_command
import time
import requests

def greet():
    print("Hello, world!")

def count(seconds):
    i = 1
    while i < int(seconds):
        print(i)
        time.sleep(1)
        i += 1
    print(f"{seconds}\nTime's up!")

def joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    joke_data = response.json()
    print(f"Joke: {joke_data['setup']}")
    print(f"Punchline: {joke_data['punchline']}")