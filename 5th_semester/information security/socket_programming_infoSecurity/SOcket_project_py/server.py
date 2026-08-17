import socket

HOST = '0.0.0.0'
PORT = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print(f"Server is listening on port {PORT}...")

while True:
    conn, addr = server.accept()
    print(f"Client connected: {addr}")

    while True:
        try:
            data = conn.recv(1024)

            if not data:
                print("Client disconnected!")
                break

            print("Client:", data.decode())

            reply = input("You: ")
            conn.send(reply.encode())

        except:
            print("Error / Client disconnected")
            break

    conn.close()