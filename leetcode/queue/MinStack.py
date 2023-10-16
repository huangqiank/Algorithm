
## list 是stack，从右pop queue 先进先出，从左pop

##155. 最小栈
#设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
#实现 MinStack 类:
#MinStack() 初始化堆栈对象。
#void push(int val) 将元素val推入堆栈。
#void pop() 删除堆栈顶部的元素。
#int top() 获取堆栈顶部的元素。
#int getMin() 获取堆栈中的最小元素。
#示例 1:

#输入：
#["MinStack","push","push","push","getMin","pop","top","getMin"]
#[[],[-2],[0],[-3],[],[],[],[]]

#输出：
#[null,null,null,null,-3,null,0,-2]
class MinStack:

    def __init__(self):
        self.min_stack = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_stack) > 0:
            self.min_stack.append(min(val,self.min_stack[-1]))
        else:
            self.min_stack.append(val)

    def pop(self) -> None:
        self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


##716. 最大栈
#设计一个最大栈数据结构，既支持栈操作，又支持查找栈中最大元素。
# 实现 MaxStack 类：
#MaxStack() 初始化栈对象
#void push(int x) 将元素 x 压入栈中。
#int pop() 移除栈顶元素并返回这个元素。
##int top() 返回栈顶元素，无需移除。
##int peekMax() 检索并返回栈中最大元素，无需移除。
#int popMax() 检索并返回栈中最大元素，并将其移除。如果有多个最大元素，只要移除 最靠近栈顶 的那个。
#示例：

#输入
#["MaxStack", "push", "push", "push", "top", "popMax", "top", "peekMax", "pop", "top"]
#[[], [5], [1], [5], [], [], [], [], [], []]
#输出
#[null, null, null, null, 5, 5, 1, 5, 1, 5]

#解释
#MaxStack stk = new MaxStack();
#stk.push(5);   // [5] - 5 既是栈顶元素，也是最大元素
#stk.push(1);   // [5, 1] - 栈顶元素是 1，最大元素是 5
#stk.push(5);   // [5, 1, 5] - 5 既是栈顶元素，也是最大元素
#stk.top();     // 返回 5，[5, 1, 5] - 栈没有改变
#stk.popMax();  // 返回 5，[5, 1] - 栈发生改变，栈顶元素不再是最大元素
#stk.top();     // 返回 1，[5, 1] - 栈没有改变
#stk.peekMax(); // 返回 5，[5, 1] - 栈没有改变
#stk.pop();     // 返回 1，[5] - 此操作后，5 既是栈顶元素，也是最大元素
#stk.top();     // 返回 5，[5] - 栈没有改变


class MaxStack:

    def __init__(self):
        self.max_stack = []
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.max_stack) > 0:
            self.max_stack.append(max(x, self.max_stack[-1]))
        else:
            self.max_stack.append(x)
        self.stack.append(x)

    def pop(self) -> int:
        self.max_stack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return self.max_stack[-1]

    def popMax(self) -> int:
        tmp1 = self.stack.pop()
        tmp2 = self.max_stack.pop()
        res = []
        while tmp1 != tmp2:
            res.append(tmp1)
            tmp1 = self.stack.pop()
            tmp2 = self.max_stack.pop()

        for i in range(len(res) - 1, -1, -1):
            self.push(res[i])
        return tmp1





