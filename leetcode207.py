class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        def dfs(index):
            if visited[index] == -1:
                return False
            if visited[index] == 1:
                return True
            visited[index] = -1
            for course in graph[index]:
                if not dfs(course):
                    return False
            visited[index] = 1
            return True

        graph = [[] for _ in xrange(numCourses)]
        visited = [0 for _ in xrange(numCourses)]
        for cur_course, pre_course in prerequisites:
            graph[cur_course].append(pre_course)

        for i in xrange(numCourses):
            if not dfs(i):
                return False
        return True
