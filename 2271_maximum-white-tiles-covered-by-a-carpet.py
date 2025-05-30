import collections
import heapq
import bisect


class Solution:

    """
    There exists a far simpler solution to this problem. Had I not been thinking about optimisation and all these algos, I would have caught this sooner.
    Infact I had started out with this exact same idea.

    Solution : This is a fairly straight forward solution.
    We keep two pointers. One from where we begin to roll the carpet and one till where we had rolled the carpet last.
    The intuition is that we should start to roll the carpet from the start of an interval, because if we start to roll from some start + x, we might discover a new tile, but we would most definitely uncover x tiles in the process.

    Accepted 26%
    """
    def maximumWhiteTiles(self, tiles, carpetLen: int) -> int:
        tiles.sort()
        start, end = 0, 0
        covered_area = 0
        partial = 0
        max_covered_area = 0
        while start < len(tiles):
            carpet_end = tiles[start][0] + carpetLen - 1
            while end < len(tiles) and tiles[end][0] <= carpet_end:
                if tiles[end][1] <= carpet_end:
                    # complete match
                    covered_area += tiles[end][1] - tiles[end][0] + 1
                else:
                    # partial match
                    partial = carpet_end - tiles[end][0] + 1
                    break
                end += 1

            max_covered_area = max(max_covered_area, covered_area + partial)
            covered_area -= (tiles[start][1] - tiles[start][0] + 1)
            partial = 0
            start += 1

        return max_covered_area




    # """
    # The idea with this was simple enough. Take a running sum of all the numbers in sorted order. Iterate over the them one by one, keeping the length of the carpet <= carpetLen and measure out the covered area.
    # The problem with this is we move in the increments of the numbers on the line.
    # [[1,5],[10,13],[14,22]], 10
    # In this case we consider [1, 10], [5, 14], [10, 13], but we don't do [10, 20] because 20 is not on the line. We also can't just add the remainder because it may be in the area between two tiled areas.
    #
    # Accepted : 5%. Changed the solution
    # """
    # def maximumWhiteTiles(self, tiles, carpetLen: int) -> int:
    #     tiles.sort()
    #     running_sum = collections.defaultdict(int)
    #     current_sum = 0
    #     for start, end in tiles:
    #         if start in running_sum:
    #             del running_sum[start]
    #         else:
    #             running_sum[start] = current_sum
    #         current_sum += end - start + 1
    #         running_sum[end + 1] = current_sum
    #
    #     max_carpet_len = 0
    #     line = sorted(running_sum.keys())
    #
    #     def covered_area_less_than(number):
    #         if number <= 0:
    #             return 0
    #         index = bisect.bisect_right(line, number)
    #         if index % 2 == 0:
    #             return running_sum[line[index - 1]]
    #         else:
    #             return running_sum[line[index - 1]] + number - line[index - 1]
    #
    #     for i in range(0, len(line), 2):
    #         max_carpet_len = max(max_carpet_len, covered_area_less_than(line[i] + carpetLen) - covered_area_less_than(line[i]))
    #         # max_carpet_len = max(max_carpet_len, covered_area_less_than(i + carpetLen) - covered_area_less_than(i), covered_area_less_than(i) - covered_area_less_than(i - carpetLen))
    #
    #     return max_carpet_len


if __name__ == '__main__':
    print(Solution().maximumWhiteTiles(tiles = [[1,5],[10,13],[14,22]], carpetLen = 10))
    print(Solution().maximumWhiteTiles([[1,1],[2,2],[5,5]], 2))
    print(Solution().maximumWhiteTiles(tiles = [[1,5],[10,11],[12,18],[20,25],[30,32]], carpetLen = 10))
    print(Solution().maximumWhiteTiles(tiles = [[10,11],[1,1]], carpetLen = 2))
    print(Solution().maximumWhiteTiles([[3745,3757],[3663,3681],[3593,3605],[3890,3903],[3529,3539],[3684,3686],[3023,3026],[2551,2569],[3776,3789],[3243,3256],[3477,3497],[2650,2654],[2264,2266],[2582,2599],[2846,2863],[2346,2364],[3839,3842],[3926,3935],[2995,3012],[3152,3167],[4133,4134],[4048,4058],[3719,3730],[2498,2510],[2277,2295],[4117,4128],[3043,3054],[3394,3402],[3921,3924],[3500,3514],[2789,2808],[3291,3294],[2873,2881],[2760,2760],[3349,3362],[2888,2899],[3802,3822],[3540,3542],[3128,3142],[2617,2632],[3979,3994],[2780,2781],[3213,3233],[3099,3113],[3646,3651],[3956,3963],[2674,2691],[3860,3873],[3363,3370],[2727,2737],[2453,2471],[4011,4031],[3566,3577],[2705,2707],[3560,3565],[3454,3456],[3655,3660],[4100,4103],[2382,2382],[4032,4033],[2518,2531],[2739,2749],[3067,3079],[4068,4074],[2297,2312],[2489,2490],[2954,2974],[2400,2418],[3271,3272],[3628,3632],[3372,3377],[2920,2940],[3315,3330],[3417,3435],[4146,4156],[2324,2340],[2426,2435],[2373,2376],[3621,3626],[2826,2832],[3937,3949],[3178,3195],[4081,4082],[4092,4098],[3688,3698]], 1638))
