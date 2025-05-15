class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        
        prev = -1
        ans = []
        for word, group in zip(words, groups):
            if group != prev:
                ans.append(word)
                prev = group
        return ans