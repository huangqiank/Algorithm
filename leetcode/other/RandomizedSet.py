
# 380. 常数时间插入、删除和获取随机元素
# 设计一个支持在平均 时间复杂度 O(1) 下，执行以下操作的数据结构。
# insert(val)：当元素 vl 不存在时，向集合中插入该项。
# remove(val)：元素 val 存在时，从集合中移除该项。
# getRandom：随机返回现有集合中的一项。每个元素应该有相同的概率被返回。
# 示例 :
# // 初始化一个空的集合。
# RandomizedSet randomSet = new RandomizedSet();
# // 向集合中插入 1 。返回 true 表示 1 被成功地插入。
# randomSet.insert(1);
# // 返回 false ，表示集合中不存在 2 。
# randomSet.remove(2);
# // 向集合中插入 2 。返回 true 。集合现在包含 [1,2] 。
# randomSet.insert(2);
# // getRandom 应随机返回 1 或 2 。
# randomSet.getRandom();
# // 从集合中移除 1 ，返回 true 。集合现在包含 [2] 。
# randomSet.remove(1);
# // 2 已在集合中，所以返回 false 。
# randomSet.insert(2);
# // 由于 2 是集合中唯一的数字，getRandom 总是返回 2 。
# randomSet.getRandom();

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.index = 0
        self.nums = []
        while iterator.hasNext():
            self.nums.append(iterator.next())
        self.length = len(self.nums)

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.nums[self.index]

    def next(self):
        """
        :rtype: int
        """
        tmp = self.nums[self.index]
        self.index += 1
        return tmp

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.index < len(self.nums):
            return True
        return False


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num_dict = {}
        self.num_list = []
        self.index = 0

    def insert(self, val: int) -> bool:
        if val not  in self.num_dict:
            self.num_dict[val] = self.index
            self.index+=1
            self.num_list.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val not in self.num_dict:
            return False
        index= self.num_dict[val]
        tmp = self.num_list[-1]
        self.num_list[index]=tmp
        self.num_dict[tmp] = index
        del self.num_dict[val]
        self.num_list.pop()
        self.index-=1
        return True


    def getRandom(self) -> int:
        if len(self.num_list) == 0:
            return -1
        t = random.randint(0, self.index)
        return self.num_list[t]
