class Solution(object):

    def findComplement(self, num):

        """

        :type num: int

        :rtype: int

        """

        num_in_bin = bin(num)
	num_in_bin_split = list(num_in_bin)
	N = len(num_in_bin_split)	

	for i in range(0, N):
		if num_in_bin_split[i] == '1':
		    num_in_bin_split[i] = '0'
		else:
		    num_in_bin_split[i] = '1'

	num_in_bin_string = ''.join(num_in_bin_split[2:len(num_in_bin_split)])
	return int(num_in_bin_string,2)

a = Solution()
n = 5
print a.findComplement(n)
