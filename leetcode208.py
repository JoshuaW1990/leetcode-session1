class Node(object):
    def __init__(self):
        """
        Initialize the Node
        """
        self.children = dict()
        self.end_flag = False

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()


    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        ptr = self.root
        for ch in word:
            if ch not in ptr.children:
                ptr.children[ch] = Node()
            ptr = ptr.children[ch]
        ptr.end_flag = True


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        ptr = self.root
        for ch in word:
            if ch not in ptr.children:
                return False
            ptr = ptr.children[ch]
        return ptr.end_flag


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        ptr = self.root
        for ch in prefix:
            if ch not in ptr.children:
                return False
            ptr = ptr.children[ch]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
