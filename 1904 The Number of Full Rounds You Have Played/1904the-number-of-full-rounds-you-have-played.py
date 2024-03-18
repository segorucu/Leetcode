class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:

        starthour = int(loginTime[0:2])
        startmins = int(loginTime[3:5])
        endhour = int(logoutTime[0:2])
        endmins = int(logoutTime[3:5])
        overnight = False
        if starthour * 60 + startmins > endhour * 60 + endmins:
            overnight = True

        startmins = math.ceil(startmins/15) * 15
        endmins = (endmins // 15) * 15
        finish = endhour * 60 + endmins
        start = starthour * 60 + startmins

        if overnight:
            return max(0,(24*60-start+finish) // 15)
        else:
            return max(0,(finish-start)) // 15



        return 0
        