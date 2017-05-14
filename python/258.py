class Solution(object):

    def addDigits(self, num):

        """

        :type num: int

        :rtype: int

        """
	while len(str(num)) > 1:
	    nums = list(str(num))
	    num = 0
	    for i in range(0, len(nums)):
	        num += int(nums[i])
	return num

a = Solution()
print a.addDigits(1222)
