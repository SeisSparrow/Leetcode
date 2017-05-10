class Solution(object):

    def nextGreaterElement(self, findNums, nums):

        """

        :type findNums: List[int]

        :type nums: List[int]

        :rtype: List[int]

        """
	N1 = len(findNums)
	N2 = len(nums)
	output = []
	for a in findNums:
	    flag = -1
	    
	    for j in range(0, N2):
		if nums[j] == a:
		    break
	    

	    if j == N2-1:
		output.append(-1)
	    else:
	        for k in range(j+1, N2):
		    if nums[k] > a:
		        output.append(nums[k])
		        break

	        if nums[k] <= a:
		    output.append(-1)
	return output

a = Solution()
num1 = [2,4]
num2 = [1,2,3,4]
print a.nextGreaterElement(num1, num2)


