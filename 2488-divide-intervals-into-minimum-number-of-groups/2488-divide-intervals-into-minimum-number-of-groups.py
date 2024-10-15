class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        min_heap = []
        intervals_sorted = sorted(intervals, key=lambda x:x[0])

        for start, end in intervals_sorted:
            if min_heap and min_heap[0] < start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, end)
        
        return len(min_heap)