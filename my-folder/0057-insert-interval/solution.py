class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        merged = []
        for idx, interval in enumerate(intervals):
            if newInterval[0] > interval[1]:
                merged.append(interval)
            elif newInterval[1] < interval[0]:
                interval, newInterval = newInterval, interval
                merged.append(interval)
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        merged.append(newInterval)
        
        return merged
