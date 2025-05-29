class Solution(object):
    def longestPalindrome(self, s):
        def spaceAround(left, right):
            while left >= 0 and right <= len(s)-1 and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1 : right]
        length = ""
        for i in range(len(s)):
            odd = spaceAround(i,i)
            even = spaceAround(i, i+1)
            length = max(length, odd, even, key = len)
        return length

        
Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
