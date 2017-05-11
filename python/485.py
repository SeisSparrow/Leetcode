class Solution(object):

    def findMaxConsecutiveOnes(self, nums):

        """

        :type nums: List[int]

        :rtype: int

        """
	count = 0
	N = len(nums)
	counts = [0]
	for i in range(0, N):
	    if nums[i] == 0:
		counts.append(i+1)
	counts.append(N+1)
	for j in range(1, len(counts)):
	    if counts[j] - counts[j-1] -1 > count:
		count = counts[j] - counts[j-1] - 1
	return count

a = Solution()
sss=[1,1,0,1,1,0,1,1,1,1,1,0,1]
print a.findMaxConsecutiveOnes(sss)
