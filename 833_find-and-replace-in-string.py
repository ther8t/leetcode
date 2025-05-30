class Solution:
    """
    Revision 2:
    This is a good algo. I was thinking along the same lines.
    My idea was to iterate over all the indexes of string and to use a pointer to see if indexes match the iteration.
    Perhaps I need to relax.
    """
    def findReplaceString(self, s: str, indices, sources, targets) -> str:
        stringMaker = list(s)

        for i, index in enumerate(indices):
            source = sources[i]
            target = targets[i]
            stringSource = s[index: index + len(source)]
            if stringSource == source:
                stringMaker[index] = target
                for j in range(index + 1, index + len(source)):
                    stringMaker[j] = ""

        return "".join(stringMaker)

if __name__ == '__main__':
    print(Solution().findReplaceString(s = "abcd", indices = [0, 2], sources = ["ab","ec"], targets = ["eee","ffff"]))
