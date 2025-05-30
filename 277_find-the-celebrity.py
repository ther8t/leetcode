# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:
import collections


class Solution:

    def findCelebrity(self, n: int) -> int:
        def knows(a, b):
            graph = [[1, 1, 0], [0, 1, 0], [1, 1, 1]]
            graph = [[1,0,1],[1,1,0],[0,1,1]]
            return bool(graph[a][b])

        indegree, outdegree = collections.defaultdict(set), collections.defaultdict(set)
        suspects = set([i for i in range(n)])

        for i in range(n):
            if i not in suspects:
                continue
            for j in range(n):
                if i == j:
                    continue
                k = knows(i, j)
                if k:
                    outdegree[i].add(j)
                    indegree[j].add(i)
                    suspects.remove(i)
                    break

        removelist = []
        for s in suspects:
            for c in range(n):
                if s == c:
                    continue
                if c in indegree[s]:
                    continue
                k = knows(c, s)
                if not k:
                    removelist.append(s)
                    break
                outdegree[c].add(s)
                indegree[s].add(c)

        for r in removelist:
            suspects.remove(r)

        suspects = list(suspects)
        return suspects[0] if len(suspects) == 1 else -1


if __name__ == '__main__':
    print(Solution().findCelebrity(3))
