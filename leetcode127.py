class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if len(beginWord) != len(endWord):
            return 0
        word_set = set(wordList)
        word_set.add(endWord)
        queue = [(1, beginWord)]
        while queue:
            count, word = queue[0]
            del queue[0]
            if word == endWord:
                return count
            else:
                for i in xrange(len(word)):
                    for ch in 'abcdefghijklmnopqrstuvwxyz':
                        current_word = word[:i] + ch + word[i+1:]
                        if current_word in word_set:
                            queue.append((count+1, current_word))
                            word_set.remove(current_word)
        return 0


