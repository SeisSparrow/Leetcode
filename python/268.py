class Solution(object):

    def missingNumber(self, nums):

        """

        :type nums: List[int]

        :rtype: int

        """
	n = len(nums)
	nums_up = sorted(nums)

	if nums_up[0] != 0:
	    return 0
	elif nums_up[n-1] != n:
	    return n
	else:
	    for i in range(0, n-1):
		if nums_up[i] + 1 != nums_up[i+1]:
		    return nums_up[i] + 1
		    break

a = Solution()
inp = [0,1,2]
print a.missingNumber(inp)
