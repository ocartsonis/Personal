import requests
import os
from os.path import exists
import csv
import secrets
import webbrowser

# Define the base URL of your backend service
base_url = 'https://listen-together-sdjm.onrender.com'  # Change this to your actual backend URL
secret_code = ''
# Example function to authenticate with Spotify
def authenticate_with_spotify():
    # Send a GET request to the /login endpoint to initiate authentication
    print("pee")
    generate_secret_code()
    try:
        response = requests.get(f'{base_url}/')
        #print(response)
        response.raise_for_status()  # Raise an exception for HTTP errors
    # Process response data...
    except requests.RequestException as e:
        print("Error:", e)

    global secret_code
    secret_code = generate_secret_code()

    webbrowser.open(f'{base_url}/user/{secret_code}')
    print("poop")
    # Check if the request was successful (status code 200)
    print(response.status_code)
    if response.status_code == 200:
        print("Authentication initiated. Please check your browser.")
    else:
        print("Failed to initiate authentication.")

def generate_secret_code():
    #generate a code that is stored in an encrypted file that will be used with requests
    if os.path.exists('secret_code.csv') == False:
        password_length = 13
        private_key = secrets.token_urlsafe(password_length)
        with open('secret_code.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(private_key)
    reader = open('secret_code.csv', 'r')
    return reader.read()

# Example function to retrieve data from a protected endpoint
def get_protected_data():
    # Send a GET request to a protected endpoint (assuming authentication is required)
    response = requests.get(f'{base_url}/listenTogether')
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()  # Assuming the response contains JSON data
        print("Data retrieved successfully:", data)
    else:
        print("Failed to retrieve data.")

# Example function to perform other actions on the backend
def create_session(session_name):
    #FIX THIS BECAUSE DIFFERENCE IN INSTANCES OR SOMETHING

    webbrowser.open(f'{base_url}/hostSession/{session_name}/{secret_code}')
    
    # Check if the request was successful (status code 200)
    

