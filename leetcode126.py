import collections

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        def build_path(source, dest, tree):
            """
            Build the path from the source word to the dest word based on the tree
            :param source: 
            :param dest: 
            :param tree: 
            :return: 
            """
            if source == dest:
                return [[source]]
            return [[source] + path for succ in tree[source] for path in build_path(succ, dest, tree)]

        def add_path(tree, word, neigh, isForw):
            """
            Add the path info into the tree based on the word and the direction
            :param tree: 
            :param word: 
            :param neigh: 
            :param isForw: 
            :return: 
            """
            if isForw:
                tree[word].append(neigh)
            else:
                tree[neigh].append(word)

        def bfs(thisLev, otherLev, tree, isForw, wordSet):
            """
            run the 2-side BFS for the word ladder and build the tree
            :param thisLev: 
            :param otherLev: 
            :param tree: 
            :param isForw: 
            :param wordSet: 
            :return: 
            """
            if not thisLev:
                return False
            if len(thisLev) > len(otherLev):
                return bfs(otherLev, thisLev, tree, not isForw, wordSet)
            for word in (thisLev | otherLev):
                wordSet.discard(word)
            nextLev, done = set(), False
            while thisLev:
                word = thisLev.pop()
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    for index in range(len(word)):
                        neigh = word[:index] + c + word[index+1:]
                        if neigh in otherLev:
                            done = True
                            add_path(tree, word, neigh, isForw)
                        if not done and neigh in wordSet:
                            nextLev.add(neigh)
                            add_path(tree, word, neigh, isForw)
            return done or bfs(nextLev, otherLev, tree, isForw, wordSet)

        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        tree = collections.defaultdict(list)
        bfs(set([beginWord]), set([endWord]), tree, True, set(wordList))
        return build_path(beginWord, endWord, tree)
