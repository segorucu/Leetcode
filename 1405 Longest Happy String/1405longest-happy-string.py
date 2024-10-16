from heapq import heapify, heappop, heappush
class Solution:


    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        heap = []
        if a > 0:
            heappush(heap,(-a,"a"))
        if b > 0:
            heappush(heap,(-b,"b"))
        if c > 0:
            heappush(heap,(-c,"c"))
            
        ans = ""
        while heap:
            count, char = heappop(heap)
            if len(ans) >= 2 and ans[-2:] == 2*char:
                if not heap:
                    return ans
                count2, char2 = heappop(heap)
                count2 += 1
                ans += char2
                if count2 < 0:
                    heappush(heap,(count2,char2))
                heappush(heap,(count,char))
            else:
                count += 1
                ans += char
                if count < 0:
                    heappush(heap,(count,char))

        return ans



            
            