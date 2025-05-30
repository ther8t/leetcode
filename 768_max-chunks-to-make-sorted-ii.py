import collections


class Solution:
    # The idea is that every digit wants to go to a place in the sorted array.
    # A chunk is formed when all the places in that chunk are within the chunk itself.
    # So the maximum place any element of the chunk wants to be at must be within the chunk or otherwise it's not a chunk yet
    def maxChunksToSorted(self, arr) -> int:
        for index, value in enumerate(arr):
            arr[index] = (value, index)

        arr.sort()

        max_index = -1
        chunks = 0
        for i, (value, index) in enumerate(arr):
            max_index = max(max_index, index)
            if max_index == i:
                chunks += 1

        return chunks



    # # can also be done using sum of the previous aside from counter
    # def maxChunksToSorted(self, arr) -> int:
    #     n = len(arr)
    #     sorted_arr = list(sorted(arr))
    #     start, end = 0, 0
    #
    #     chunks = 0
    #     while start < n and end < n:
    #         end = start
    #         arr_set, sorted_arr_set = 0, 0
    #         while end < n:
    #             arr_set += arr[end]
    #             sorted_arr_set += sorted_arr[end]
    #             end += 1
    #             if arr_set == sorted_arr_set:
    #                 break
    #         chunks += 1
    #         start = end
    #     return chunks
    #
    # def maxChunksToSorted(self, arr) -> int:
    #     n = len(arr)
    #     sorted_arr = list(sorted(arr))
    #     start, end = 0, 0
    #
    #     chunks = 0
    #     while start < n and end < n:
    #         end = start
    #         arr_set, sorted_arr_set = collections.Counter(), collections.Counter()
    #         while end < n:
    #             arr_set[arr[end]] += 1
    #             sorted_arr_set[sorted_arr[end]] += 1
    #             end += 1
    #             if arr_set == sorted_arr_set:
    #                 break
    #         chunks += 1
    #         start = end
    #     return chunks


if __name__ == '__main__':
    print(Solution().maxChunksToSorted(arr = [5,4,3,2,1]))
    print(Solution().maxChunksToSorted(arr = [2,1,3,4,4]))
    print(Solution().maxChunksToSorted([1,1,1,0,1,0,0,0,1,0]))
