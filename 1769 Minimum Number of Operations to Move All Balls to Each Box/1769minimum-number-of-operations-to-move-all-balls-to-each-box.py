class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        n = len(boxes)
        ans = n * [0]
        for i in range(n):
            for j in range(n):
                if boxes[j] == "1":
                    ans[i] += abs(j-i)

        return ans
