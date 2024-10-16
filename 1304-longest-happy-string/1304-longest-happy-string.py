import heapq  # Importing the heapq module to use priority queues

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pq = []  # Priority queue to store characters along with their counts in max-heap style (negative count to make it behave like a max-heap)

        # Add 'a', 'b', and 'c' to the priority queue with their respective counts (negative for max-heap)
        if a > 0:
            heapq.heappush(pq, (-a, 'a'))  # Push 'a' with negative count
        if b > 0:
            heapq.heappush(pq, (-b, 'b'))  # Push 'b' with negative count
        if c > 0:
            heapq.heappush(pq, (-c, 'c'))  # Push 'c' with negative count

        result = []  # List to store the final result (characters of the string)

        # Main loop: Continue until we can't add any more valid characters
        while pq:
            # Pop the character with the highest remaining count (most frequent)
            count1, char1 = heapq.heappop(pq)

            # If the last two characters in the result are the same as the current character (char1), 
            # we need to handle it carefully to avoid adding three consecutive identical characters.
            if len(result) >= 2 and result[-1] == char1 and result[-2] == char1:
                # If the priority queue is empty, we can't add any other characters to avoid three in a row
                if not pq:
                    break  # Break out of the loop, since no valid moves are possible

                # Pop the next most frequent character (this will be used as a temporary filler)
                count2, char2 = heapq.heappop(pq)

                # Add this second character (char2) to the result
                result.append(char2)

                # Decrease its count (since we used it once)
                count2 += 1  # Increment because we store the count as negative (to restore to max-heap)

                # If count2 is still negative (meaning more of this character can still be used),
                # push it back into the priority queue
                if count2 < 0:
                    heapq.heappush(pq, (count2, char2))

                # After adding the second character (char2), push the first character (char1) back into the queue
                # because we will use it later once it's safe to do so.
                heapq.heappush(pq, (count1, char1))

            else:
                # If adding char1 doesn't result in three consecutive identical characters,
                # simply append it to the result
                result.append(char1)

                # Decrease the count of char1 since we used it once
                count1 += 1  # Increment because we store count as negative (to restore to max-heap)

                # If count1 is still negative (meaning more of this character can still be used),
                # push it back into the priority queue
                if count1 < 0:
                    heapq.heappush(pq, (count1, char1))

        # Join the list of characters into a final string and return it
        return ''.join(result)
