"""handles connections"""
import socket
import threading

serverAddres = "127.0.0.1"  # Localhost
serverPort = 1500

clientSockets = []

def handle_client(clientSocket): #handles the client connection
    while True:
        #code to handle client messages and broadcast to other clients
        clientSocket.close()

def start_server():
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind((serverAddres, serverPort))
    serverSocket.listen()

    print("Server is listening on {}:{}".format(serverAddres, serverPort))

    while True:
        clientSocket, clientAddress = serverSocket.accept()
        print("New connection from {}:{}".format(clientAddress[0], clientAddress[1]))

        clientSockets.append(clientSocket)

        thread =threading.Thread(target=handle_client, args=(clientSocket,))
        thread.start()