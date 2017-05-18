class Solution(object):

    def convertToBase7(self, num):

        """

        :type num: int

        :rtype: str

        """

        out = []
	
	num_abs = abs(num)
	
	while num_abs >= 7:
	    yushu = num_abs % 7
	    out.insert(0, str(yushu))
	    num_abs /= 7
	
	out.insert(0, str(num_abs))
	
	output = ''.join(out)

	if num > 0:
	    return str(int(output))
	elif num < 0:
	    return str(-1 * int(output))
	else:
	    return str(0)

a = Solution()

print a.convertToBase7(100)
	    
