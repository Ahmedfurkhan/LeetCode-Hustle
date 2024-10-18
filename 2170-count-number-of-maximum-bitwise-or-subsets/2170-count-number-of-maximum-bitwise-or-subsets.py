class Solution:
    def backtrack(self, nums, index, currentOR, maxOR, count):
        # Base case: If currentOR equals maxOR, increment the count
        if currentOR == maxOR:
            count[0] += 1

        # Early termination: If currentOR exceeds maxOR, prune the branch
        if currentOR > maxOR:
            return

        # Explore further subsets by including each number in the remaining array
        for i in range(index, len(nums)):
            self.backtrack(nums, i + 1, currentOR | nums[i], maxOR, count)

    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # Compute the maximum OR by performing OR operations on all numbers
        maxOR = 0
        for num in nums:
            maxOR |= num

        # Initialize a count to track the number of subsets with maximum OR
        count = [0]

        # Perform backtracking to count the subsets with maximum OR
        self.backtrack(nums, 0, 0, maxOR, count)

        # Return the count of subsets with maximum OR
        return count[0]