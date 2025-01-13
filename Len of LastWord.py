
class Solution(object):
    def lengthOfLastWord(self, s):
        s1 = s.strip()
        s2 = s1.split(' ')
        return len(s2[-1])
      
