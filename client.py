import socket
import sys

def main():
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "10.10.2.1"
    port = 8884

    try:
        soc.connect((host, port))
    except:
        print("Connection error")
        sys.exit()

    print("***********************************************************************************************\n");
    print("\tWelcome to PNB restaurant\n");
    print("\tMenu for the Day\n");
    print("\tIdli - \t\tRs 10\n");
    print("\tDosa - \t\tRs 30\n");
    print("\tUpma - \t\tRs 5\n");
    print("\tButterChicken - Rs 80\n");
    print("\tLasagne - \tRs 160\n");
    print("\tTiramisu - \tRs 200\n");
    print("***********************************************************************************************\n");

    items = {
            "idli":10,
            "dosa":30,
            "upma":5,
            "butterchicken":80,
            "lasagne":160,
            "tiramisu":200
            }

    print("Enter your name or 'quit' to exit")
    message = input(" -> ")
    
    while message != 'quit':
        total=0;
        print("Enter your order from the menu separated by a ,")
        message_order = input(" -> ");
        message_order = message_order.lower()
        for m in message_order.split(","):
              item,quantity = m.split(" ")
              if(item in items):
                 total = total + (items.get(item)*int(quantity))
        soc.sendall(message.encode("utf8"))
        message_order = " " + message_order
        soc.sendall(message_order.encode("utf8"))
        if soc.recv(5120).decode("utf8") == "-":
             pass        # null operation
        print("Order Successfully placed")
        print("Grand Total")
        print(total)
        print("Enter your name and 'quit' to exit")
        message = input(" -> ")

    soc.send(b'--quit--')

if __name__ == "__main__":
    main()
