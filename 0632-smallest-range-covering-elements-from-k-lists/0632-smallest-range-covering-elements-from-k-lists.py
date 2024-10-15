class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # Initializing Minimum Heap to track the elments in Klist which is sorted !!
        min_heap = []
# Tracking the current largest element in the window or finding the maximum value in a set of numbers.It's used primarily in algorithms that need to identify the largest element in a collection.
        current_max = float('-inf')
# Initializing the heap with first element fro the list 
        for i in range(len(nums)):
            heapq.heappush(min_heap,(nums[i][0], i,0)) # value, list_index, element_index
            current_max = max(current_max, nums[i][0]) # Update the max value
# Initialize the result range to a very large one from the constraints 
        result_range = [-10**5, 10**5]

        while min_heap:
            current_min, list_idx, elem_idx = heapq.heappop(min_heap) # pop the smallest element from the heap

            #check if the current range [current_min, current_max] is smaller
            if current_max - current_min < result_range[1] - result_range[0]:
                result_range = [current_min, current_max]

            # If we have reached the end of one lists, break the loop
            if elem_idx + 1 == len(nums[list_idx]):
                break
            
            #Otherwise , push the next element from the same list into the heap
            next_elem =  nums[list_idx][elem_idx + 1]
            heapq.heappush(min_heap, (next_elem, list_idx, elem_idx + 1))

            # Update the max value
            current_max = max(current_max, next_elem)

        return result_range