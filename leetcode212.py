class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        def dfs(word, node, location):
            row, col = location
            node = node.children.get(board[row][col])
            if node is None:
                return
            dz = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            visited[row][col] = True
            for x, y in dz:
                newRow = row + x
                newCol = col + y
                if 0 <= newRow < len(board) and 0 <= newCol < len(board[0]) and not visited[newRow][newCol]:
                    dfs(word + board[newRow][newCol], node, (newRow, newCol))
            if node.isWord:
                result.add(word)
                trie.delete(word)
            visited[row][col] = False
        
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        visited = [[False for i in xrange(len(board[0]))] for j in xrange(len(board))]
        result = set()

        for row in xrange(len(board)):
            for col in xrange(len(board[0])):
                dfs(board[row][col], trie.root, (row, col))
        
        return sorted(list(result))



class TrieNode():
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isWord = True
    
    def delete(self, word):
        node = self.root
        stack = []
        for ch in word:
            stack.append((ch, node))
            node = node.children.get(ch)
            if node is None:
                return False
        if not node.isWord:
            return False
        if len(node.children):
            node.isWord = False
        else:
            while stack:
                ch, node = stack.pop()
                del node.children[ch]
                if len(node.children) or node.isWord:
                    break
        return True
