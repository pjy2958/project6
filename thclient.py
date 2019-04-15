import socket
import argparse
import threading

def send(sock) :
    while True :
        msg = input(">>>")
        sock.sendall(msg.encode())

def read(sock) :
    while True :
        resp = sock.recv(1024)
        print(resp.decode())

def run(host, port) :
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s :
        s.connect((host, port))

        sender = threading.Thread(target = send, args = (s, ))
        reader = threading.Thread(target = read, args = (s, ))

        sender.start()
        reader.start()

if __name__ == "__main__" :
    parser = argparse.ArgumentParser(description="Echo client -p port -i host")
    parser.add_argument("-p", help = "port_number", required = True)
    parser.add_argument("-i", help = "host_name", required = True)

    args = parser.parse_args()
    run(host = args.i, port = int(args.p))