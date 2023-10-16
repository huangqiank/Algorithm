##211. 添加与搜索单词 - 数据结构设计
# 请你设计一个数据结构，支持 添加新单词 和 查找字符串是否与任何先前添加的字符串匹配 。
# 实现词典类 WordDictionary ：
# WordDictionary() 初始化词典对象
# void addWord(word) 将 word 添加到数据结构中，之后可以对它进行匹配
# bool search(word) 如果数据结构中存在字符串与 word 匹配，则返回 true ；否则，返回  false 。word 中可能包含一些 '.' ，每个 . 都可以表示任何一个字母。
# 示例：
# 输入：
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# 输出：
# [null,null,null,null,false,true,true,true]
# 解释：
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = {}
        self.end = False

    def addWord(self, word: str) -> None:
        s = self
        for i in word:
            if i not in s.children:
                s.children[i] = WordDictionary()
            s = s.children[i]
        s.end = True

    def search(self, word):
        return self.search_help(word, 0)

    def search_help(self, word, index):
        if index == len(word):
            return self.end
        s = self
        if word[index] == ".":
            for j in s.children.values():
                if j.search_help(word, index + 1):
                    return True
        if word[index] in s.children:
            s = s.children[word[index]]
            return s.search_help(word, index + 1)
        return False


wordDictionary = WordDictionary()
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")

wordDictionary.search("pad")
wordDictionary.search("bad")
print(wordDictionary.search(".ad"))
print(wordDictionary.search("b.."))
