class Solution(object):

    def toHex(self, num):

        """

        :type num: int

        :rtype: str

        """	
	output = []
	dic = {0:"0", 1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9", 10:"a", 11:"b", 12:"c", 13:"d", 14:"e", 15:"f"}
	dic2 = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "a":10, "b":11, "c":12, "d":13, "e":14, "f":15}

	if num == 0:
	    return str(0)
	elif num > 0:
	    while num >= 16:
		output.insert(0, dic[num % 16])
		num /= 16
	    output.insert(0, dic[num])
	    return ''.join(output)
	else:
	    num_abs = abs(num)
            while num_abs >= 16:
                output.insert(0, dic[num_abs % 16])
                num_abs /= 16
            output.insert(0, dic[num_abs])
	
	    while len(output) < 8:
		output.insert(0, '0')
		
	    for i in range(0, 8):
		output[i] = dic[15 - dic2[output[i]]]

	    jinwei = 0

	    if output[7] == "f":
		jinwei = 1
		output[7] = "0"
	    else:
		jinwei = 0
		output[7] = dic[dic2[output[7]] + 1]

	    for i in range(6, -1, -1):
		if jinwei == 1:
		    if output[i] == "f":
			output[i] = "0"
			jinwei = 1
		    else:
			output[i] = dic[dic2[output[i]] + 1]
			jinwei = 0
	
            return ''.join(output)
		
a = Solution()
print a.toHex(-100000)
