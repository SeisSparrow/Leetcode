import math
class Solution(object):

    def climbStairs(self, n):

        """

        :type n: int

        :rtype: int

        """

	sqrt5 = math.sqrt(5)

        return int(sqrt5 / 5 * (pow((1+sqrt5)/2, n+1) - pow((1-sqrt5)/2, n+1)))

a = Solution()
print a.climbStairs(2)
