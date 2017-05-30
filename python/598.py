class Solution(object):

    def maxCount(self, m, n, ops):

        """

        :type m: int

        :type n: int

        :type ops: List[List[int]]

        :rtype: int

        """
	N = len(ops)

	minx = m

	miny = n

	for i in range(0, N):

	    if ops[i][0] < minx:

		minx = ops[i][0]

	    if ops[i][1] < miny:
		
		miny = ops[i][1]

	return minx * miny

a = Solution()
operations = [[2,2],[3,3]]
print a.maxCount(3, 3, operations)
