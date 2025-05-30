class Solution:
    def numSpecialEquivGroups(self, words) -> int:
        def getHash(word):
            odd, even = [], []
            for i, c in enumerate(word):
                if i % 2 == 0:
                    even.append(c)
                else:
                    odd.append(c)

            return "".join(sorted(odd)) + "".join(sorted(even))

        return len(set([getHash(word) for word in words]))


if __name__ == '__main__':
    print(Solution().numSpecialEquivGroups(words = ["abcd","cdab","cbad","xyzz","zzxy","zzyx"]))
    print(Solution().numSpecialEquivGroups(words = ["abc","acb","bac","bca","cab","cba"]))
