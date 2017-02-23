class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def helper(number, start, res, result, solution):
            if res == 0:
                result.append(solution)
                return
            for i in xrange(start, len(number)):
                if i > start and number[i] == number[i - 1]:
                    continue
                if number[i] > res:
                    break
                helper(number, i + 1, res - number[i], result, solution + [number[i]])
        
        result = []
        helper(sorted(candidates), 0, target, result, [])
        return result
        
