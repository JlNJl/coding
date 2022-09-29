# 定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。

 

# 示例:

# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.min();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.min();   --> 返回 -2.
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l,self.bak=[],[]

    def push(self, x: int) -> None:
        self.l.append(x)
        for i in self.bak:
            if x<i:self.bak.append(x)

    def pop(self) -> None:
        self.l.pop()
        self.bak.pop()



    def top(self) -> int:
        self.l.pop()


    def min(self) -> int:
        return self.bak.pop()


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
# obj.pop()
# print(obj.top())
print(obj.min())