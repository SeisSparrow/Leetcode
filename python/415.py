class Solution(object):

    def addStrings(self, num1, num2):

        """

        :type num1: str

        :type num2: str

        :rtype: str

        """
	n1 = list(num1)
	n2 = list(num2)

	N1 = len(n1)
	N2 = len(n2)
	
	output = 0

	for i in range(0, N1):
	    output += int(n1[i]) * pow(10, N1 - i - 1)

        for j in range(0, N2):
            output += int(n2[j]) * pow(10, N2 - j - 1)	

	return str(output)

a = Solution()
in1 = "10"
in2 = "333"
print a.addStrings(in1, in2)
        
