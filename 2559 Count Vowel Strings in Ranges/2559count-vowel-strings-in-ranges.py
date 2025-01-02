class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:

        arr = [0]
        vowels = {'a', 'e', 'i', 'o', 'u'}
        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                arr.append(arr[-1]+1)
            else:
                arr.append(arr[-1])

        ans = []
        for l,r in queries:
            ans.append(arr[r+1]-arr[l])
        return ans
        