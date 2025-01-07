from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        if ransomNote == magazine:
            return True 
        mag = Counter(magazine)
        ran = Counter(ransomNote)
        for char, count in ran.items():
            if mag[char] < count:
                return False 
        return True

