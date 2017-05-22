"""
Use the trie to implement it
"""
class Node:
    def __init__(self):
        """
        Initialize the node for trie here.

        children: the pointer to the child node, default value is None.
        end_flag: the flag to indicate whether this character is an end of a word in the WordDictionary. Default value is False.
        """
        self.children = dict()
        self.end_flag = False


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node()


    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        ptr = self.head
        for ch in word:
            if ch not in ptr.children:
                ptr.children[ch] = Node()
            ptr = ptr.children[ch]
        ptr.end_flag = True


    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        def helper(string, root):
            """
            Check whether there is a string existed in the Trie defined with root node
            """
            if root is None:
                return False
            if len(string) == 0:
                return root.end_flag
            ch = string[0]
            if ch != '.':
                return helper(string[1:], root.children.get(ch, None))
            else:
                result = False
                for key in root.children.keys():
                    result |= helper(string[1:], root.children[key])
                return result

        return helper(word, self.head)


"""
Use the dictionary and set to implement it
"""
class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.word_dict = collections.defaultdict(set)


    def addWord(self, word):
        """
        Adds a word into the data structure.
        Use the length as the key
        :type word: str
        :rtype: void
        """
        length = len(word)
        self.word_dict[length].add(word)


    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        length = len(word)
        if not word:
            return False
        if '.' not in word:
            return (word in self.word_dict[length])
        for v in self.word_dict[length]:
            for i, ch in enumerate(word):
                if ch != v[i] and ch != '.':
                    break
                if i == length - 1:
                    return True
        return False





# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
