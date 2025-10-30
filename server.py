import socket
import logging
import datetime
import random


logging.basicConfig(
    level=logging.INFO,
    format=('%(asctime)s - %(levelname)s - %(message)s'),
    handlers=[
        logging.FileHandler("server_log.file")
    ]
)


#constants
QUEUE_LINE = 5
MAX_PACKET = 4
HOST = '0.0.0.0'
PORT = 6767
SERVER_NAME = 'Alon_server'


def handle_client(client_socket:socket.socket, client_address:tuple):
    try:
        while 1 == 1:
            command = client_socket.recv(MAX_PACKET).decode().strip()
            if command == 'TIME':
                logging.info("Sending time")
                client_socket.send(datetime.datetime.now().strftime("%H:%M:%S").encode())
            elif command == 'NAME':
                logging.info("Sending server name")
                client_socket.send(SERVER_NAME.encode())
            elif command == 'RAND':
                logging.info("Sending Random number")
                client_socket.send(str(random.randint(1,10)).encode())
            elif command == 'EXIT':
                logging.error("Client closed connection")
                client_socket.send('GoodBye!'.encode())
                break
            else:
                logging.info("Invalid command")
                client_socket.send("Invalid command".encode())
    except socket.error as msg:
        print('received socket error ' + str(msg))
    finally:
        client_socket.close()


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        logging.info("Starting communication")
        server_socket.bind((HOST, PORT))
        server_socket.listen(QUEUE_LINE)
        client_socket, client_address = server_socket.accept()
        logging.info("server connection succeeded")
        handle_client(client_socket, client_address)
    except socket.error as msg:
        logging.info("server Connection failed")
        print('received socket error ' + str(msg))
    finally:
        logging.info("closing server socket")
        server_socket.close()

def main():
    start_server()      
        

if __name__ == "__main__":
    main()