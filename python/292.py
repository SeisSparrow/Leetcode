class Solution(object):

    def canWinNim(self, n):

        """

        :type n: int

        :rtype: bool

        """

        if n == 1:
	    return True
 	elif n == 2:
	    return True
	elif n % 4 == 0:
	    return False
	else:
	    return True


