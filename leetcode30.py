class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        n = len(words)
        l = len(words[0])
        res = []
        wordCnt = {}
        for word in words:
            wordCnt[word] = wordCnt[word] + 1 if word in wordCnt else 1
        for i in xrange(len(s) - n * l + 1):
            cnt = 0
            tmpCnt = {}
            while cnt < n:
                word = s[i + l * cnt : i + l * (cnt + 1)]
                if word not in wordCnt:
                    break
                elif word in tmpCnt:
                    if tmpCnt[word] >= wordCnt[word]:
                        break
                    else:
                        tmpCnt[word] += 1
                else:
                    tmpCnt[word] = 1
                cnt += 1
            if cnt == n:
                res.append(i)
        return res