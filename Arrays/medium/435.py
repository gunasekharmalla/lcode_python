class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[1])
        res = []
        count = 0
        last_end = intervals[0][1]
        for start, end in intervals[1:]:
            if last_end <= start:
                last_end = end
                continue
            else:
                count += 1
                res.append([start,end])
        return count


        
