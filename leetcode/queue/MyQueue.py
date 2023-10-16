##232. 用栈实现队列
#请你仅使用两个栈实现先入先出队列。队列应当支持一般队列支持的所有操作（push、pop、peek、empty）：
#实现 MyQueue 类：
#void push(int x) 将元素 x 推到队列的末尾
#int pop() 从队列的开头移除并返回元素
#int peek() 返回队列开头的元素
#boolean empty() 如果队列为空，返回 true ；否则，返回 false
#说明：
#你 只能 使用标准的栈操作 —— 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
#你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
#示例 1：
#输入：
#["MyQueue", "push", "push", "peek", "pop", "empty"]
#[[], [1], [2], [], [], []]
#输出：
#[null, null, null, 1, 1, false]

class MyQueue:

    def __init__(self):

        self.s1=[]
        self.s2=[]
        self.front = None


    def push(self, x: int) -> None:
        if len(self.s1) == 0 :
            self.s1.append(x)
            self.front = x
        else:
            self.s1.append(x)

    def pop(self) -> int:
        if len(self.s2) == 0 :
            while len(self.s1) != 0 :
                self.s2.append(self.s1.pop())
        return self.s2.pop()


    def peek(self) -> int:
        if len(self.s2) != 0 :
            return self.s2[-1]
        return self.front


    def empty(self) -> bool:
        return len(self.s1) ==0 and len(self.s2) ==0


## 123 []  1
## []  32   1
##

for i in "abc":
    print(i)

    ##给定一个由 0 和 1 组成的数组 arr ，将数组分成  3 个非空的部分 ，使得所有这些部分表示相同的二进制值。

#如果可以做到，请返回任何 [i, j]，其中 i+1 < j，这样一来：

#arr[0], arr[1], ..., arr[i] 为第一部分；
#arr[i + 1], arr[i + 2], ..., arr[j - 1] 为第二部分；
#arr[j], arr[j + 1], ..., arr[arr.length - 1] 为第三部分。
#这三个部分所表示的二进制值相等。
#如果无法做到，就返回 [-1, -1]。
#注意，在考虑每个部分所表示的二进制时，应当将其看作一个整体。例如，[1,1,0] 表示十进制中的 6，而不会是 3。此外，前导零也是被允许的，所以 [0,1,1] 和 [1,1] 表示相同的值。