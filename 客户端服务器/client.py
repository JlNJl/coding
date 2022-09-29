import socket
import sys
host_c = sys.argv[1]
port_c = sys.argv[2]

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# try:
client.connect((host_c,int(port_c)))
# except error as e:
#     print("something goes wrong !:%s"%e)
client.send("123456".encode())
response = client.recv(2048)
print(response)