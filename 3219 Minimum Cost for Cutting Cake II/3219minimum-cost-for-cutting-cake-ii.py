class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        
        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)
        
        horizontal_pieces = 1
        vertical_pieces = 1
        i, j = 0, 0
        total_cost = 0
        
        # Greedily make the most expensive cuts first
        while i < len(horizontalCut) and j < len(verticalCut):
            if horizontalCut[i] > verticalCut[j]:
                total_cost += horizontalCut[i] * vertical_pieces
                i += 1
                horizontal_pieces += 1
            else:
                total_cost += verticalCut[j] * horizontal_pieces
                j += 1
                vertical_pieces += 1
        
        # Add remaining horizontal cuts (if any)
        while i < len(horizontalCut):
            total_cost += horizontalCut[i] * vertical_pieces
            i += 1
        
        # Add remaining vertical cuts (if any)
        while j < len(verticalCut):
            total_cost += verticalCut[j] * horizontal_pieces
            j += 1
        
        return total_cost