##Design a special dictionary with some words that searchs the words in it by a prefix and a suffix.
#Implement the WordFilter class:
#WordFilter(string[] words) Initializes the object with the words in the dictionary.
#f(string prefix, string suffix) Returns the index of the word in the dictionary, which has the prefix prefix and the suffix suffix. If there is more than one valid index, return the largest of them. If there is no such word in the dictionary, return -1.
#Example 1:
#Input
#["WordFilter", "f"]
#[[["apple"]], ["a", "e"]]
#Output
#[null, 0]
#Explanation
#WordFilter wordFilter = new WordFilter(["apple"]);
#wordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix = "a" and suffix = 'e".

class Trie():
    def __init__(self):
        self.children = {}
        self.word = ""
        self.end = 0

    def insert(self, word):
        c = self
        for i in range(len(word)):
            if word[i] not in c.children:
                c.children[word[i]] = Trie()
            c = c.children[word[i]]
        c.word = word
        c.end = 1

    def startwith(self, word):
        c = self
        for i in range(len(word)):
            if word[i] not in c.children:
                return None
            c = c.children[word[i]]
        return c


class Suffix():
    def __init__(self):
        self.children = {}
        self.begin = 0
        self.word = ""

    def insert(self, word):
        c = self
        for i in range(len(word) - 1, -1, -1):
            if word[i] not in c.children:
                c.children[word[i]] = Suffix()
            c = c.children[word[i]]
        c.word = word
        c.begin = 1

    def endwith(self, word):
        c = self
        for i in range(len(word) - 1, -1, -1):
            if word[i] not in c.children:
                return None
            c = c.children[word[i]]
        return c


class WordFilter:

    def __init__(self, words):
        self.t = Trie()
        self.s = Suffix()
        self.words = {}
        for i, word in enumerate(words):
            self.t.insert(word)
            self.s.insert(word)
            self.words[word] = i

    def f(self, prefix: str, suffix: str) -> int:
        s = self.t.startwith(prefix)  ## trie
        start_with_prefix = set()
        tmp = [s]
        while tmp:
            n = len(tmp)
            while n > 0:
                n -= 1
                s = tmp.pop(0)
                if s is None:
                    continue
                if s.end == 1:
                    start_with_prefix.add(s.word)
                for i in s.children.values():
                    tmp.append(i)
        end_with_suffix = set()
        s = self.s.endwith(suffix)
        tmp = [s]
        while tmp:
            n = len(tmp)
            while n > 0:
                s = tmp.pop(0)
                n -= 1
                if s is None:
                    continue
                if s.begin == 1:
                    end_with_suffix.add(s.word)
                for i in s.children.values():
                    tmp.append(i)
        intersect = start_with_prefix.intersection(end_with_suffix)
        max_index = -1
        for word in intersect:
            max_index = max(max_index, self.words[word])
        return max_index