class Solution(object):

    def findWords(self, words):

        """

        :type words: List[str]

        :rtype: List[str]

        """
	N = len(words)
	row1 = ['q','w','e','r','t','y','u','i','o','p','Q','W','E','R','T','Y','U','I','O','P']
	row2 = ['a','s','d','f','g','h','j','k','l','A','S','D','F','G','H','J','K','L']
	row3 = ['z','x','c','v','b','n','m','Z','X','C','V','B','N','M']
	output = []	

	for i in range(0, N):
	    temp = list(words[i])
	    flag1 = 1
	    for letter in temp:
		if letter in row1:
		    flag1 *= 1
		else:
		    flag1 *= 0

            flag2 = 1
            for letter in temp:
                if letter in row2:
                    flag2 *= 1
                else:
                    flag2 *= 0

            flag3 = 1
            for letter in temp:
                if letter in row3:
                    flag3 *= 1
                else:
                    flag3 *= 0
	    if flag1 == 1 or flag2 == 1 or flag3 == 1:
	        output.append(''.join(temp))
	return output

a = Solution()
sss = ["hello", "Alaska", "Dad", "Peace"]
print a.findWords(sss)
