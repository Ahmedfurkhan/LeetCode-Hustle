class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        # Initialize the answer as infinity since we are looking for a minimum length.
        ans = inf
        # Dictionary `d` will store subarray OR values as keys and their maximum left endpoint as values.
        d = dict()
        
        # Iterate through each element in nums, where `i` is the index and `x` is the element at that index.
        for i, x in enumerate(nums):
            # Update dictionary `d` to include new OR results by OR'ing each existing key with the current number `x`.
            # The left endpoint will be the same as the original left endpoint for that OR value.
            # This step accumulates possible OR values for subarrays ending at index `i`.
            d = {or_ | x: left for or_, left in d.items()}
            
            # Add the subarray that contains only the current element `x`, with the left endpoint as `i`.
            d[x] = i
            
            # Check each OR value in dictionary `d`:
            # If the OR value is greater than or equal to `k`, we check if this subarray's length is the shortest so far.
            for or_, left in d.items():
                if or_ >= k:
                    # Calculate the length of this subarray and update `ans` if it's the shortest found.
                    ans = min(ans, i - left + 1)
        
        # Return the minimum length if we found a valid subarray, otherwise return -1.
        return ans if ans < inf else -1
