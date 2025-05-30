# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
import collections


class Master:
    def guess(self, word: str) -> int:
        secretWord = "ccoyyo"
        score = 0
        for i in range(len(secretWord)):
            if secretWord[i] == word[i]:
                score += 1
        return score


class Solution:
    def findSecretWord(self, wordlist, master: 'Master') -> None:
        guessedArray = []

        probabilityCard = [[0 for _ in range(26)] for _ in range(6)]
        scoreCard = [0 for _ in range(len(wordlist))]

        for i in range(len(wordlist)):
            for j in range(len(wordlist[i])):
                probabilityCard[j][ord(wordlist[i][j]) - 97] += 1/len(wordlist)

        for i in range(len(wordlist)):
            # update the score card
            for i in range(len(wordlist)):
                for characterIndex in range(len(wordlist[i])):
                    scoreCard[i] += probabilityCard[characterIndex][ord(wordlist[i][characterIndex]) - 97]

            # find the most probable word.
            maxScoreIndex = 0
            maxScore = -1
            for i in range(len(wordlist)):
                if wordlist[i] not in guessedArray and scoreCard[i] > maxScore:
                    maxScore = scoreCard[i]
                    maxScoreIndex = i

            print("Selected word - " + wordlist[maxScoreIndex] + " at " + str(maxScoreIndex) + " Score = " + str(
                scoreCard[maxScoreIndex]))

            # match it to the secret word.
            selectedWord = wordlist[maxScoreIndex]
            matchScore = master.guess(selectedWord)
            guessedArray.append(selectedWord)
            print("Match Score - " + str(matchScore))
            if matchScore == 6:
                break

            scoreUpdate = matchScore / 6 if matchScore > 0 else -1000

            # update the probability card
            for i in range(len(selectedWord)):
                character = selectedWord[i]
                probabilityCard[i][ord(character) - 97] += scoreUpdate


    """
    Revision 2:
    I had planned on an algo a bit different from the solution.
    My idea was to have a most probable word, which would be the encapsulation of all the word characters most probable at their respective indices.
    Then find the score of each word with this that most probable word and choose one of the word.
    This is the same as calculating prob of each character at index and update it.
    
    There is one small catch with this though and I could not figure it out. For some reason, a single word(not the answer) can come up as most likely word repeatedly.
    In order to counter that, we use a visited/guessed set.
    """
    def findSecretWord(self, wordlist, master: 'Master') -> None:
        guessed = set()
        probability_counter = [collections.Counter() for _ in range(6)]

        for word in wordlist:
            for index, char in enumerate(word):
                probability_counter[index][char] += 1 / len(wordlist)

        a = 0
        for i in range(len(wordlist)):
            a += 1
            score_card = collections.defaultdict(int)

            for word_index in range(len(wordlist)):
                for index in range(6):
                    score_card[wordlist[word_index]] += probability_counter[index][wordlist[word_index][index]]

            sorted_word_list = sorted(wordlist, key=lambda x: score_card[x] + 0 if x not in guessed else -1000, reverse=True)
            chosen_word = sorted_word_list[0]
            guessed.add(chosen_word)
            match = master.guess(chosen_word)
            if match == 6:
                print(a)
                break

            for index in range(6):
                probability_counter[index][chosen_word[index]] += match / 6 if match > 0 else -1000


if __name__ == '__main__':
    print(Solution().findSecretWord(
        ["wichbx", "oahwep", "tpulot", "eqznzs", "vvmplb", "eywinm", "dqefpt", "kmjmxr", "ihkovg", "trbzyb", "xqulhc",
         "bcsbfw", "rwzslk", "abpjhw", "mpubps", "viyzbc", "kodlta", "ckfzjh", "phuepp", "rokoro", "nxcwmo", "awvqlr",
         "uooeon", "hhfuzz", "sajxgr", "oxgaix", "fnugyu", "lkxwru", "mhtrvb", "xxonmg", "tqxlbr", "euxtzg", "tjwvad",
         "uslult", "rtjosi", "hsygda", "vyuica", "mbnagm", "uinqur", "pikenp", "szgupv", "qpxmsw", "vunxdn", "jahhfn",
         "kmbeok", "biywow", "yvgwho", "hwzodo", "loffxk", "xavzqd", "vwzpfe", "uairjw", "itufkt", "kaklud", "jjinfa",
         "kqbttl", "zocgux", "ucwjig", "meesxb", "uysfyc", "kdfvtw", "vizxrv", "rpbdjh", "wynohw", "lhqxvx", "kaadty",
         "dxxwut", "vjtskm", "yrdswc", "byzjxm", "jeomdc", "saevda", "himevi", "ydltnu", "wrrpoc", "khuopg", "ooxarg",
         "vcvfry", "thaawc", "bssybb", "ccoyyo", "ajcwbj", "arwfnl", "nafmtm", "xoaumd", "vbejda", "kaefne", "swcrkh",
         "reeyhj", "vmcwaf", "chxitv", "qkwjna", "vklpkp", "xfnayl", "ktgmfn", "xrmzzm", "fgtuki", "zcffuv", "srxuus",
         "pydgmq"], Master()))
