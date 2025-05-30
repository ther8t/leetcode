class Solution:
    def countAndSay(self, n):
        if n == 1:
            return "1"
        nMinusOne = self.countAndSay(n - 1)
        identifier = 0
        counter = 0
        n = ""
        while identifier < len(nMinusOne):
            if counter < len(nMinusOne) and nMinusOne[identifier] == nMinusOne[counter]:
                counter += 1
            else:
                n += (str(counter - identifier) + str(nMinusOne[identifier]))
                identifier = counter
        return n


if __name__ == '__main__':
    print(Solution().countAndSay(8))
