#include <iostream>     // input/output ka lia
#include <sys/socket.h> // socket create / send /recv
#include <netinet/in.h> // IP + port structure (sockadd_in)
#include <unistd.h>     // close()
#include <cstring>      // memset()

using namespace std;
#define PORT 8080 // COMMUNICATION number

int main()
{

    // STEP 1: Create socket
    int server_fd = socket(AF_INET, SOCK_STREAM, 0); // ipv4   TCP   -> phone create karna

    // agar socket create nhi hua
    if (server_fd < 0)
    {
        perror("Socket failed");
        return 1;
    }

    // STEP 2: Define address
    struct sockaddr_in address;
    memset(&address, 0, sizeof(address));
    // Address sturcture banaya + clean kiya
    // e.g  Form bahrna sa pahle blank karna

    // server ka address set :
    //  INADDR_ANY -> ksi bhi ip se connection allow
    // htons() -> port ko netwoek format me convert
    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(PORT);
    // eg. ma ksi bhi number sa call receive karunga

    // STEP 3: Bind
    // socket ko address + port assign kiya
    // phone number active karna
    //  e.g 5 log line ma wait kar sakta hain

    if (bind(server_fd, (struct sockaddr *)&address, sizeof(address)) < 0)
    {
        perror("Bind failed");
        return 1;
    }

    // STEP 4: Listen
    // server ready ha connection ka lia
    // 5 -> max waiting clients
    if (listen(server_fd, 5) < 0)
    {
        perror("Listen failed");
        return 1;
    }

    cout << "Server is listening on port " << PORT << "...\n";

    // infinite loop -> server kabhi band nhi hota

    // step:5 accept
    

    while (true)
    {

        int new_socket = accept(server_fd, NULL, NULL); // client connect hota ha
        // eg: phone call receive

        // agr accept fail -> next try
        if (new_socket < 0)
        {
            perror("Accept failed");
            continue;
        }

        cout << "Client connected!\n";

        // Ek client ka sath continouec chat
        while (true)
        {
            char buffer[1024] = {0}; // msg store karna ka lia memory

            int bytes = recv(new_socket, buffer, sizeof(buffer), 0); // client ka msg receive


             if (bytes <= 0)
            { // 0 -> client closed     < 0 -> error
                cout << "Client disconnected!\n";
                break;
            }

            // receive ke baad exit ka lia 
       string msg(buffer, bytes);

            if (msg == "exit")
            {
                cout << "Client ended chat\n";
              break;
            }

           

            cout << "Client: " << buffer << endl; // msg print

            // Server reply input
            string reply;
            cout << "You: ";
            getline(cin, reply); // server user sa reply input

            send(new_socket, reply.c_str(), reply.length()+1, 0);

            if (reply == "exit")
            {
                cout << "Server ended chat\n";
                break;
            }
        }

        close(new_socket); // client ka connection band
    }

    return 0;
}