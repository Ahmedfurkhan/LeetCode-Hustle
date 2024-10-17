class Solution:
    def maximumSwap(self, num: int) -> int:
        # Step 1: Convert the integer number into a list of digits as strings
        num_list = list(str(num))  # Example: if num = 2736, then num_list = ['2', '7', '3', '6']

        # Step 2: Create a dictionary to store the last occurrence of each digit in num_list
        last = {int(d): i for i, d in enumerate(num_list)}
        # The 'last' dictionary will store each digit's last index in the list.
        # For example: if num_list = ['2', '7', '3', '6'], then last = {2: 0, 7: 1, 3: 2, 6: 3}
        # This helps to know where each digit appears for possible swaps later on.

        # Step 3: Loop through the digits of num_list to find the first digit that can be swapped
        for i, digit in enumerate(num_list):
            # For the current digit, check if there exists a larger digit (9 down to current digit + 1)
            # that appears later in the number.
            for d in range(9, int(digit), -1):  # Check from 9 down to one more than the current digit
                # If a larger digit (d) exists later in the list (i.e., has a higher index than current digit),
                # we will swap it with the current digit.
                if last.get(d, -1) > i:  # If the last occurrence of d is after the current index i
                    # Step 4: Swap the current digit with the larger digit
                    num_list[i], num_list[last[d]] = num_list[last[d]], num_list[i]
                    # Example: if num_list = ['2', '7', '3', '6'] and the swap happens between 2 and 7,
                    # after the swap, num_list = ['7', '2', '3', '6']

                    # Step 5: Convert the list of digits back into an integer and return the result
                    return int(''.join(num_list))  # Example: ['7', '2', '3', '6'] becomes 7236
        
        # Step 6: If no swap is performed, return the original number
        return num
