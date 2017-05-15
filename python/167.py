class Solution(object):

    def twoSum(self, numbers, target):

        """

        :type numbers: List[int]

        :type target: int

        :rtype: List[int]

        """
	N = len(numbers)
	i = 0
	while 1:
	    for j in range(i+1, N):
		if numbers[i] + numbers[j] == target:
		    return [i+1, j+1]
		    break
	    	    break
	    i += 1
	    while numbers[i+1] == numbers[i] and numbers[i] + numbers[i+1] < target:
		i += 1
	    

a = Solution()
nums = [5,25,75]
print a.twoSum(nums, 100)
