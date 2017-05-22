class Solution(object):

    def isPowerOfThree(self, n):

        """

        :type n: int

        :rtype: bool

        """
        if n <= 0:

            return False

        else:    

            while n > 1 and n % 3 == 0:
		n /= 3
	    
	    if n == 1:
		return True
	    else:
		return False 

a = Solution()
print a.isPowerOfThree(45)
