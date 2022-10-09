import base64
f=open("flag.txt","r")
a=f.read()
print(f,a)
res=base64.b64decode(a)

while(1):
    res=base64.b64decode(res)
    print(res)