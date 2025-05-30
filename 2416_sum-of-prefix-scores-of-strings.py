import collections

Trie = lambda: collections.defaultdict(Trie)
COUNT = "#"


class Solution:
    # Using tries
    def sumPrefixScores(self, words):
        if len(words) == 1:
            return [len(words[0])]

        trie = Trie()
        for w in words:
            temp = trie
            for char in w:
                temp = temp[char]
                if COUNT not in temp:
                    temp[COUNT] = 0
                temp[COUNT] += 1

        out = []
        for w in words:
            score = 0
            temp = trie
            for char in w:
                temp = temp[char]
                score += temp[COUNT]
            out.append(score)

        return out

    def sumPrefixScores(self, words):
        if len(words) == 1:
            return [len(words[0])]
        prefix_word_map = collections.defaultdict(list)
        for w in words:
            builder = ""
            for char in w:
                builder += char
                prefix_word_map[builder].append(w)

        out = []
        for w in words:
            builder = ""
            ans = 0
            for char in w:
                builder += char
                ans += len(prefix_word_map[builder])
            out.append(ans)

        return out


if __name__ == '__main__':
    print(Solution().sumPrefixScores(words = ["abc","ab","bc","b"]))
    print(Solution().sumPrefixScores(words = ["abcd"]))
    print(Solution().sumPrefixScores(["qtcqcmwcin","vkjotbrbzn","eoorlyfche","eoorlyhn","eoorlyfcxk","qfnmjilcom","eoorlyfche","qtcqcmwcnl","qtcqcrpjr"]))
