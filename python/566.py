class Solution(object):

    def matrixReshape(self, nums, r, c):

        """

        :type nums: List[List[int]]

        :type r: int

        :type c: int

        :rtype: List[List[int]]

        """
        nn = 0
        n1 = len(nums)
	nums_temp = []
	nums_new = []

        for i in range(0, n1):
	    nn += len(nums[i])
	    for j in range(0, len(nums[i])):
		nums_temp.append(nums[i][j])

	if r * c != nn:
	    return nums
	else:
	    for i in range(0, r):
		nums_new.append([])
		for j in range(0, c):
		    nums_new[i].append(nums_temp[i*c+j]) 
		  
	return nums_new

a = Solution()
matrix_in = [[1,2],[3,4]]
no_r = 4
no_c = 1
print a.matrixReshape(matrix_in, no_r, no_c)
