class Solution(object):

    def reverseWords(self, s):

        """

        :type s: str

        :rtype: str

        """
	words_split = s.split(' ')
	s_reverse = []
	
	for i in range(0, len(words_split)):
	    char_split = []
	    char_split_reverse = []
	    char_split = list(words_split[i])
	    for j in range(0, len(char_split)):
		char_split_reverse.append(char_split[len(char_split)-1-j])
	    words_split_reverse = ''.join(char_split_reverse)
	    s_reverse.append(words_split_reverse)
	return ' '.join(s_reverse)

#a = Solution()
#sss = "Let's take Leetcode contest"
#print a.reverseWords(sss)
