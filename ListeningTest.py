import requests
import webbrowser
import socket

url = "https://listen-together-sdjm.onrender.com"
sc = socket.socket()

def check_request():
    request = requests.get(url)
    return request
webbrowser.open(url)
ip = sc.gethostname()
request = check_request()
print(ip)