from collections import Counter


class Solution:
    def topKFrequent(self, nums, k: int):
        counter = Counter(nums)
        sorted_counter = sorted(counter, key=lambda x:counter[x], reverse=True)
        return sorted_counter[:k]


if __name__ == '__main__':
    print(Solution().topKFrequent(nums = [1,1,1,2,2,3], k = 2))
    print(Solution().topKFrequent(nums = [1], k = 1))
