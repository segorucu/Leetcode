class Solution:
    def countCollisions(self, directions: str) -> int:
        

        ans = 0
        rights = 0
        crash = False
        prev = None
        for i, direc in enumerate(directions):
            if not prev:
                if direc == "R":
                    rights = 1
            elif prev == "L":
                if direc == "R":
                    rights = 1
                elif direc == "L":
                    if crash:
                        ans += 1
                elif direc == "S":
                    pass
            elif prev == "R":
                if direc == "L":
                    ans += rights + 1
                    crash = True
                    rights = 0
                elif direc == "R":
                    rights += 1
                elif direc == "S":
                    ans += rights
                    rights = 0
                    crash = True
            elif prev == "S":
                if direc == "L":
                    crash = True
                    ans += 1
                elif direc == "R":
                    rights  =1
                elif direc == "S":
                    pass

            prev = direc
        return ans







