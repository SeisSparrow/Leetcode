class Solution(object):

    def numberOfBoomerangs(self, points):

        """

        :type points: List[List[int]]

        :rtype: int

        """
	N = len(points)
	count = 0
	
	for a in points:
	    dic = {}

	    for b in points:

		if b != a:
		    dist = pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2)
		    if dist in dic:
			dic[dist] += 1
		    else:
			dic[dist] = 1

	    for c in dic:
		count += dic[c] * (dic[c] - 1)
	return count
		    

a = Solution()
pts = [[0,0],[1,0],[2,0]]
print a.numberOfBoomerangs(pts)
