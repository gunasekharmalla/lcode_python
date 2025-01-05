class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        start = strs[0] 
        for string in strs[1:]:
            while not string.startswith(start):
                start = start[:-1] 
                if not start:
                    return ""
        return start 