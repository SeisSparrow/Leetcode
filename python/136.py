class Solution(object):

    def singleNumber(self, nums):

        """

        :type nums: List[int]

        :rtype: int

        """
        N = len(nums)
        nums_sorted = sorted(nums)
        #return nums_sorted
        if N>1:
            for i in range(0,N):
                if nums_sorted[0] != nums_sorted[1]:
                    return nums_sorted[0]
                if nums_sorted[i-1] != nums_sorted[i] and nums_sorted[i] != nums_sorted[i+1]:
                    return nums_sorted[i]
                if nums_sorted[N-2] != nums_sorted[N-1]:
                    return nums_sorted[N-1]
        else:
            return nums[0]   
#a = Solution()
#print a.singleNumber([1,5,4,1,4])
