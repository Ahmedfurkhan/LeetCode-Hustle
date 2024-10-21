class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        """
        This function calculates the total number of substrings in a given string s
        that contain exactly k occurrences of a character.

        :type s: str
        :type k: int
        :rtype: int
        """

        # Initialize the answer variable to store the total number of substrings
        ans = 0

        # Initialize a pointer for the left end of the sliding window
        l = 0

        # Initialize a dictionary to store the frequency of characters in the current window
        d = {}

        # Iterate over each character in the string
        for c in s:
            # Increment the frequency of the current character in the window
            d[c] = d.get(c, 0) + 1

            # If the frequency of the current character is equal to k
            while d[c] == k:
                # Decrement the frequency of the character at the left end of the window
                d[s[l]] -= 1

                # Move the left end of the window one position to the right
                l += 1

            # Add the current window size to the answer
            # This is because the current window size represents the number of substrings ending at the current position
            # that contain exactly k occurrences of the previous character
            ans += l

        # Return the total number of substrings that contain exactly k occurrences of a character
        return ans