import collections


class Solution:
    def maxScoreWords(self, words, letters, score) -> int:
        word_scores = collections.defaultdict(int)

        for word in words:
            total_score = 0
            for c in word:
                total_score += score[(ord(c) - ord('a'))]
            word_scores[word] = total_score

        letters = collections.Counter(letters)

        ans = 0

        def dfs(index, stack):
            nonlocal ans
            if index == len(words):
                ans = max(ans, sum([word_scores[word] for word in stack]))
                return
            dfs(index + 1, stack)
            can_use = True
            word_counter = collections.Counter(words[index])
            for c in word_counter:
                if letters[c] < word_counter[c]:
                    can_use = False
                    break

            if can_use:
                for c in word_counter:
                    letters[c] -= word_counter[c]
                dfs(index + 1, stack + [words[index]])
                for c in word_counter:
                    letters[c] += word_counter[c]

        dfs(0, [])
        return ans


if __name__ == '__main__':
    print(Solution().maxScoreWords(words = ["dog","cat","dad","good"], letters = ["a","a","c","d","d","d","g","o","o"], score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]))
    print(Solution().maxScoreWords(words = ["xxxz","ax","bx","cx"], letters = ["z","a","b","c","x","x","x"], score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]))
    print(Solution().maxScoreWords(words = ["leetcode"], letters = ["l","e","t","c","o","d"], score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]))
