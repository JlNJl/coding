from http import client
import threading
import socket 
import sys
from urllib import request
# host_s = sys.argv[1]
# port_s = sys.argv[2]
host_s = "0.0.0.0"
port_s = 9999
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    server.bind((host_s,port_s))
except:
    print("bind fail !")
server.listen(5)
print("server listen on %s : %d"%(host_s,port_s))
def handle_client(client_socket):
    request = client_socket.recv(1024)
    print("*received:%s"%request)
    client_socket.send("ACK!".encode())
    client_socket.close()
while(1):
    client,addr = server.accept()
    print("Accepted connection from:%s:%d"%(addr[0],addr[1]))
    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()