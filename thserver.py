import socket
import argparse
import threading

def send(conn) :
    while True :
        msg = input(">>>")
        conn.sendall(msg.encode())

def read(conn) :
    while True :
        resp = conn.recv(1024)
        print(resp.decode())

def run_server(port = 4000) :
    host = ""

    with socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM) as s :
        s.bind((host, port))
        s.listen(1)
        conn, addr = s.accept()
            
        sender = threading.Thread(target = send, args = (conn, ))
        reader = threading.Thread(target = read, args = (conn, ))

        sender.start()
        reader.start()

        conn.close()

if __name__ == "__main__" :
    parser = argparse.ArgumentParser(description = "Echo server -p port")
    parser.add_argument("-p", help = "port_number", required = True)

    args = parser.parse_args()
    run_server(port = int(args.p))

