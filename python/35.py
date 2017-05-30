class Solution(object):

    def searchInsert(self, nums, target):

        """

        :type nums: List[int]

        :type target: int

        :rtype: int

        """
	N = len(nums)

	if target < nums[0]:
	    
	    return 0
	
	elif target > nums[N-1]:
	
	    return N

	else:
		
	    for i in range(0, N):
		
		if nums[i] == target:
		
		    return i
		    break

		if i <= N-2 and nums[i] < target and target < nums[i+1]:
		
		    return i+1
		    break

a = Solution()
num = [1]
tar = 1
print a.searchInsert(num, tar)
