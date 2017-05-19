class Solution(object):

    def intersect(self, nums1, nums2):

        """

        :type nums1: List[int]

        :type nums2: List[int]

        :rtype: List[int]

        """
	N1 = len(nums1)
	N2 = len(nums2)
	dic1 = {}
	dic2 = {}
	output = []

	for i in range(0, N1):
	    if nums1[i] in dic1:
		dic1[nums1[i]] += 1
	    else:
		dic1[nums1[i]] = 1

        for j in range(0, N2):
            if nums2[j] in dic2:
                dic2[nums2[j]] += 1
            else:
                dic2[nums2[j]] = 1	

	for a in dic1:
	    if a in dic2:
		for k in range(0, dic1[a] if dic1[a] <= dic2[a] else dic2[a]):
		    output.append(a)
	return output

a = Solution()
num1 = [1, 2, 2, 1]
num2 = [2, 2]
print a.intersect(num1, num2)
