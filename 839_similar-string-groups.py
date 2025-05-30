class DSU:

    def __init__(self, length):
        self.parent = [i for i in range(length)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        parent_a, parent_b = self.find(a), self.find(b)
        if parent_b == parent_a:
            return
        self.parent[parent_b] = parent_a


class Solution:
    def numSimilarGroups(self, strs) -> int:
        dsu = DSU(len(strs))

        def compare(s1, s2):
            if s1 == s2:
                return True
            diff = []
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    diff.append(i)
                    if len(diff) > 2:
                        return False
            if len(diff) != 2:
                return False
            return s1[diff[0]] == s2[diff[1]] and s2[diff[0]] == s1[diff[1]]

        for i in range(len(strs) - 1):
            for j in range(i + 1, len(strs)):
                if compare(strs[i], strs[j]):
                    dsu.union(i, j)

        groups = set()
        for i in range(len(strs)):
            groups.add(dsu.find(i))

        return len(groups)


if __name__ == '__main__':
    print(Solution().numSimilarGroups(strs = ["omv","ovm"]))
    print(Solution().numSimilarGroups(["kccomwcgcs","socgcmcwkc","sgckwcmcoc","coswcmcgkc","cowkccmsgc","cosgmccwkc","sgmkwcccoc","coswmccgkc","kowcccmsgc","kgcomwcccs"]))
