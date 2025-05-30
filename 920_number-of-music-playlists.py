class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        total = 1
        for i in range(1, n + 1):
            total *= i
            total %= MOD
        for i in range(n + 1, goal + 1):
            total *= (n - k)
            total %= MOD

        return total


if __name__ == '__main__':
    print(Solution().numMusicPlaylists(n = 3, goal = 3, k = 1))
    print(Solution().numMusicPlaylists(n = 2, goal = 3, k = 0))
    print(Solution().numMusicPlaylists(n = 2, goal = 3, k = 1))
