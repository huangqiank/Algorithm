# 请你仅使用两个队列实现一个后入先出（LIFO）的栈，并支持普通队列的全部四种操作（push、top、pop 和 empty）。
#
# 实现 MyStack 类：
#
# void push(int x) 将元素 x 压入栈顶。
# int pop() 移除并返回栈顶元素。
# int top() 返回栈顶元素。
# boolean empty() 如果栈是空的，返回 true ；否则，返回 false 。
#

class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.a = []
        self.b = []

    def push(self, x: int) -> None:
        ## 保证后进的放在头部,两个list谁是空放那个 ,再把另外一个接在尾部。
        """
        Push element x onto stack.
        """
        if len(self.a) == 0:
            self.a.append(x)
            while len(self.b) >= 0:
                tmp = self.b.pop(0)
                self.a.append(tmp)
        elif len(self.b) == 0:
            self.b.append(x)
            while len(self.a) >= 0:
                tmp = self.a.pop(0)
                self.b.append(tmp)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if len(self.a) != 0:
            return self.a.pop(0)
        if len(self.b) != 0:
            return self.b.pop(0)
        return None

    def top(self):
        if len(self.a) != 0:
            return self.a[0]
        if len(self.b) != 0:
            return self.b[0]
        return None

    def empty(self):
        if len(self.a) != 0 or len(self.b) != 0:
            return True
        return False
