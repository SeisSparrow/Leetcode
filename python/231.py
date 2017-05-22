class Solution(object):

    def isPowerOfTwo(self, n):

        """

        :type n: int

        :rtype: bool

        """
        if n <= 0:

            return False

        else:    

            while n > 1 and n % 2 == 0:
		n /= 2
	    
	    if n == 1:
		return True
	    else:
		return False 

a = Solution()
print a.isPowerOfThree(45)
