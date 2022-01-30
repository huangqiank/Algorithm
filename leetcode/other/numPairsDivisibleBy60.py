#1010. 总持续时间可被 60 整除的歌曲
#在歌曲列表中，第 i 首歌曲的持续时间为 time[i] 秒。
#返回其总持续时间（以秒为单位）可被 60 整除的歌曲对的数量。
# 形式上，我们希望索引的数字 i 和 j 满足  i < j 且有 (time[i] + time[j]) % 60 == 0。
#示例 1：
#输入：[30,20,150,100,40]
#输出：3
#解释：这三对的总持续时间可被 60 整数：
#(time[0] = 30, time[2] = 150): 总持续时间 180
#(time[1] = 20, time[3] = 100): 总持续时间 120
#(time[1] = 20, time[4] = 40): 总持续时间 60
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        nums_dict = {}
        count = 0
        for i in time:
            tmp = i % 60
            nums_dict[tmp] = nums_dict.get(tmp, 0) + 1
        if 0 in nums_dict:
            count += int(nums_dict[0] * (nums_dict[0] - 1) / 2)
        for i in range(1, 30):
            m = nums_dict.get(i, 0)
            n = nums_dict.get(60 - i, 0)
            count += m * n
        if 30 in nums_dict:
            count += int(nums_dict[30] * (nums_dict[30] - 1) / 2)
        return count
