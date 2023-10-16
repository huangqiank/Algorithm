##剑指 Offer II 033. 变位词组
#给定一个字符串数组 strs ，将 变位词 组合在一起。 可以按任意顺序返回结果列表。
#注意：若两个字符串中每个字符出现的次数都相同，则称它们互为变位词。
#示例 1:
#输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
#输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
#示例 2:
#输入: strs = [""]
#输出: [[""]]


class Solution:
    def groupAnagrams(self, strs):
        str_map = {}
        for s in strs:
            output = self.get_cnt(s)
            str_map[output] = str_map.get(output, []) + [s]
        return list(str_map.values())

    def get_cnt(self, s):
        output = ""
        char_cnt = {}
        n = len(s)
        for i in range(n):
            char_cnt[s[i]] = char_cnt.get(s[i], 0) + 1
        for key in sorted(char_cnt.keys()):
            output += key
            output += str(char_cnt[key])
        return output

s = Solution()
print(s.groupAnagrams(["abc","cba","acb","ab"]))