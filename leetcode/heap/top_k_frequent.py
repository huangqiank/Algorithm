##692. 前K个高频单词
##给一非空的单词列表，返回前 k 个出现次数最多的单词。
#返回的答案应该按单词出现频率由高到低排序。如果不同的单词有相同出现频率，按字母顺序排序。
#示例 1：
#输入: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
#输出: ["i", "love"]
#解析: "i" 和 "love" 为出现次数最多的两个单词，均为2次。
#    注意，按字母顺序 "i" 在 "love" 之前。
#示例 2：
#输入: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
#输出: ["the", "is", "sunny", "day"]
#解析: "the", "is", "sunny" 和 "day" 是出现次数最多的四个单词，
# 出现次数依次为 4, 3, 2 和 1 次。
#注意：
#假定 k 总为有效值， 1 ≤ k ≤ 集合元素数。
#输入的单词均由小写字母组成。
#扩展练习：
#尝试以 O(n log k) 时间复杂度和 O(n) 空间复杂度解决。
import heapq


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_count={}
        for word in words:
            if word in word_count:
                word_count[word] +=1
            else:
                word_count[word] = 1
        res = []
        for word in word_count.keys():
            res.append((-word_count[word],word))
        h =  res[:k]
        heapq._heapify_max(h)
        n= len(res)
        for i in range(k,n):
            if res[i] < h[0]:
                heapq._heapreplace_max(h,res[i])
        h = sorted(h,key=lambda x:(x[0],x[1]))
        ans = []
        for pair in h:
            ans.append(pair[1])
        return ans


##不可以用 minheap 因为字母比较的时候大的在堆的前面
import heapq
from collections import defaultdict


class Solution2:

    def topKFrequent(self, words, k):
        words_cnt = defaultdict(int)
        heap = []
        for word in words:
            words_cnt[word] += 1
        words = list(words_cnt.keys())
        for i in range(k):
            heap.append((words_cnt[words[i]], words[i]))
        heapq.heapify(heap)
        for i in range(k, len(words)):
            print(heap)
            if words_cnt[words[i]] > heap[0][0] or (words_cnt[words[i]] == heap[0][0] and words[i] < heap[0][1]):
                heapq.heappop(heap)
                heapq.heappush(heap, (words_cnt[words[i]], words[i]))
        heap = sorted(heap, key=lambda x: (-x[0], x[1]))
        res = []
        for cnt, word in heap:
            res.append(word)
        return res


s = Solution2()
# print(s.topKFrequent(
# ["i","love","leetcode","i","love","coding"],3))
# print("leetcode" < "coding")
print(s.topKFrequent(["aaa", "aa", "a"], 2))

s= Solution()
print(s.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"],3))
print("coding" < "leetcode")


