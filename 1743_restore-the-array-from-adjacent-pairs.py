import collections


class Solution:
    def restoreArray(self, adjacentPairs):
        mapper = collections.defaultdict(set)
        for a, b in adjacentPairs:
            mapper[a].add(b)
            mapper[b].add(a)

        start = None
        for k in mapper.keys():
            if len(mapper[k]) == 1:
                start = k
                break

        out = []
        previous, current = None, start
        while True:
            out.append(current)
            if previous in mapper[current]:
                mapper[current].remove(previous)
            previous = current
            if len(mapper[current]) == 0:
                break
            current = mapper[current].pop()

        return out


if __name__ == '__main__':
    print(Solution().restoreArray(adjacentPairs = [[2,1],[3,4],[3,2]]))
    print(Solution().restoreArray(adjacentPairs = [[4,-2],[1,4],[-3,1]]))
    print(Solution().restoreArray(adjacentPairs = [[100000,-100000]]))

