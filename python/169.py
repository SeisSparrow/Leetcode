class Solution(object):

    def majorityElement(self, nums):

        """

        :type nums: List[int]

        :rtype: int

        """
       	N = len(nums)
	
	dic = {}

	for i in range(0, N):
	    if nums[i] in dic:
		dic[nums[i]] += 1
	    else:
		dic[nums[i]] = 1

	count = 0

	for a in dic:
	    if dic[a] > count:
		count = dic[a]
		output = a

	return output

a = Solution()
sss = [1]
print a. majorityElement(sss)
