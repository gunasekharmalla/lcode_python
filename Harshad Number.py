
class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        val = x;sm=0
        while(x!=0):
            rm = x % 10
            sm += rm
            x /= 10 
        if val % sm == 0:
            return sm
        return -1
            
        
