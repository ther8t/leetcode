class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sLeft = 0
        sRight = len(s) - 1
        pLeft = 0
        pRight = len(p) - 1

        def matchAndMoveRight():
            nonlocal sLeft
            nonlocal sRight
            nonlocal pLeft
            nonlocal pRight

            while sLeft < len(s) and pLeft < len(p) and p[pLeft] != "*":
                if s[sLeft] == p[pLeft] or p[pLeft] == "?":
                    sLeft += 1
                    pLeft += 1
                else:
                    return False
            return True

        def matchAndMoveLeft():
            nonlocal sLeft
            nonlocal sRight
            nonlocal pLeft
            nonlocal pRight

            while sRight >= 0 and pRight >= 0 and p[pRight] != "*":
                if s[sRight] == p[pRight] or p[pRight] == "?":
                    sRight -= 1
                    pRight -= 1
                else:
                    return False
            return True

        if len(p) == 0:
            return len(s) == 0

        if len(p) == 1:
            if p == "*":
                return True
            if p == "?" and len(s) == 1:
                return True
            if s==p:
                return True
            return False

        if len(s) == 0:
            if len(p) == 0:
                return True
            allStars = True
            for i in p:
                if i != "*":
                    allStars = False
                    break
            return allStars

        if len(s) == 1:
            for i in p:
                if i != "*":
                    continue
                else:
                    if i == s or i == "?":
                        return True
                    else:
                        return False

        while sLeft < sRight and pLeft < pRight:
            print(s[sLeft:sRight + 1], p[pLeft:pRight + 1])
            leftMatch = matchAndMoveRight()
            rightMatch = matchAndMoveLeft()
            if leftMatch and rightMatch:
                while pLeft < len(p) and p[pLeft] == "*":
                    pLeft += 1
                while pRight >= 0 and p[pRight] == "*":
                    pRight -= 1
            else:
                return False

        return True


# # TLE
# def isMatch(self, s: str, p: str) -> bool:
#     if p == "":
#         return s == ""
#     if s == "":
#         return p[0] == "*" and self.isMatch(s, p[1:])
#     if p[0] == "*":
#         starMeansBlank = self.isMatch(s, p[1:])
#         starMeansBusiness = self.isMatch(s[1:], p) if len(s) > 0 else False
#         return starMeansBlank or starMeansBusiness
#     elif p[0] == "?":
#         return self.isMatch(s[1:], p[1:]) if len(s) > 0 else False
#     else:
#         return self.isMatch(s[1:], p[1:]) if len(p) > 0 and len(s) > 0 and p[0] == s[0] else False


if __name__ == '__main__':
    print(Solution().isMatch("aaa", "aa"))
