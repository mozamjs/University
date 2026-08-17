#include <iostream>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <cstring>

using namespace std;

#define PORT 8080

int main()
{
    // STEP 1: Create socket
    int sock = socket(AF_INET, SOCK_STREAM, 0);
    if (sock < 0)
    {
        perror("Socket creation failed");
        return 1;
    }

    // STEP 2: Define server address
    struct sockaddr_in server_addr;
    memset(&server_addr, 0, sizeof(server_addr));

    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(PORT);

    // Convert IP address
    if (inet_pton(AF_INET, "127.0.0.1", &server_addr.sin_addr) <= 0)
    {
        perror("Invalid address");
        return 1;
    }

    // STEP 3: Connect to server
    if (connect(sock, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0)
    {
        perror("Connection failed");
        return 1;
    }

    cout << "Connected to server!" << endl;

    while (true)
    {

        string message;
        cout << "You: ";
        getline(cin, message);

        if (message == "exit")
        {
            send(sock, message.c_str(), message.length(), 0);
            cout << "You ended chat\n";
            break;
        }

        send(sock, message.c_str(), message.length(), 0);

        char buffer[1024] = {0};
        int bytes = recv(sock, buffer, sizeof(buffer), 0);



        if (bytes <= 0)
        {
            cout << "Server disconnected!\n";
            break;
        }

       string msg(buffer, bytes);

        if (msg == "exit")
        {
            cout << "Server ended chat\n";
            break;
        }


        cout << "Server: " << buffer << endl;
    }

    // STEP 6: Close socket
    close(sock);

    return 0;
}