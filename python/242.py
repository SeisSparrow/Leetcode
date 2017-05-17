class Solution(object):

    def isAnagram(self, s, t):

        """

        :type s: str

        :type t: str

        :rtype: bool

        """
	s_list = list(s)
	t_list = list(t)

       	Ns = len(s_list)
	Nt = len(t_list)

	if Ns != Nt:
	    return False
	if Ns == Nt and Ns == 0:
	    return True
	else:
	    dic_s = {}
	    dic_t = {}
	    
	    for i in range(0, Ns):
		if s_list[i] in dic_s:
		    dic_s[s_list[i]] += 1
		else:
		    dic_s[s_list[i]] = 1

            for i in range(0, Nt):
                if t_list[i] in dic_t:
                    dic_t[t_list[i]] += 1
                else:
                    dic_t[t_list[i]] = 1


	    if dic_s == dic_t:
		return True
	    else:
		return False

a = Solution()
sss = ""
ttt = ""
print a.isAnagram(sss,ttt)
	 
