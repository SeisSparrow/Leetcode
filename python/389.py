class Solution(object):

    def findTheDifference(self, s, t):

        """

        :type s: str

        :type t: str

        :rtype: str

        """
        s_sorted = sorted(s)

        Ns = len(s)

        t_sorted = sorted(t)

        if Ns == 0:

            return t

        else:

            for i in range(0, Ns):

                if s_sorted[i] != t_sorted[i]:

                    return t_sorted[i]

                    break

            if i == Ns-1 and s_sorted[i] == t_sorted[i]:

                return t_sorted[Ns]


a = Solution()
ss = "abcd"
tt = "abcde"
print a.findTheDifference(ss, tt)
