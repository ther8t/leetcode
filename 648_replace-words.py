class Solution:
    def replaceWords(self, dictionary, sentence: str) -> str:
        dictionary = set(dictionary)

        a = []
        for w in sentence.split(" "):
            word = ""
            for c in w:
                word += c
                if word in dictionary:
                    break
            a.append(word)
        return " ".join(a)


if __name__ == '__main__':
    print(Solution().replaceWords(dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"))
    print(Solution().replaceWords(dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"))
