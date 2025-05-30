import collections


class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if len(str1) != len(str2):
            return False
        change_map = {}
        reverse_change_map = collections.defaultdict(list)
        for i in range(len(str1)):
            if str1[i] in change_map.keys():
                if change_map[str1[i]] != str2[i]:
                    return False
            else:
                change_map[str1[i]] = str2[i]
                reverse_change_map[str2[i]].append(str1[i])

        for char in change_map:
            if char == change_map[char]:
                continue
            nodes = set()

            while char in change_map:
                if char in nodes:
                    if len(reverse_change_map) < 26:
                        break
                    else:
                        return False
                nodes.add(char)
                char = change_map[char]

        return True

    """
    Revision 2:
    I didn't write the code just now. But I had figured the code out because I remembered my past mistake of comparing the counters of both the strings to check if they have same frequencies.
    This method doesn't work because there can be multiple steps involved in this. abc -> ddd which is true in this case but would give false according to my assumption.
    The other reason why this method fails is that it doesn't consider the fact that once a character has been registered in the change map it can NOT be altered afterwards. a->c cannot have a->b conversion later in the string.
    
    There was one thing I absolutely missed in this.
    (1) - This
    """
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return True
        change_map = {}
        reverse_change_map = collections.defaultdict(list)
        for i in range(len(str1)):
            if str1[i] in change_map.keys():
                if change_map[str1[i]] != str2[i]:
                    return False
            else:
                change_map[str1[i]] = str2[i]
                reverse_change_map[str2[i]].append(str1[i])

        """
        (1)
        It took me some time to recognise why I wrote this. It's because abcdefghijklmnopqrstuvwxyz cannot be converted to zyxwvutsrqponmlkjihgfedcba.
        A complete conversion of strings cannot happen. Simply because once I convert any occurrence of a character to the other it's previous occurrence and this are bound. abc -(b->c)-> acc -(c->d)-> add.
        Try converting abc to cba assuming there are only a,b,c characters in the alphabet.
        """
        if len(reverse_change_map) < 26:
            return True
        return False

    """
    Attempt: Fired
    Accepted: 5%
    """
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return True
        m = collections.defaultdict(chr)

        for i in range(len(str1)):
            c1, c2 = str1[i], str2[i]
            if c1 in m:
                if m[c1] == c2:
                    continue
                else:
                    return False
            m[c1] = c2

        return len(set([m[c1] for c1 in m])) != 26


if __name__ == '__main__':
    print(Solution().canConvert("abcdefghijklmnopqrstuvwxyz", "zyxwvutsrqponmlkjihgfedcba"))
    print(Solution().canConvert(str1 = "ab", str2 = "ba"))
    print(Solution().canConvert(str1 = "aabcc", str2 = "ccdee"))
    print(Solution().canConvert(str1 = "leetcode", str2 = "codeleet"))
    print(Solution().canConvert("abcdefghijklmnopqrstuvwxyz", "bcdefghijklmnopqrstuvwxyza"))
    print(Solution().canConvert("abcdefghijklmnopqrstuvwxyz", "bcadefghijklmnopqrstuvwxzz"))
    print(Solution().canConvert("abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz"))
