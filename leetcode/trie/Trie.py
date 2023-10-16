##208. 实现 Trie (前缀树)
# Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补完和拼写检查。
# 请你实现 Trie 类：
# Trie() 初始化前缀树对象。
# void insert(String word) 向前缀树中插入字符串 word 。
# boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。
# boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。
# 示例：
# 输入
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# 输出
# [null, null, true, false, true, null, true]
# 解释
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // 返回 True
# trie.search("app");     // 返回 False
# trie.startsWith("app"); // 返回 True
# trie.insert("app");
# trie.search("app");     // 返回 True
class Trie2:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = {}
        self.is_end = False

    def insert(self, word):
        c = self.children
        for i in range(len(word)):
            if word[i] not in c:
                c[word[i]] = Trie()
            c = c[word[i]]
        c.is_end = True

    def search(self, word):
        s = self.startprefix(word)
        if s != None:
            return s.is_end
        return False

    def startprefix(self, word):
        s = self
        for i in word:
            if i not in s.children:
                return None
            s = s.children[i]
        return s

    def startsWith(self, word):
        if self.startprefix(word) != None:
            return True
        return False


##1804. 实现 Trie （前缀树） II
# 前缀树（trie ，发音为 "try"）是一个树状的数据结构，用于高效地存储和检索一系列字符串的前缀。前缀树有许多应用，如自动补全和拼写检查。
# 实现前缀树 Trie 类：
# Trie() 初始化前缀树对象。
# void insert(String word) 将字符串 word 插入前缀树中。
# int countWordsEqualTo(String word) 返回前缀树中字符串 word 的实例个数。
# int countWordsStartingWith(String prefix) 返回前缀树中以 prefix 为前缀的字符串个数。
# void erase(String word) 从前缀树中移除字符串 word 。
# 示例 1:
# 输入
# ["Trie", "insert", "insert", "countWordsEqualTo", "countWordsStartingWith", "erase", "countWordsEqualTo", "countWordsStartingWith", "erase", "countWordsStartingWith"]
# [[], ["apple"], ["apple"], ["apple"], ["app"], ["apple"], ["apple"], ["app"], ["apple"], ["app"]]
# 输出
# [null, null, null, 2, 2, null, 1, 1, null, 0]
# 解释
# Trie trie = new Trie();
# trie.insert("apple");               // 插入 "apple"。
# trie.insert("apple");               // 插入另一个 "apple"。
# trie.countWordsEqualTo("apple");    // 有两个 "apple" 实例，所以返回 2。
# trie.countWordsStartingWith("app"); // "app" 是 "apple" 的前缀，所以返回 2。
# trie.erase("apple");                // 移除一个 "apple"。
# trie.countWordsEqualTo("apple");    // 现在只有一个 "apple" 实例，所以返回 1。
# trie.countWordsStartingWith("app"); // 返回 1
# trie.erase("apple");                // 移除 "apple"。现在前缀树是空的。
# trie.countWordsStartingWith("app"); // 返回 0

class Trie:

    def __init__(self):
        self.children = {}
        self.count1 = 0
        self.count2 = 0

    def insert(self, word: str) -> None:
        s = self
        for i in word:
            if i not in s.children:
                s.children[i] = Trie()
            s = s.children[i]
            s.count1 += 1
        s.count2 += 1

    def countWordsEqualTo(self, word: str) -> int:
        s = self.wordsStartingWith(word)
        if s is None:
            return 0
        return s.count2

    def countWordsStartingWith(self, prefix: str) -> int:
        s = self.wordsStartingWith(prefix)
        if s is None:
            return 0
        return s.count1

    def wordsStartingWith(self, prefix: str):
        s = self
        for word in prefix:
            if word not in s.children:
                return None
            s = s.children[word]
        return s

    def erase(self, word: str) -> None:
        s = self
        for i in word:
            s.children[i].count1 -= 1
            s = s.children[i]
        s.count2 -= 1


t = Trie()
t.insert("apple")
t.insert("apple")
print(t.countWordsEqualTo("apple"))
print(t.countWordsStartingWith("app"))
t.erase("apple")
print(t.countWordsEqualTo("apple"))
print(t.countWordsStartingWith("apple"))
t.erase("apple")
print(t.countWordsStartingWith("app"))
