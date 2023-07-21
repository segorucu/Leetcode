from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        counts = Counter(nums)
        print(counts)

        pair = []
        for val, freq in counts.items():
            heappush(pair,(freq,val))
            if len(pair) > k:
                heappop(pair) 

        return [val[1] for val in pair]


