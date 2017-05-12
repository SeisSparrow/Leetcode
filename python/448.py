class Solution(object):

    def findDisappearedNumbers(self, nums):

        """

        :type nums: List[int]

        :rtype: List[int]

        """
        output = []

        N = len(nums)

        nums_sorted = sorted(nums)        

        if N > 1:

            if nums_sorted[0] > 1:

                for i in range(1,nums_sorted[0]):

                    output.append(i)

            for i in range(0, N-1):

                if nums_sorted[i+1] - nums_sorted[i] > 1:

                    temp = nums_sorted[i] + 1

                    while temp < nums_sorted[i+1]:

                        output.append(temp)

                        temp += 1                        

            if nums_sorted[N-1] < N:

                for i in range(nums_sorted[N-1], N):

                    output.append(i+1)

        return output

a = Solution()
sss = [1]
print a.findDisappearedNumbers(sss)
