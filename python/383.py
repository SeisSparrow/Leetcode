class Solution(object):

    def canConstruct(self, ransomNote, magazine):

        """

        :type ransomNote: str

        :type magazine: str

        :rtype: bool

        """
	N1 = len(ransomNote)
	N2 = len(magazine)

	ran_up = sorted(ransomNote)
	mag_up = sorted(magazine)

	output = True

	flag = 0
	
	if N1 > 0 and N2 == 0:
	    output = False

	if N1 > 0 and N2 > 0:	
		
	    for i in range(0, N1):
	    	for j in range(flag, N2):
		
		    if ran_up[i] == mag_up[j]:
		    	flag = j + 1
		    	break
	    
	    	if j == N2 - 1 and ran_up[i] == mag_up[j] and i < N1 - 1:
	            output = False
	    	    break
	
	    	if j == N2 - 1 and ran_up[i] != mag_up[j]:
	 	    output = False
		    break
	return output

a = Solution()
ss = "a"
tt = ""
print a.canConstruct(ss, tt)
