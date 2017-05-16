class Solution(object):

    def findRelativeRanks(self, nums):

        """

        :type nums: List[int]

        :rtype: List[str]

        """
	N = len(nums)
	DICT = {}
	
	output=[]

	for i in range(0, N):
	    DICT[i] = nums[i]	    
	
	if N == 1:
	    return ["Gold Medal"]
	
	elif N == 2:

            DICT_up = sorted(DICT, key=DICT.get)

            DICT[DICT_up[N-1]] = "Gold Medal"
            DICT[DICT_up[N-2]] = "Silver Medal"

            for i in range(0, N):
                output.append(DICT[i])

            return output

	else:
	    DICT_up = sorted(DICT, key=DICT.get)

	    DICT[DICT_up[N-1]] = "Gold Medal"
            DICT[DICT_up[N-2]] = "Silver Medal"
            DICT[DICT_up[N-3]] = "Bronze Medal"

	    for i in range(N-4, -1, -1):
	    	DICT[DICT_up[i]] = str(N-i)

	    for i in range(0, N):
	    	output.append(DICT[i])
	
	    return output

a = Solution()
numbers = [5]
print a.findRelativeRanks(numbers)
