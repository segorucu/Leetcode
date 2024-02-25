class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:


        degreemp = collections.defaultdict(int)
        for i in range(n):
            degreemp[i] = 0
        for a,b in roads:
            degreemp[a] += 1
            degreemp[b] += 1

        degreelist = collections.defaultdict(list)
        for key, val in degreemp.items():
            degreelist[val].append(key)

        arr = n * [0]
        imp = 1
        for key,values in sorted(degreelist.items()):
            for val in values:
                arr[val] = imp
                imp += 1

        ans = 0
        for a,b in roads:
            ans += arr[a]
            ans += arr[b]

        return ans
        