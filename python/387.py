class Solution(object):

    def firstUniqChar(self, s):

        """

        :type s: str

        :rtype: int

        """

        letters = list(s)
        N = len(letters)
        dic = {}
        for i in range(0, N):
            dic.update({i: letters[i]})
        location = -1
        letters_sorted = sorted(letters)
        
        if N >= 2: 
            for i in range(0, N):
                if i == 0:
                    if letters_sorted[i] != letters_sorted[i+1]:
                        location = dic.keys()[dic.values().index(letters_sorted[i])]
                elif i > 0 and i <= N-2:
                    if letters_sorted[i-1] != letters_sorted[i] and letters_sorted[i] != letters_sorted[i+1]:
		        if dic.keys()[dic.values().index(letters_sorted[i])] < location:
			    location = dic.keys()[dic.values().index(letters_sorted[i])]
                else:
                    if letters_sorted[i-1] != letters_sorted[i]:
                        if dic.keys()[dic.values().index(letters_sorted[i])] < location:
                            location = dic.keys()[dic.values().index(letters_sorted[i])]
	else:
            return 0
	    
	return location

a = Solution()
sss = "loveleetcode"
print a.firstUniqChar(sss)    
        
