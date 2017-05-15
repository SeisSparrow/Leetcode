class Solution(object):

    def findContentChildren(self, g, s):

        """

        :type g: List[int]

        :type s: List[int]

        :rtype: int

        """
	N_child = len(g)
	N_cookie = len(s)
	g_up = sorted(g)
	s_up = sorted(s)
	
	count = 0
	j0 = 0

	if N_cookie == 0:
	    return 0
	else:
	
	    for i in range(0, N_child):
	    	for j in range(j0, N_cookie):

		    if s_up[j] >= g_up[i]:
		    	count += 1
		    	break
	    	j0 = j+1
	return count

a = Solution()
gg = [1, 2]
ss = []
print a.findContentChildren(gg, ss)
		
