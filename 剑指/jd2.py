#小红定义好数组，当且仅当数组不存在相同元素，空数组也是好数组
# #将相同元素去除，比较二者的差与给定次数的大小，
import sys 
t=input()
while(t):
    l=[]
    n,k =input().split()
    if n==0:
        print("Yes")
    x=input().split() 
    for i in x:
        l.append(i)

    #判断处
    ll=list(set(l))
    if (len(l)-len(ll)>int(k)):
        print("No")
    else:
        print("Yes")
    t=int(t)-1

