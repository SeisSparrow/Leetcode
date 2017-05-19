class Solution(object):

    def romanToInt(self, s):

        """

        :type s: str

        :rtype: int

        """
	dic = {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}

	nums = list(str(s))

	N = len(nums)
		
	output = []

	for i in range(0, N):

	    nums[i] = int(nums[i])
	
	for i in range(0, N):

	    if nums[i] >= 1 and nums[i] <= 3:
		for j in range(0, nums[i]):
		    output.append(dic[pow(10, N-i-1)])

	    if nums[i] >= 4 and nums[i] <= 8:
		for j in range(nums[i], 5):
		    output.append(dic[pow(10, N-i-1)])
		
		output.append(dic[5 * pow(10, N-i-1)])	
		
		for j in range(0, nums[i] - 5):

		    output.append(dic[pow(10, N-i-1)])
	    
	    if nums[i] == 9:
		output.append(dic[pow(10, N-i-1)])
		output.append(dic[pow(10, N-i)])

	return ''.join(output)

a = Solution()
print a.romanToInt(99)
