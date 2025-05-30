class Solution:
    def numberOfWays(self, s: str) -> int:
        zeros, ones = 0, 0
        for char in s:
            if char == "0":
                zeros += 1
            else:
                ones += 1

        zeros_before, ones_before = 0, 0
        ans = 0
        for char in s:
            if char == "0":
                ans += ones_before * ones
                zeros -= 1
                zeros_before += 1
            else:
                ans += zeros_before * zeros
                ones -= 1
                ones_before += 1

        return ans

    # def numberOfWays(self, s: str) -> int:
    #     dp = {"0": 0, "01": 0, "010": 0, "1": 0, "10": 0, "101": 0}
    #     for char in s:
    #         if char == "0":
    #             dp["0"] += 1
    #             dp["10"] += dp["1"]
    #             dp["010"] += dp["01"]
    #         else:
    #             dp["1"] += 1
    #             dp["01"] += dp["0"]
    #             dp["101"] += dp["10"]
    #
    #     return dp["101"] + dp["010"]


if __name__ == '__main__':
    print(Solution().numberOfWays(s="001101"))
