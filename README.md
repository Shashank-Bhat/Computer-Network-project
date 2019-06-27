# Computer-Network-project
Sayantan Nandy - 01FB16ECS345
Shashank Prabhakar - 01FB16ECS356
Shashank Bhat - 01FB16ECS358

Project Title - Food Ordering system for the PNB Restaturant

This project aims to showcase how to handle multiple clients for a single server.Many restaurants may handle multiple clients but our project aims to make this better by providing a beautiful interface and streamline the entire procedure and make it hassle free.The project mainly uses a threaded server so that it can handle multiple clients.Users can place the order by separating each item with a ",".This project uses the concept of Socket Programming.

Socket programming is a way of connecting two nodes on a network to communicate with each other. One socket(node) listens on a particular port at an IP, while other socket reaches out to the other to form a connection. Server forms the listener socket while client reaches out to the server.A socket can be created by using the function socket.socket().This function takes two parameters and the second parameter is used to tell whether it will be a TCP connection or a UDP connection. socket.sendall(message) sends the message in a particular encoded format to the server.In this case we are using utf-8 format.Thread(target=client_thread, args=(connection, ip, port)).start() function is used so as to start the thread on the server and accept multiple clients.
