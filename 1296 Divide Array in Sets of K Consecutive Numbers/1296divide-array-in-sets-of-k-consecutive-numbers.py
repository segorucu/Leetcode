class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:

        n = len(nums)
        if n % k != 0:
            return False
        m = n // k

        counter = collections.Counter(nums)

        for _ in range(m):
            curr = min(counter.keys())
            counter[curr] -= 1
            if counter[curr] == 0:
                del counter[curr]
            for i in range(1,k):
                curr += 1
                if counter[curr] == 0:
                    return False
                counter[curr] -= 1
                if counter[curr] == 0:
                    del counter[curr]

        return True

        
        