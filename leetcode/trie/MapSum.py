##677. 键值映射
# 设计一个 map ，满足以下几点:
# 字符串表示键，整数表示值
# 返回具有前缀等于给定字符串的键的值的总和
# 实现一个 MapSum 类：
# MapSum() 初始化 MapSum 对象
# void insert(String key, int val) 插入 key-val 键值对，字符串表示键 key ，整数表示值 val 。如果键 key 已经存在，那么原来的键值对 key-value 将被替代成新的键值对。
# int sum(string prefix) 返回所有以该前缀 prefix 开头的键 key 的值的总和。
# 示例 1：
# 输入：
# ["MapSum", "insert", "sum", "insert", "sum"]
# [[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
# 输出：
# [null, null, 3, null, 5]
# 解释：
# MapSum mapSum = new MapSum();
# mapSum.insert("apple", 3);
# mapSum.sum("ap");           // 返回 3 (apple = 3)
# mapSum.insert("app", 2);
# mapSum.sum("ap");           // 返回 5 (apple + app = 3 + 2 = 5)


class MapSum:

    def __init__(self):
        self.children = {}
        self.num = 0

    def insert(self, key: str, val: int) -> None:
        s = self
        for i in key:
            if i not in s.children:
                s.children[i] = MapSum()
            s = s.children[i]
        s.num = val

    def sum(self, prefix: str) -> int:
        s = self
        for i in prefix:
            if i not in s.children:
                return 0
            s = s.children[i]
        total = 0
        total += s.num
        queue = list(s.children.values())
        while queue:
            n = len(queue)
            while n > 0:
                node = queue.pop(0)
                total += node.num
                for i in node.children.values():
                    queue.append(i)
                n -= 1
        return total

