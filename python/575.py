class Solution(object):

    def distributeCandies(self, candies):

        """

        :type candies: List[int]

        :rtype: int

        """
        nn = len(candies)
	n = nn/2
	candies_up = sorted(candies)
	no_kinds = 1

	for i in range(0, nn-1):
	    if candies_up[i] != candies_up[i+1]:
		no_kinds += 1
	if no_kinds <= n:
	    return no_kinds
	if no_kinds > n:
	    return n	

#a = Solution()
#sss = [1,2,1,3,6,2]
#print a.distributeCandies(sss)
