class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        
        def is_possible(val):
            temp_n = n

            for i in quantities:
                if i <= val:
                    temp_n -= 1
                
                else:
                    temp_n -= math.ceil(i / val)
                
                if temp_n < 0:
                    return False
            
            return True


        start = 1
        end = max(quantities)

        res = end

        while start <= end:
            mid = (start + end) // 2
            possible = is_possible(mid)
            
            if possible:
                res = min(res, mid)
                end = mid - 1
            
            else:
                start = mid + 1
        
        return res