import re


class Solution:
    # def reverse(self, string, reverseRange):
    #     start, end = reverseRange[0], reverseRange[1]
    #     outputString = string[0:start]
    #     for i in range(end - 1, start - 1, -1):
    #         outputString += string[i]
    #     outputString += string[end:]
    #     return outputString

    """
    Revision 2 : I figured out some of the things about the question but not the actual solution. I was able to deduce that that two string would be convertible if the sequence of R and L is the same.
    and that every one of the R and L have a correspondence in the start and end string. I however got stuck with evaluating X. The trick however is:
    There is a correspondence between Rs and Ls of start and end string. If RX -> XR which means that in the end, position of R > position of R in start. The reverse is true for L.
    If either the characters in the string are not the same or their positions are not appropriate return False. Return True if all pans out.
    """
    def canTransform(self, start: str, end: str) -> bool:
        ptrStart, ptrEnd, N = 0, 0, len(start)

        while ptrStart < N or ptrEnd < N:
            while ptrStart < N and start[ptrStart] == 'X':
                ptrStart += 1
            while ptrEnd < N and end[ptrEnd] == 'X':
                ptrEnd += 1
            if ptrStart == N or ptrEnd == N:
                return ptrStart == ptrEnd

            if (start[ptrStart] != end[ptrEnd]) or (start[ptrStart] == 'L' and ptrStart < ptrEnd) or (
                    start[ptrStart] == 'R' and ptrStart > ptrEnd):
                return False
            ptrStart += 1
            ptrEnd += 1

        return True

    # def canTransform(self, start: str, end: str) -> bool:
    # if start == end:
    #     return True
    # similarTill = -1
    # for i in range(len(start)):
    #     if i + 1 < len(start) and start[similarTill + 1] != end[similarTill + 1]:
    #         break
    #     similarTill += 1
    #
    # ptr1 = similarTill + 1
    # ptr2 = similarTill + 1
    # while ptr2<len(start):
    #     if self.reverse(start, (ptr1, ptr2+1))[ptr1: ptr2+1] == end[ptr1: ptr2+1]:
    #         break
    #
    #
    # startLMatch = re.search("X+L", start[similarTill + 1:])
    # startRMatch = re.search("RX+", start[similarTill + 1:])
    #
    # lMatchRange = (similarTill + 1 + startLMatch.start(), similarTill + 1 + startLMatch.end())  # [)
    # rMatchRange = (similarTill + 1 + startRMatch.start(), similarTill + 1 + startRMatch.end())  # [)
    #
    # if startLMatch is not None and self.reverse(start, lMatchRange)[lMatchRange[0]:lMatchRange[1]] == end[
    #                                                                                                   lMatchRange[
    #                                                                                                       0]:
    #                                                                                                   lMatchRange[
    #                                                                                                       1]]:
    #     return self.canTransform(start[lMatchRange[1]: len(start)],
    #                              end[lMatchRange[1]: len(start)])
    #
    # if startRMatch is not None and self.reverse(start, rMatchRange)[rMatchRange[0]:rMatchRange[1]] == end[
    #                                                                                                   rMatchRange[
    #                                                                                                       0]:
    #                                                                                                   rMatchRange[
    #                                                                                                       1]]:
    #     return self.canTransform(start[rMatchRange[1]: len(start)],
    #                              end[rMatchRange[1]: len(start)])
    # #
    # # endLMatch = re.search("LX+", end[similarTill + 1:])
    # # endRMatch = re.search("X+R", end[similarTill + 1:])
    # #
    # # if startLMatch is not None and startLMatch.start() == 0 and endLMatch is not None and endLMatch.start() == 0 and (endLMatch.end() - endLMatch.start()) >= (startLMatch.end() - startLMatch.start()):
    # #     reverseRange = (similarTill + 1, similarTill + 1 + min(startLMatch.end() - 1, endLMatch.end() - 1))
    # #     start = self.reverse(start, reverseRange)
    # #     return self.canTransform(start[reverseRange[1] + 1:], end[reverseRange[1] + 1:])
    # #
    # # if startRMatch is not None and startRMatch.start() == 0 and endRMatch is not None and endRMatch.start() == 0 and (startRMatch.end() - startRMatch.start()) >= (endRMatch.end() - endRMatch.start()):
    # #     reverseRange = (similarTill + 1, similarTill + 1 + min(startRMatch.end() - 1, endRMatch.end() - 1))
    # #     start = self.reverse(start, reverseRange)
    # #     return self.canTransform(start[reverseRange[1] + 1:], end[reverseRange[1] + 1:])
    #
    # return False

    # def canTransform(self, start: str, end: str) -> bool:
    #     if start == end:
    #         return True
    #     if len(start) <= 1:
    #         return False
    #
    #     foundIndex = -1
    #     for i in range(len(start)):
    #         if i + 1 < len(start) and (start[i:i + 2] in ["XL", "RX"]):
    #             foundIndex = i
    #             break
    #     if foundIndex == -1:
    #         return False
    #
    #     canTransform = False
    #     if start[0:foundIndex+1] == end[0:foundIndex+1]:
    #         canTransform = self.canTransform(start[foundIndex + 1:], end[foundIndex + 1:])
    #     if not canTransform:
    #         start = self.flip(start, foundIndex)
    #         canTransform = self.canTransform(start, end)
    #     return canTransform

    def flip(self, start, foundIndex):
        return start[0:foundIndex] + start[foundIndex + 1] + start[foundIndex] + start[foundIndex + 2:]


if __name__ == '__main__':
    print(Solution().canTransform("XXXXXLXXXLXXXX", "XXLXXXXXXXXLXX"))
