class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        dir_list = path.split('/')
        for i, directory in enumerate(dir_list):
            if directory == '' or directory == '.':
                del dir_list[i]
            elif directory == '..':
                del dir_list[i]
                if i != 0:
                    del dir_list[i-1]
        return '/'.join(dir_list)


