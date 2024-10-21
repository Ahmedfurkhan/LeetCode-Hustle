class Solution:
    def minOperations(self, nums: List[int]) -> int:
        """
        This function calculates the minimum number of operations required to make a given list of integers
        into a sorted list in ascending order. An operation is defined as replacing an element with its divisor.

        :type nums: List[int]
        :rtype: int
        """

        # Initialize the answer variable to store the minimum number of operations
        ans = 0

        # Iterate over the list of numbers in reverse order
        for i in range(len(nums) - 1, 0, -1):
            # If the current number is less than the previous number, it means the list is not sorted
            if nums[i] < nums[i - 1]:
                # Find the smallest divisor of the previous number that makes it not greater than the current number
                # and replace the previous number with this divisor
                nums[i - 1] = self.findNum(nums[i], nums[i - 1])

                # If no such divisor is found, return -1 as it is not possible to make the list sorted
                if nums[i - 1] == -1: return -1

                # Increment the answer by 1 as one operation is performed
                ans += 1

        # Return the minimum number of operations required
        return ans

    def findNum(self, n1, n2):
        """
        This function finds the smallest divisor of n2 that makes it not greater than n1.

        :type n1: int
        :type n2: int
        :rtype: int
        """

        # Iterate over the numbers from 2 to n1 (inclusive)
        for i in range(2, n1 + 1):
            # If n2 is divisible by i, return i as the smallest divisor
            if n2 % i == 0: return i

        # If no divisor is found, return -1
        return -1