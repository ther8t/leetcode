import collections


class Solution:
    def alienOrder(self, words) -> str:
        graph = collections.defaultdict(set)
        counter = collections.Counter({c: 0 for word in words for c in word})

        for first, second in zip(words, words[1:]):
            for a, b in zip(first, second):
                if a != b:
                    if b not in graph[a]:
                        graph[a].add(b)
                        counter[b] += 1
                    break
            else:
                # This may seem like a redundant step but this is crucial. Imagine "abc" and "ab".
                # But why does it come to it. There is nothing added to the adjacency matrix or counter?
                # It's because though there is nothing added, we had to initialise the counter because the first zero indegree, would never come of it's own during iteration.
                if len(second) < len(first):
                    return ""

        queue = collections.deque()
        for key in counter:
            if counter[key] == 0:
                queue.append(key)

        out = []
        while queue:
            popped = queue.popleft()
            out.append(popped)
            for neighbour in graph[popped]:
                counter[neighbour] -= 1
                if counter[neighbour] == 0:
                    queue.append(neighbour)

        if len(out) != len(counter):
            return ""

        return "".join(out)


if __name__ == '__main__':
    # print(Solution().alienOrder(words = ["wrt","wrf","er","ett","rftt"]))
    # print(Solution().alienOrder(words = ["z","x","z"]))
    # print(Solution().alienOrder(words = ["z","x"]))
    print(Solution().alienOrder(words = ["abc","ab"]))
    # print(Solution().alienOrder(["z","x","a","zb","zx"]))
