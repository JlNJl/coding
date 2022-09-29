# 给你一个数组 nums 。数组「动态和」的计算公式为：runningSum[i] = sum(nums[0]…nums[i]) 。

# 请返回 nums 的动态和。

 

# 示例 1：

# 输入：nums = [1,2,3,4]
# 输出：[1,3,6,10]
# 解释：动态和计算过程为 [1, 1+2, 1+2+3, 1+2+3+4] 。

# 示例 2：

# 输入：nums = [1,1,1,1,1]
# 输出：[1,2,3,4,5]
# 解释：动态和计算过程为 [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1] 。
def runningSum1(nums: list[int]) -> list[int]:
    l=[]
    for i in range(0,len(nums)):
        if i>0:
            l.append(nums[i]+l[i-1])
        if i == 0:
            l.append(nums[i])
    return l
num=[1,2,3,4]

s=runningSum1(nums=num)
print("1:",s)

#-------------------------------------------------------
def runningSum2(nums: list[int]) -> list[int]:
    l=[]
    l.append(nums[0])
    for i in range(1,len(nums)):
            l.append(nums[i]+l[i-1])
    return l
num=[1,2,3,4]

s=runningSum2(nums=num)
print("2:",s)
#---------------------------------------------------------
def runningSum3(nums: list[int]) -> list[int]:
    l=[0]*len(nums)
    l[0]=nums[0]
    for i in range(1,len(nums)):
            l[i]=nums[i]+l[i-1]
    return l
num=[1,2,3,4]

s=runningSum3(nums=num)
print("3:",s)