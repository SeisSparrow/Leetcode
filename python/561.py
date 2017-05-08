class Solution(object):

    def arrayPairSum(self, nums):

        """

        :type nums: List[int]

        :rtype: int

        """
        nn = len(nums)
        n = nn / 2
        nums_up = sorted(nums)
        sum = 0
        for i in range(0, n):
            sum += nums_up[2*i]

        return sum
       
a = Solution()
print a.arrayPairSum([1,3,2,4]) 
