class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        inserted = False
        for [s, e] in intervals:
            if e < newInterval[0]:
                res.append([s, e])
            elif s > newInterval[1]:
                if not inserted:
                    res.append(newInterval)
                    inserted = True
                res.append([s, e])
            else:
                newInterval[0] = min(s, newInterval[0]) 
                newInterval[1] = max(e, newInterval[1]) 
        
        if not inserted:
            res.append(newInterval)

        return res
