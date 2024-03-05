class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        
        counter = collections.Counter(arr)
        n = len(arr)
        for k,v in sorted(counter.items()):
            while counter[k] > 0:
                if k > 0:
                    if counter[2*k] > 0:
                        counter[k] -= 1
                        counter[2*k] -= 1
                        n -= 2
                    else:
                        break
                elif k < 0:
                    if k % 2 ==0 and counter[k//2] > 0:
                        counter[k] -= 1
                        counter[k//2] -= 1
                        n -= 2
                    else:
                        break
                elif k == 0:
                    if counter[k] % 2 == 0:
                        counter[k] -= 2
                        n -= 2
                    else:
                        break
        return n == 0