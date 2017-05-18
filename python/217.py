class Solution(object):

    def containsDuplicate(self, nums):

        """

        :type nums: List[int]

        :rtype: bool

        """

        N = len(nums)

	dic = {}

	output = False

	for i in range(0, N):

	    if nums[i] in dic:
		output = True
	    else:
		dic[nums[i]] = 1

	return output
