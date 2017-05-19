class Solution(object):

    def romanToInt(self, s):

        """

        :type s: str

        :rtype: int

        """
	dic = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

	nums = list(s)

	N = len(nums)
		
	output = 0

	i = 0

	while i < N - 1:
	    if dic[nums[i]] >= dic[nums[i+1]]:
		output += dic[nums[i]]
		i += 1
	    else:
		output += dic[nums[i+1]] - dic[nums[i]]
		i += 2
	
	if dic[nums[N-1]] <= dic[nums[N-2]]:
	    output += dic[nums[N-1]]

	return output

a = Solution()
print a.romanToInt("VIII")
