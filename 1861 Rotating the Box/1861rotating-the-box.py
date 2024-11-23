class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:

        n = len(box)
        m = len(box[0])

        ans = [n*[""] for _ in range(m)]

        def rotate(arr):
            n = len(arr)
            tmparr = n * ["."]
            stones = 0
            for r in range(n):
                if arr[r] == "#":
                    stones += 1
                elif arr[r] == "*":
                    for i in range(stones):
                        tmparr[r-i-1] = "#"
                    tmparr[r] = "*"
                    stones = 0
            if stones:
                for i in range(stones):
                    tmparr[n-i-1] = "#"
            return tmparr


        for col in range(n):
            arr = rotate(box[col])
            # print(arr)
            for r in range(m):
                ans[r][n-col-1] = arr[r]

        return ans
        