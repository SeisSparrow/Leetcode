class Solution(object):

    def isHappy(self, n):

        """

        :type n: int

        :rtype: bool

        """
	dic = []
	
	while n != 1 and n not in dic:
	    dic.append(n)
	    nstr = list(str(n))
	    n = 0
	    for a in nstr:
		n += pow(int(a), 2)
	
	if n == 1:
	    return True
	else:
	    return False

a = Solution()
print a.isHappy(19) 
