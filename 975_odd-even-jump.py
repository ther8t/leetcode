import collections

from sortedcontainers import SortedList
import bisect

class Solution:

    """
    Revision 2 : This was the problem which first introduced me to monotonic stacks during Google's preparation.
    The thing about monotonic stacks is that we only need to arrange the array in the order that we need from the problem statement.
    The part which monotonic stacks solve is finding the next or previous index of pattern we need from the question.
    For example in this case we need the next smallest or largest number greater than or smaller than the number at index.
    Thus we need to rearrange the numbers in such a way that we form the pattern and then iterate over the array to get the number at the next indexes.
    """

    # TLE 61/65
    def oddEvenJumps(self, arr) -> int:
        n = len(arr)
        next_greater = list(range(n))
        stack = []
        for index in sorted(next_greater, key=lambda x: arr[x]):
            while stack and stack[-1] < index:
                next_greater[stack.pop()] = index
            stack.append(index)

        next_smaller = list(range(n))
        stack = []
        for index in sorted(next_smaller, key=lambda x: arr[x], reverse=True):
            while stack and stack[-1] < index:
                next_smaller[stack.pop()] = index
            stack.append(index)

        odd, even = [False] * n, [False] * n
        odd[-1], even[-1] = True, True
        for i in range(n - 2, -1, -1):
            if next_greater[i] != i and even[next_greater[i]]:
                odd[i] = True
            if next_smaller[i] != i and odd[next_smaller[i]]:
                even[i] = True

        return sum(odd)




    # def oddEvenJumps(self, arr) -> int:
    #     dp = {(len(arr) - 1, 'e'): True, (len(arr) - 1, 'o'): True}
    #
    #     next_greater = [-1 for _ in range(len(arr))]
    #     next_smaller = [-1 for _ in range(len(arr))]
    #
    #     ascending = sorted([(a, i) for i, a in enumerate(arr)])
    #     descending = sorted([(a, i) for i, a in enumerate(arr)], reverse=True, key=lambda x:(x[0], -x[1]))
    #
    #     stack = []
    #     for v, i in ascending:
    #         while stack and stack[-1] < i:
    #             next_greater[stack.pop()] = i
    #         stack.append(i)
    #
    #     for v, i in descending:
    #         while stack and stack[-1] < i:
    #             next_smaller[stack.pop()] = i
    #         stack.append(i)
    #
    #     def is_good(index, jump_polarity):
    #         if (index, jump_polarity) in dp:
    #             return dp[(index, jump_polarity)]
    #         if index == len(arr) - 1:
    #             return True
    #         next_index = index
    #         if jump_polarity == 'o' and next_greater[index] != -1:
    #             next_index = next_greater[index]
    #         elif jump_polarity == 'e' and next_smaller[index] != -1:
    #             next_index = next_smaller[index]
    #
    #         if next_index == index:
    #             dp[(index, jump_polarity)] = False
    #             return False
    #         is_next_good = is_good(next_index, 'o' if jump_polarity == 'e' else 'e')
    #         dp[(index, jump_polarity)] = is_next_good
    #         return is_next_good
    #
    #     counter = 0
    #     for i in range(len(arr)):
    #         if (i, 'o') in dp and dp[(i, 'o')]:
    #             counter += 1
    #             continue
    #         else:
    #             if is_good(i, 'o'):
    #                 counter += 1
    #
    #     return counter


if __name__ == '__main__':
    print(Solution().oddEvenJumps([1,2,3,2,1,4,4,5])) #6
    print(Solution().oddEvenJumps(arr = [5,1,3,4,2])) #3
    print(Solution().oddEvenJumps(arr = [2,3,1,1,4])) #3
    print(Solution().oddEvenJumps(arr = [10,13,12,14,15])) #2
    a = "0090"
    print(a.lstrip("0"))
