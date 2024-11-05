class Solution:
    def minChanges(self, s: str) -> int:
        # Initialize a counter to keep track of required changes
        count = 0
        # Initialize index pointer
        i = 0
        
        # Loop through the string, but only check every second character
        # (so `i` increments by 2 each time)
        while i < len(s) - 1:
            # Check if the current character is different from the next one
            # If they are different, it implies an alternating pattern, so we need to make a change
            if s[i] != s[i + 1]:
                count += 1  # Increment count for each required change
            
            # Move to the next pair (skip one character forward)
            i += 2
        
        # Return the total count of changes needed to ensure alternating pattern
        return count
