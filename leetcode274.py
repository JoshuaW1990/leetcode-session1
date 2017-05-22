class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citation_list = list(citations)
        citation_list.sort()
        citation_list.reverse()
        citation = 0
        for count, citation in enumerate(citation_list):
            if count >= citation:
                return count
        return len(citations)
