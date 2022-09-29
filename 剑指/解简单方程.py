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


def runningSum(nums: list[int]) -> list[int]:
    l=[]
    for i in range(0,len(nums)):
        if i>0:
            l.append(nums[i]+l[i-1])
        if i == 0:
            l.append(nums[i])
    return l
num=[1,2,3,4]

s=runningSum(nums=num)
print(s)