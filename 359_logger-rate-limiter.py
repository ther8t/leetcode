from collections import deque

class Logger:
    logKeeper = {}

    def __init__(self):
        pass

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        previousTime = -10

        if message in self.logKeeper.keys():
            previousTime = self.logKeeper[message]

        if timestamp - previousTime >= 10:
            self.logKeeper[message] = timestamp
        return True if timestamp - previousTime >= 10 else False

# Your Logger object will be instantiated and called as such:
obj = Logger()
print(obj.shouldPrintMessage(100, "bug"))
print(obj.shouldPrintMessage(111, "bug"))

q = deque()
q.append(1)
q.append(2)
q.append(3)
q.append(4)

for i in q:
    print(i)