class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if prerequisites == []:
            return False
        course_dict = {}
        for item in prerequisites:
            course_dict[item[0]] = item[1]
        for i in xrange(len(prerequisites)):
            stack = [(prerequisites[i][0], set([prerequisites[i][0]]))]
            while stack:
            	course, visited = stack.pop()
            	if course not in course_dict:
            		if len(visited) == numCourses:
            			return True
            		else:
            			break
            	pre_course = course_dict[course]
            	if pre_course in visited:
            		continue
            	else:
            		visited |= pre_course
            		stack.append(pre_course, visited)
        return False

