from typing import List

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        """
        This function calculates the maximum possible bitwise OR of a subset of the input array
        and returns the number of different non-empty subsets that achieve this maximum.

        Parameters:
        nums (List[int]): The input array of integers

        Returns:
        int: The number of different non-empty subsets with the maximum bitwise OR
        """

        # Get the length of the input array
        n = len(nums)

        # Initialize the maximum bitwise OR and the count of subsets that achieve it
        max_or = 0
        max_count = 0

        # We will iterate over all possible subsets of the input array
        # A subset is represented by a bitmask where each bit corresponds to an element in the array
        # If the bit is 1, the element is included in the subset; if the bit is 0, the element is not included
        for bitmask in range(1, 2 ** n):
            # Initialize the bitwise OR of the current subset
            curr_or = 0

            # Iterate over the elements of the array
            for i in range(n):
                # Check if the current element is included in the subset
                if bitmask & (1 << i):  # (1 << i) is a bitmask with only the ith bit set
                    # If the element is included, update the bitwise OR of the subset
                    curr_or |= nums[i]

            # If the bitwise OR of the current subset is greater than the maximum seen so far
            if curr_or > max_or:
                # Update the maximum bitwise OR and reset the count of subsets that achieve it
                max_or = curr_or
                max_count = 1
            # If the bitwise OR of the current subset is equal to the maximum seen so far
            elif curr_or == max_or:
                # Increment the count of subsets that achieve the maximum bitwise OR
                max_count += 1

        # Return the count of subsets that achieve the maximum bitwise OR
        return max_count