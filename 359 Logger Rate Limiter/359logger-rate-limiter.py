class Logger:

    def __init__(self):
        self.lastseen = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.lastseen:
            self.lastseen[message] = timestamp
            return True
        else:
            if self.lastseen[message] + 10 > timestamp:
                return False
            else:
                self.lastseen[message] = timestamp
                return True
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)