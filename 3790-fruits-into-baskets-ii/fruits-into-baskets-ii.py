class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        

        ans = 0
        for i, f in enumerate(fruits):
            # print(baskets)
            for j, b in enumerate(baskets):
                if f <= b:
                    baskets[j] = 0
                    break
            else:
                ans += 1

        return ans