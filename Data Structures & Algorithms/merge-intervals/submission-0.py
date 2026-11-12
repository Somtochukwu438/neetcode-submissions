class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return None
        n = len(intervals)
        intervals.sort(key=lambda x:x[0])
        merge = [intervals[0]]
        for i in range(1, n):
            last = merge[-1]
            curr = intervals[i]

            if last[1] >= curr[0]:
                last[1] = max(last[1], curr[1])
            else:
                merge.append(curr)
        return merge


        