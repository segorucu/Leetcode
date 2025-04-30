class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        n = len(image)

        for irow in range(n):
            row = image[irow]
            l = 0
            r = n-1
            while l < r:
                row[r], row[l] = row[l], row[r]
                row[r] = 1 - row[r]
                row[l] = 1 - row[l]
                l += 1
                r -= 1
            if n % 2:
                row[n//2] = 1 - row[n//2]

        return image