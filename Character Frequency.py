
from collections import Counter 
class Solution(object):
    def areOccurrencesEqual(self, s):
        if not s:
            return False
        count = Counter(s)
        val = [val for val in count.values()]
        same = all(x == val[0] for x in val)
        return same

