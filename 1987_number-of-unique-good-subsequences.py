class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        MOD = 10 ** 9 + 7
        latest_zero_count, latest_one_count = 0, 0

        for char in binary:
            if char == '1':
                latest_one_count = (latest_one_count + latest_zero_count + 1) % MOD
            else:
                latest_zero_count = (latest_one_count + latest_zero_count) % MOD

        return latest_one_count + latest_zero_count + (1 if '0' in binary else 0)


if __name__ == '__main__':
    print(Solution().numberOfUniqueGoodSubsequences(binary = "001"))
    print(Solution().numberOfUniqueGoodSubsequences(binary = "11"))
    print(Solution().numberOfUniqueGoodSubsequences(binary = "101"))
