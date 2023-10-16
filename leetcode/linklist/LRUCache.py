###146. LRU 缓存
# 请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
# 实现 LRUCache 类：
# LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
# int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
# void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
# 函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。
# 示例：
# 输入
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# 输出
# [null, null, null, 1, null, -1, null, -1, 3, 4]
from collections import deque, defaultdict
from functools import lru_cache


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.cache = {}

    def put(self, key, val):
        if key in self.cache:
            node = self.cache[key]
            node.val = val
            self.move_node(node)
        else:
            node = Node(key, val)
            self.add_head(node)
            self.cache[key] = node
            self.size += 1
        if self.size > self.capacity:
            tmp =self.remove_tail()
            self.capacity.pop(tmp)
            self.size -= 1
        return

    def remove_tail(self):
        node = self.tail.pre
        self.remove_node(node)
        return node.key

    def add_head(self, node):
        self.head.next.pre = node
        node.next = self.head.next
        node.pre = self.head
        self.head.next = node

    def move_node(self, node):
        self.remove_node(node)
        self.add_head(node)

    def remove_node(self, node):
        node.next.pre = node.pre
        node.pre.next = node.next

    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.move_node(node)
        return node.val


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None


class LRUCache1:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.dict = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.size = 0

    def remove(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
        del self.dict[node.key]

    def add_tail(self, node):
        node.pre = self.tail.pre
        node.next = self.tail
        self.tail.pre.next = node
        self.tail.pre = node
        self.dict[node.key] = node

    def move_tail(self, node):
        self.remove(node)
        self.add_tail(node)

    def get(self, key: int) -> int:
        if key in self.dict:
            node = self.dict[key]
            self.move_tail(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            node = self.dict[key]
            node.key = key
            node.value = value
            self.move_tail(node)
            return
        node = Node(key, value)
        self.add_tail(node)
        self.size += 1
        if self.size > self.cap:
            self.remove(self.head.next)
            self.size -= 1




class Solution12:
    def findLongestChain(self, pairs):

        graph= {}
        n = len(pairs)
        pairs= sorted(pairs)
        for i in range(n):
            for j in range(i+1,n):
                if pairs[i][1] < pairs[j][0]:
                    if i in graph:
                        graph[i].append(j)
                    else:
                        graph[i] = [j]
        if len(pairs) == 0 :
            return 0
        max_l = 1
        self.graph = graph

        for i in graph.keys():
            max_l = max(max_l,self.dfs(i))
        return max_l

    @lru_cache(None)
    def dfs(self,node):
        max_l = 1
        if node not in self.graph:
            return max_l
        for i in self.graph[node]:
            max_l = max(max_l, 1 + self.dfs(i))
        return max_l

words= ["qw","qw","a"]
words = sorted(words, key=lambda x: len(x))
print(words)