class Solution(object):

    def detectCapitalUse(self, word):

        """

        :type word: str

        :rtype: bool

        """
	words = list(word)
	N = len(words)
	output = True
	if N == 1:
	    pass
	elif N == 2:
	    if words[0].islower() and words[1].isupper():
	    	output = False
	else:
	    if words[0].isupper() and words[1].isupper():
		for i in range(2, N):
		    if words[i].islower():
	    	    	output = False
		    	break
	    if words[0].isupper() and words[1].islower():
            	for i in range(2, N):
                    if words[i].isupper():
                    	output = False
		    	break	
	    if words[0].islower():
	    	for i in range(1, N):
		    if words[i].isupper():
		    	output = False
		    	break
	return output

a = Solution()
sss = "oD"
print a.detectCapitalUse(sss)
 
