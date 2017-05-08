class Solution(object):

    def titleToNumber(self, s):

        """

        :type s: str

        :rtype: int

        """

        letters = list(s)
        N = len(letters)
	num = 0
        for i in range(0, N):
            num += (ord(letters[i])-64)*pow(26,N-1-i)
        return num

#ss = Solution()
#print ss.titleToNumber("AAB")

