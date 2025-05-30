import collections


class Solution:

    def findOriginalArray(self, changed):
        n = len(changed)
        if n % 2 == 1:
            return []
        counter = collections.Counter(changed)
        out = []
        for i in sorted(counter):
            if counter[i] == 0:
                continue
            if 2 * i not in counter or counter[2 * i] < counter[i]:
                return []
            while counter[i] > 0:
                counter[2 * i] -= 1
                counter[i] -= 1
                out.append(i)
            del counter[i]

        return out


    # # Simpler Code 50%
    # def findOriginalArray(self, changed):
    #     changed.sort()
    #     values = collections.defaultdict(int)
    #     for i in range(len(changed)):
    #         values[changed[i]] += 1
    #
    #     result = []
    #     for value in values:
    #         count = values[value]
    #         if count == 0:
    #             continue
    #
    #         if value == 0:
    #             if count % 2 == 1:
    #                 return []
    #             result += [0 for _ in range(count // 2)]
    #             values[0] = 0
    #             continue
    #
    #         if value * 2 in values and values[value * 2] > 0 and values[value * 2] >= count:
    #             values[value] = 0
    #             values[value * 2] -= count
    #             result += [value for _ in range(count)]
    #         else:
    #             return []
    #     return result

    # # 62%
    # def findOriginalArray(self, changed):
    #     changed.sort()
    #     values = collections.defaultdict(int)
    #     for i in range(len(changed)):
    #         values[changed[i]] += 1
    #
    #     result = []
    #     for value in values:
    #         count = values[value]
    #         if count == 0:
    #             continue
    #
    #         if value == 0:
    #             if count % 2 == 1:
    #                 return []
    #             result += [0 for _ in range(count // 2)]
    #             values[0] = 0
    #             continue
    #
    #         if value % 2 == 1:
    #             if (2 * value) not in values:
    #                 return []
    #             else:
    #                 valueDoubleCount = values[2 * value]
    #                 if valueDoubleCount < count:
    #                     return []
    #                 values[2 * value] -= count
    #                 values[value] -= count
    #                 result += [value for _ in range(count)]
    #         else:
    #             if value // 2 in values and values[value // 2] > 0:
    #                 valueHalfCount = values[value // 2]
    #                 count -= valueHalfCount
    #                 values[value // 2] = 0
    #                 values[value] = count
    #                 result += [value // 2 for _ in range(valueHalfCount)]
    #
    #             if count > 0 and value * 2 in values and values[value * 2] > 0:
    #                 valueDoubleCount = values[2 * value]
    #                 if valueDoubleCount < count:
    #                     return []
    #                 values[value * 2] -= count
    #                 result += [value for _ in range(count)]
    #                 values[value] -= count
    #         if values[value] != 0:
    #             return []
    #     return result


if __name__ == '__main__':
    print(Solution().findOriginalArray(changed=[4, 8, 2, 16, 1, 8]))
    print(Solution().findOriginalArray(changed = [1,3,4,2,6,8]))
    print(Solution().findOriginalArray(changed = [6,3,0,1]))
    print(Solution().findOriginalArray(changed = [1]))
    print(Solution().findOriginalArray(changed = [0, 0, 0, 0]))
