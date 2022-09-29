x = input("输入位置：")
l=x.split()
#print(l)
m=int(l[0])
n=int(l[1])
triangle = [[1], [1, 1]]
for i in range(2, m):  
    pre = triangle[i-1]  
    cul = [1]  
    for j in range(i-1):  
        cul.append(pre[j]+pre[j+1]) 
    cul.append(1)  
    triangle.append(cul)
print("这个数字是:{}".format(triangle[m-1][n-1]))
