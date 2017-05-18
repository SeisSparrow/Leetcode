class Solution(object):

    def longestPalindrome(self, s):

        """

        :type s: str

        :rtype: int

        """
	s_list = list(s)
	
	N = len(s_list)
	dic = {}
	
	length = N
	
	length_odd = 0

	flag = 0

	for i in range(0, N):
	    if s_list[i] in dic:
		dic[s_list[i]] += 1
	    else:
		dic[s_list[i]] = 1
	
	for a in dic:
	    if dic[a] % 2 != 0:
		length -= 1
		flag = 1	

	return length + flag

a = Solution()
sss = "aa"
print a.longestPalindrome(sss)
