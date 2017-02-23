class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def helper(number, res, result, solution):
            for i in xrange(len(number)):
                if i != len(number) - 1 and number[i] == number[i + 1]:
                    continue
                num = number[i]
                if res - num == 0:
                    result.append(solution + [num])
                elif res - num < 0:
                    continue
                else:
                    helper(number[i:], res - num, result, solution + [num])
            return result
        
        return helper(sorted(candidates), target, [], [])
