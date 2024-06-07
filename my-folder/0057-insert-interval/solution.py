class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        final_intervals = []

        for [a, b] in intervals:
            if b < newInterval[0]:
                final_intervals.append([a, b])
            elif a > newInterval[1]:
                final_intervals.append(newInterval)
                newInterval = [a, b]
            else:
                newInterval[0] = min(a, newInterval[0])
                newInterval[1] = max(b, newInterval[1])

        final_intervals.append(newInterval)

        return final_intervals
