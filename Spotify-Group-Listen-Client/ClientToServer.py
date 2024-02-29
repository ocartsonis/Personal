import requests
import os
from os.path import exists
from cryptography.fernet import Fernet

# Define the base URL of your backend service
base_url = 'https://listen-together-sdjm.onrender.com'  # Change this to your actual backend URL
secret_code = ''
# Example function to authenticate with Spotify
def authenticate_with_spotify():
    # Send a GET request to the /login endpoint to initiate authentication
    print("pee")
    try:
        response = requests.get(f'{base_url}/')
        #print(response)
        response.raise_for_status()  # Raise an exception for HTTP errors
    # Process response data...
    except requests.RequestException as e:
        print("Error:", e)
    print("poop")
    # Check if the request was successful (status code 200)
    print(response.status_code)
    if response.status_code == 200:
        print("Authentication initiated. Please check your browser.")
    else:
        print("Failed to initiate authentication.")

def generate_secret_code():
    #generate a code that is stored in an encrypted file that will be used with requests
    if os.path.exists() == False:
        #generate a file that stores the secret code


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
def perform_action():
    # Send a POST request with data to perform an action on the backend
    data = {'key': 'value'}  # Example data to send
    response = requests.post(f'{base_url}/someEndpoint', json=data)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        print("Action performed successfully.")
    else:
        print("Failed to perform action.")

