class Solution(object):

    def intersection(self, nums1, nums2):

        """

        :type nums1: List[int]

        :type nums2: List[int]

        :rtype: List[int]

        """
	N1 = len(nums1)
	N2 = len(nums2)
	
	nums1_up = sorted(nums1)

	nums2_up = sorted(nums2)
	
	common = []

	m = 0
	n = 0

	for i in range(0, N1):	

	    for j in range(m, N2):
		
		if nums1_up[i] == nums2_up[j]:
		    common.append(nums2_up[j])
		    m = j
		    
		    while m < N2 - 1 and nums2_up[m] == nums2_up[m+1]:
			m += 1

		    m += 1
		    break
	return common

a = Solution()
ss = [1,2,2,2,4,4,83]
tt = [2,5,99999,1,0,0,83]
print a.intersection(ss,tt)		
