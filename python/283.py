class Solution(object):

    def moveZeroes(self, nums):

        """

        :type nums: List[int]

        :rtype: void Do not return anything, modify nums in-place instead.

        """

        N = len(nums)
        i = 0
        zeros = 0
        
        while i + zeros < N:
            if nums[i] != 0:
                i += 1
            else:
                nums.pop(i)
                zeros += 1
                nums.append(0)

#a = Solution()
#sss=[1, 0, 3, 12, 0]
#a.moveZeroes(sss)
#print sss
