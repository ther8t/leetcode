import collections
import functools


class Solution:

    def minimizeMax(self, nums, p: int) -> int:
        nums.sort()
        diff_map = collections.defaultdict(list)
        covered_set = set()
        for i in range(len(nums) - 1):
            diff_map[nums[i + 1] - nums[i]].append((i, i + 1))

        ans = 0
        for diff in sorted(diff_map.keys()):
            for a, b in diff_map[diff]:
                if p == 0:
                    return ans
                if a not in covered_set and b not in covered_set:
                    ans += diff
                    covered_set.add(a)
                    covered_set.add(b)
                    p -= 1

        return ans

    """
    TLE
    """
    def minimizeMax(self, nums, p: int) -> int:
        nums.sort()

        @functools.lru_cache(None)
        def min_max_diff(index, p):
            if p == 0:
                return 0
            if index >= len(nums) - 1:
                return float('inf')
            return min(max(nums[index + 1] - nums[index], min_max_diff(index + 2, p - 1)), min_max_diff(index + 1, p))

        return min_max_diff(0, p)


    """
    Wrong answer:
    The reason for that is since we use greedy and my idea was to capture the least diff first, so there might be a case where one selection interferes with the other.
    [1, 2, 2, 2, 4] i = 1, 2 is selected for diff = 0.
    But this 
    """
    def minimizeMax(self, nums, p: int) -> int:
        nums.sort()

        diffs = collections.defaultdict(list)

        for i in range(len(nums) - 1):
            diffs[abs(nums[i + 1] - nums[i])].append((i, i + 1))

        def check():
            used = set()
            count = 0
            for d in sorted(diffs.keys()):
                if d > mid or count > p:
                    break
                for a, b in diffs[d]:
                    if a not in used and b not in used:
                        used.add(a)
                        used.add(b)
                        count += 1
            return count >= p

        lo, hi = 0, nums[-1] - nums[0]
        while lo < hi:
            mid = (lo + hi) // 2
            if check():
                hi = mid
            else:
                lo = mid + 1

        return hi


    def minimizeMax(self, nums, p: int) -> int:
        nums.sort()

        diffs = collections.defaultdict(list)

        for i in range(len(nums) - 1):
            diffs[abs(nums[i + 1] - nums[i])].append((i, i + 1))

        def check():
            index, count = 0, 0
            while index < len(nums) - 1:
                # If a valid pair is found, skip both numbers.
                if nums[index + 1] - nums[index] <= mid:
                    count += 1
                    index += 1
                if count >= p:
                    return True
                index += 1
            return count >= p

        lo, hi = 0, nums[-1] - nums[0]
        while lo < hi:
            mid = (lo + hi) // 2
            if check():
                hi = mid
            else:
                lo = mid + 1

        return hi



if __name__ == '__main__':
    print(Solution().minimizeMax([3,4,2,3,2,1,2], 3))
    # print(Solution().minimizeMax(nums = [10,1,2,7,1,3], p = 2))
    # print(Solution().minimizeMax(nums = [4,2,1,2], p = 1))
    # print(Solution().minimizeMax([8,9,1,5,4,3,6,4,3,7], 4))
    # print(Solution().minimizeMax([75841,10836,90297,65300,2691,4222,31819,62366,74592,61726,2747,25749,82186,13526,68417,20213,51542,53629,48677,39515,1420,29980,82925,28030,48133,8712,18133,58186,90944,14106,58497,7113,22120,37507,8118,34489,55965,48887,18831,17644,77696,23889,705,28242,76776], 11))
