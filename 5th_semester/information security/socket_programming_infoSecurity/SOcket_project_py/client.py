import socket

HOST = '127.0.0.1'
PORT = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

print("Connected to server!")

while True:
    try:
        msg = input("You: ")
        client.send(msg.encode())

        data = client.recv(1024)

        if not data:
            print("Server disconnected!")
            break

        print("Server:", data.decode())

    except:
        print("Error / Server disconnected")
        break

client.close()