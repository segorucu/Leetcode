class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        l = r = 0
        n = len(arr)
        ans = 1
        expectation = None
        while r < n-1:
            if arr[r] == arr[r+1]:
                r = l = r + 1
            elif arr[r] > arr[r+1]:
                if expectation:
                    if expectation == "decreasing":
                        r += 1
                        expectation = "increasing"
                    else:
                        l = r
                        expectation = "increasing"
                        r += 1
                else:
                    r += 1
                    expectation = "increasing"
            elif arr[r] < arr[r+1]:
                if expectation:
                    if expectation == "increasing":
                        r += 1
                        expectation = "decreasing"
                    else:
                        l = r
                        expectation = "decreasing"
                        r += 1
                else:
                    expectation = "decreasing"
                    r += 1
            ans = max(ans,r-l+1)
        return ans