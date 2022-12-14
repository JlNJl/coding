# 输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

 

# 示例 1：

# 输入：head = [1,3,2]
# 输出：[2,3,1]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x:int):
        self.val = x
        self.next = None

class List:
    def __init__(self):
        self.element = ListNode


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        resList = []
        while head:
            resList.append(head.val)
            head = head.next
        return resList[::-1]
if __name__ == "__main__":
    l=[2,3,1,4,5]
    reversePrint(l)