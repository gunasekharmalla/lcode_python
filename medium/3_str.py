class Solution(object):
    def lengthOfLongestSubstring(self, s):
        s1 = set()
        j = max_len = 0
        for i in range(len(s)):
            while s[i] in s1:
                s1.remove(s[j])
                j+=1
            s1.add(s[i])
            max_len = max(max_len, i - j +1)
        return max_len
        
