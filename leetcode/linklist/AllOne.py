##432. 请你设计一个用于存储字符串计数的数据结构，并能够返回计数最小和最大的字符串。
# 现 AllOne 类：
# AllOne() 初始化数据结构的对象。
# inc(String key) 字符串 key 的计数增加 1 。如果数据结构中尚不存在 key ，那么插入计数为 1 的 key 。
##给你一个括号字符串 s ，它只包含字符 '(' 和 ')' 。一个括号字符串被称为平衡的当它满足：
# 任何左括号 '(' 必须对应两个连续的右括号 '))' 。
# 左括号 '(' 必须在对应的连续两个右括号 '))' 之前。
# 比方说 "())"， "())(())))" 和 "(())())))" 都是平衡的， ")()"， "()))" 和 "(()))" 都是不平衡的。
# 你可以在任意位置插入字符 '(' 和 ')' 使字符串平衡。
# 请你返回让 s 平衡的最少插入次数。
# 示例 1：
# 输入：s = "(()))"
# dec(String key) 字符串 key 的计数减少 1 。如果 key 的计数在减少后为 0 ，那么需要将这个 key 从数据结构中删除。测试用例保证：在减少计数前，key 存在于数据结构中。
# getMaxKey() 返回任意一个计数最大的字符串。如果没有元素存在，返回一个空字符串 "" 。
# getMinKey() 返回任意一个计数最小的字符串。如果没有元素存在，返回一个空字符串 "" 。

# 示例：

# 输入
# ["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]
# [[], ["hello"], ["hello"], [], [], ["leet"], [], []]
# 输出
# [null, null, null, "hello", "hello", null, "hello", "leet"]

# 解释
# AllOne allOne = new AllOne();
# allOne.inc("hello");
# allOne.inc("hello");
# allOne.getMaxKey(); // 返回 "hello"
# allOne.getMinKey(); // 返回 "hello"
# allOne.inc("leet");
# allOne.getMaxKey(); // 返回 "hello"
# allOne.getMinKey(); // 返回 "leet"


class node:
    def __init__(self, key="", cnt=0):
        self.pre = None
        self.next = None
        self.key = {key}
        self.cnt = cnt


class doublelist:
    def __init__(self):
        self.head = node()
        self.tail = node()
        self.head.next = self.tail
        self.tail.pre = self.head

    def insert(self, new, old):
        old.next.pre = new
        new.next = old.next
        old.next = new
        new.pre = old

    def remove(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre


class AllOne:

    def __init__(self):
        self.doublist = doublelist()
        self.key_node = {}

    def inc(self, key):
        if key not in self.key_node:
            if self.doublist.head.next == self.doublist.tail or self.doublist.head.next.cnt > 1:
                new = node(key, 1)
                self.doublist.insert(new, self.doublist.head)
                self.key_node[key] = new
            else:
                self.doublist.head.next.key.add(key)
                self.key_node[key] = self.doublist.head.next
        else:
            cur = self.key_node[key]
            if cur.next == self.doublist.tail or cur.next.cnt > cur.cnt + 1:
                new = node(key, cur.cnt + 1)
                self.doublist.insert(new, cur)
                self.key_node[key] = new
            else:
                cur.next.key.add(key)
                self.key_node[key] = cur.next
            cur.key.remove(key)
            if len(cur.key) == 0:
                self.doublist.remove(cur)

    def dec(self, key):
        cur = self.key_node[key]
        if cur.cnt == 1:
            self.key_node.pop(key)
        else:
            if cur.pre == self.doublist.head or cur.pre.cnt < cur.cnt - 1:
                new = node(key, cur.cnt - 1)
                self.doublist.insert(new, cur.pre)
                self.key_node[key] = new
            else:
                cur.pre.key.add(key)
                self.key_node[key] = cur.pre
        cur.key.remove(key)
        if len(cur.key) == 0:
            self.doublist.remove(cur)

    def getMaxKey(self):
        if self.doublist.tail.pre == self.doublist.head:
            return ""
        return next(iter(self.doublist.tail.pre.key))

    def getMinKey(self) -> str:
        if self.doublist.head.next == self.doublist.tail:
            return ""
        return next(iter(self.doublist.head.next.key))


##输入
#["AllOne","inc","inc","getMaxKey","getMinKey","inc","getMaxKey","getMinKey"]
#[[],["hello"],["hello"],[],[],["leet"],[],[]]
a= AllOne()
a.inc("hello")
print(a.doublist.head.next.key,a.doublist.head.next.cnt)
a.inc("hello")
print(a.doublist.head.next.key,a.doublist.head.next.cnt)
a.inc("leet")
print(a.doublist.head.next.key)

