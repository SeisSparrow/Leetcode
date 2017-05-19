class Solution(object):

    def readBinaryWatch(self, num):

        """

        :type num: int

        :rtype: List[str]

        """
	alltime = []
	
	for up8 in range(0, 2):
	    for up4 in range(0, 2):
		for up2 in range(0, 2):
		    for up1 in range(0, 2):
			for down32 in range(0, 2):
			    for down16 in range(0, 2):
				for down8 in range(0, 2):
				    for down4 in range(0, 2):
					for down2 in range(0, 2):
					    for down1 in range(0, 2):
						
						if up8+up4+up2+up1+down32+down16+down8+down4+down2+down1==num and up8+up4 < 2 and 32*down32+16*down16+8*down8+4*down4+2*down2+down1<60:
						    if 32*down32+16*down16+8*down8+4*down4+2*down2+down1 < 10:
							temp = ":0"
						    else:
							temp = ":"
						    time=str(8*up8+4*up4+2*up2+up1)+temp+str(32*down32+16*down16+8*down8+4*down4+2*down2+down1)
						    alltime.append(time)
	return alltime
	
a = Solution()
print a.readBinaryWatch(2)
