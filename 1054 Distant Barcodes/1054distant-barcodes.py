class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        
        counter = collections.Counter(barcodes)

        freq_arr = []
        for key,val in counter.items():
            freq_arr.append([-val,key])
        heapq.heapify(freq_arr)

        ans = []
        while freq_arr:
            val, key = heapq.heappop(freq_arr)
            val += 1
            ans.append(key)
            if freq_arr and val <= freq_arr[0][0]:
                val2, key2 = heapq.heappop(freq_arr)
                val2 += 1
                ans.append(key2)
                if val2 < 0:
                    heapq.heappush(freq_arr,[val2,key2])
            if val < 0:
                heapq.heappush(freq_arr,[val,key])

        return ans
