import os
while(1):
    cmd=input()
    output=os.popen(cmd).readlines()
    print(''.join(output))
    