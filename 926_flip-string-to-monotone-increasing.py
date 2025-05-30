class Solution:

    # Just simplified version of the below code.
    def minFlipsMonoIncr(self, s: str) -> int:
        zero, one = 0, 0
        for i in range(len(s) - 1, -1, -1):
            zero = (0 if s[i] == "0" else 1) + min(zero, one)
            one = (1 if s[i] == "0" else 0) + one

        return min(zero, one)

    # # Accepted : 58%
    # def minFlipsMonoIncr(self, s: str) -> int:
    #     zero, one = 0, 0
    #     for i in range(len(s) - 1, -1, -1):
    #         if s[i] == "0":
    #             # if I wish to keep this 0, the next can be either 0 or 1
    #             zero = 0 + min(zero, one)
    #             # if I wish to flip this 0 to 1, the next can only be 1
    #             one = 1 + one
    #         else:
    #             # if I wish to flip this 1 to 0, the next can be either 0 or 1
    #             zero = 1 + min(one, zero)
    #             # if I wish to keep this 1, the next can be only 1
    #             one = 0 + one
    #
    #     return min(zero, one)


if __name__ == '__main__':
    print(Solution().minFlipsMonoIncr("00110"))
    print(Solution().minFlipsMonoIncr("010110"))
    print(Solution().minFlipsMonoIncr("00011000"))
