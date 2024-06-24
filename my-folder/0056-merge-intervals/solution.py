class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        prev = [-1, -1]
        merged = []
        intervals = sorted(intervals, key = lambda interval: interval[0])
        for interval in intervals:
            if interval[0] > prev[1]:
                merged.append(interval)
            elif interval[1] > prev[1]:
                merged[-1][1] = interval[1]
            prev = merged[-1]
        
        return merged
        
