class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:

        k -= 1
        def backtrack(k, index):
            if index == 0:
                return 0

            first_half = pow(2, index-1)
            if k < first_half:
                return backtrack(k, index-1)
            else:
                if operations[index-1] == 0:
                    return backtrack(k-first_half, index-1)
                else:
                    return (backtrack(k - first_half, index-1) + 1) % 26

        return chr(backtrack(k,len(operations)) + ord("a"))
        