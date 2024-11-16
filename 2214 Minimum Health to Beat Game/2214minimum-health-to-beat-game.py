class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        
        # damage.sort()
        sm = sum(damage)
        
        selected = min(max(damage),armor)

        return sm + 1 - selected