class Solution(object):

    def checkRecord(self, s):

        """

        :type s: str

        :rtype: bool

        """
	ss = list(s)
	
	N = len(ss)

	NA = 0

	NL = 0
	
	output = True

	for i in range(0, N):
	    if ss[i] == "A":
		NA += 1
	    if i > 0 and i < N-1 and ss[i-1] == "L" and ss[i] == "L" and ss[i+1] == "L":
		output = False

	if NA > 1:
	    output = False
	return output

a = Solution()
inp = "PPALLPLL"
print a.checkRecord(inp)
