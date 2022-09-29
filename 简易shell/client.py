import socket
host = "192.168.123.163"
port = 9999
while(1):
    try:
        print("$:")
        client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # udp
    #client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #tcp
        cmd = input().encode()
        client.sendto(cmd,(host,port))
        data,addr=client.recvfrom(4096)
        recv = data.decode()
        print(recv)

        
        client.close()
    except KeyboardInterrupt:
        print("bye!")
        break