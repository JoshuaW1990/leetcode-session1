class Solution(object):
    def helper(self, p1, p2):
        """
        calculate the distance and vector between two coordinates
        """
        x1, y1 = p1
        x2, y2 = p2
        vector = [x1 - x2, y1 - y2]
        square_distance = vector[0]**2 + vector[1]**2
        return vector, square_distance

    def vector_mult(self, vec1, vec2):
        x1, y1 = vec1
        x2, y2 = vec2
        return x1 * x2 + y1 * y2

    def validSquare(self, p1, p2, p3, p4):
        """
        Confirm the validSquare according to the definition
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        # try p1 and p2, p3 and p4 combination
        vector1, square_distance1 = self.helper(p1, p2)
        vector2, square_distance2 = self.helper(p3, p4)
        if square_distance1 != square_distance2 or square_distance1 == 0:
            return False
        multiple = self.vector_mult(vector1, vector2)
        if multiple != 0:
            vector3, square_distance3 = self.helper(p1, p3)
            vector4, square_distance4 = self.helper(p2, p4)
            if square_distance3 == square_distance4:
                if multiple > 0:
                    return self.vector_mult(vector1, vector3) == 0
                else:
                    return self.vector_mult(vector3, vector4) == 0
            else:
                return False
        elif multiple == 0:
            return True
