class Solution(object):
    def strStr(self, haystack, needle):
        if not haystack and not needle:
            return -1 
        if needle not in haystack:
            return -1 
        if needle in haystack:
            return haystack.index(needle)