"""Sends and recieves"""

import socket
import threading

serverAddres = "127.0.0.1"  # Localhost
serverPort = 1500

def connect_client():
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((serverAddres, serverPort))

    threading.Thread(target=receive_message, args=(clientSocket,)).start()

def receive_message(clientSocket):
    while True:
        """Receives messages from the server and prints them to the console."""