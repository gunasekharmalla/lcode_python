from collections import Counter as cnt
class Solution(object):
    def topKFrequent(self, nums, k):
        count = cnt(nums)
        return [item for item, _ in count.most_common(k)]


