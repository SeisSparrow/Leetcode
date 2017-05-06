class Solution(object):

    def reverseString(self, s):

        """

        :type s: str

        :rtype: str

        """
        letters = list(s)
        letters_reverse = []
        for i in range (0, len(letters)):
            letters_reverse.append(letters[len(letters)-1-i])
        s_reverse = ''.join(letters_reverse)    
        return s_reverse

a = Solution()
print a.reverseString("shit")
