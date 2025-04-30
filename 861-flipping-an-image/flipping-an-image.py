class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        n = len(image)

        for irow in range(n):
            row = image[irow]
            l = 0
            r = n-1
            while l < r:
                row[r], row[l] = row[l], row[r]
                l += 1
                r -= 1

        for r in range(n):
            for c in range(n):
                image[r][c] = 1 - image[r][c]

        return image