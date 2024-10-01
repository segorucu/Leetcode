class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        
        
        n = len(arr)
        counter = collections.defaultdict(int)
        for i in range(n):
            val = arr[i] % k
            if counter[k-val] > 0:
                counter[k-val] -= 1
            else:
                counter[val] += 1

        if counter[0] % 2 != 0:
            return False
        del counter[0]
        keylist = counter.keys()
        for key in list(keylist):
            if counter[key] == 0:
                del counter[key]
        
        return len(counter.keys()) == 0