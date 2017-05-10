class Solution(object):

    def islandPerimeter(self, grid):

        """

        :type grid: List[List[int]]

        :rtype: int

        """
        h = len(grid)
	l = len(grid[0])
	
	if h == 1 and l ==1:
	    return 4 * grid[0][0]
	elif h == 1 and l != 1:
	    num = 0
	    for i in range(0, l):
		num += grid[0][i]
	    return 4 * num - 2 * (num-1)
	elif h != 1 and l == 1:
            num = 0
            for i in range(0, h):
                num += grid[0][i]
            return 4 * num - 2 * (num-1)
	else:
	    peri = 0
	    for i in range(0, h):
	        for j in range(0, l):

		    if i == 0:
		        if j == 0 and grid[i][j] == 1:
	  	            peri += 4 - grid[i][j+1] - grid[i+1][j]
		        if j > 0 and j < l-1 and grid[i][j] == 1:
		            peri += 4 - grid[i][j-1] - grid[i][j+1] - grid[i+1][j]
		        if j == l-1 and grid[i][j] == 1:
                            peri += 4 - grid[i][j-1] - grid[i+1][j]
	    	    if i > 0 and i < h-1:
                        if j == 0 and grid[i][j] == 1:
		            peri += 4 - grid[i+1][j] - grid[i-1][j] - grid[i][j+1]
                        if j > 0 and j < l-1 and grid[i][j] == 1:
                            peri += 4 - grid[i+1][j] - grid[i-1][j] - grid[i][j+1] - grid[i][j-1]
                        if j == l-1 and grid[i][j] == 1:
		            peri += 4 - grid[i+1][j] - grid[i-1][j] - grid[i][j-1]
            	    if i == h-1:
                        if j == 0 and grid[i][j] == 1:
                            peri += 4 - grid[i][j+1] - grid[i-1][j]
                        if j > 0 and j < l-1 and grid[i][j] == 1:
                            peri += 4 - grid[i][j-1] - grid[i][j+1] - grid[i-1][j]
                        if j == l-1 and grid[i][j] == 1:
                            peri += 4 - grid[i][j-1] - grid[i-1][j]
	    return peri

#a = Solution()
#sss = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
#sss = [[0,1,0,0],[0,1,1,0]]
#print a.islandPerimeter(sss)

				    
