class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        # go through all binary places, and count num 1's
        i, ans = 0, 0
        maxval = max(candidates)
        while (1 << i) <= maxval:
            ans = max(ans, sum([1 for x in candidates if (1 << i) & x]))
            i += 1
        return ans