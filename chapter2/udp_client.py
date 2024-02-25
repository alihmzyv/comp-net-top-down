from socket import *

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.bind(('localhost', 12001))
message = input('Input lowercase sentence:')
clientSocket.connect((serverName, serverPort))
clientSocket.send(message.encode())
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print('It waits, so you cannot see this unless a new message received')
print(modifiedMessage.decode())
clientSocket.close()
