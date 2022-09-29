# 定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

 

# 示例:

# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL

 

# 限制：

# 0 <= 节点个数 <= 5000


# Definition for singly-linked list.
import copy
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


for i in range(1,10):
    l=ListNode(i) 
    print(l.val)
    l.next=copy.deepcopy(l)



class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur, pre = head, None
        while cur:
            tmp = cur.next # 暂存后继节点 cur.next
            cur.next = pre # 修改 next 引用指向
            pre = cur      # pre 暂存 cur
            cur = tmp      # cur 访问下一节点
        return pre

