class Solution(object):

    def hammingDistance(self, x, y):

        """

        :type x: int

        :type y: int

        :rtype: int

        """
        z = x ^ y
        z_list = list(bin(z))
        N = len(z_list)
        num = 0
        for i in range(2,N):
            if int(z_list[i]) != 0:
		num += 1
        return num

#a=Solution()
#print a.hammingDistance(9,4)
#
#
