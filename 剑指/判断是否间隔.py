#构造长度为a+b的数组，其中有a个1，b个2，且任意相邻的乘积都是偶数，不行输出-1，可以输出任意解
# #b个2里面插入a个1,b+1个位置

import sys 
for line in sys.stdin:
    x = line.split()
    a=int(x[0])
    b=int(x[1])
    if a > (b+1):
        print(-1)
        break
    else:
        for i in range(0,a):
            sys.stdout.write(str("1 "))
            sys.stdout.write(str("2 "))
        for i in range(b-a):
            sys.stdout.write(str("2"))
        break
    #print("1 2 2 1")