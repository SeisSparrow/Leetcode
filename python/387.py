import operator

class Solution(object):

    def firstUniqChar(self, s):

        """

        :type s: str

        :rtype: int

        """

        letters = list(s)
        N = len(letters)
        
        if N >= 2: 

	    location = -1
            dic = {}

            for i in range(0, N):
            	dic.update({i: letters[i]})

	    dic_sorted = sorted(dic.items(), key=operator.itemgetter(1))
	    
	    for i in range(0, N):
		if i == 0 and dic_sorted[i][1] != dic_sorted[i+1][1]:
                    if location != -1 and location > dic_sorted[i][0]:
                        location = dic_sorted[i][0]
                    if location == -1:
                        location = dic_sorted[i][0]
		
		if i >= 1 and i <= N-2 and dic_sorted[i][1] != dic_sorted[i+1][1] and dic_sorted[i-1][1] != dic_sorted[i][1]:
		    if location != -1 and location > dic_sorted[i][0]:
                        location = dic_sorted[i][0]
		    if location == -1:
                        location = dic_sorted[i][0]

		if i == N-1 and dic_sorted[i-1][1] != dic_sorted[i][1]:

                    if location != -1 and location > dic_sorted[i][0]:
                        location = dic_sorted[i][0]
                    if location == -1:
                        location = dic_sorted[i][0]
	
	if N == 1:
            location = 0

	if N == 0:
	    location = -1
	    
	return location

a = Solution()
sss = "a"
print a.firstUniqChar(sss)    
        
