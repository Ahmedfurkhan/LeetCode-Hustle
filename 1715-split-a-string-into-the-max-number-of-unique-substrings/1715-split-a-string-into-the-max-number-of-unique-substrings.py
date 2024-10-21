class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        """
        This function calculates the maximum number of unique substrings that the given string s
        can be split into.

        :type s: str
        :rtype: int
        """

        # Initialize a set to store the unique substrings
        unique_substrings = set()

        # Initialize a variable to store the maximum number of unique substrings
        max_unique = 0

        # Define a recursive function to perform backtracking
        def backtrack(start, unique_substrings, unique_count):
            nonlocal max_unique

            # If the current substring is already in the set, return
            if start == len(s):
                max_unique = max(max_unique, unique_count)
                return

            # Iterate over the substrings starting from the current position
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]

                # If the current substring is not in the set, add it and continue backtracking
                if substring not in unique_substrings:
                    unique_substrings.add(substring)
                    backtrack(end, unique_substrings, unique_count + 1)
                    unique_substrings.remove(substring)

        # Perform backtracking
        backtrack(0, unique_substrings, 0)

        # Return the maximum number of unique substrings
        return max_unique