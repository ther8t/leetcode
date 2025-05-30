class Solution:
    def fullJustify(self, words, maxWidth: int):
        wordIndex = 0
        stringOutput = []
        while wordIndex < len(words):
            wordsWhichCanBeAdjusted = 0
            wordLengthCount = 0
            for i in range(wordIndex, len(words)):
                if (wordsWhichCanBeAdjusted + wordLengthCount + len(words[i])) > maxWidth:
                    break
                wordLengthCount += len(words[i])
                wordsWhichCanBeAdjusted += 1
            equalSpaceCount = 1
            extraSpaceCount = 0
            equalSpace = " "
            if wordsWhichCanBeAdjusted > 1 and wordIndex + wordsWhichCanBeAdjusted < len(words):
                # not the last row
                equalSpaceCount = (maxWidth - wordLengthCount) // (wordsWhichCanBeAdjusted - 1)
                extraSpaceCount = (maxWidth - wordLengthCount) % (wordsWhichCanBeAdjusted - 1)
                equalSpace = ""
                for i in range(equalSpaceCount):
                    equalSpace += " "

            outputRowString = ""
            charsFilled = 0
            wordsFilled = 0
            while wordsFilled < wordsWhichCanBeAdjusted:
                print(words[wordIndex + wordsFilled])
                outputRowString += words[wordIndex + wordsFilled]
                charsFilled += len(words[wordIndex + wordsFilled])
                if wordsFilled < wordsWhichCanBeAdjusted - 1:
                    outputRowString += equalSpace
                    charsFilled += len(equalSpace)
                if extraSpaceCount != 0:
                    outputRowString += " "
                    charsFilled += 1
                    extraSpaceCount -= 1
                wordsFilled += 1
            while (maxWidth - charsFilled) > 0:
                outputRowString += " "
                charsFilled += 1
            stringOutput.append(outputRowString)
            wordIndex += wordsWhichCanBeAdjusted

        return stringOutput


if __name__ == '__main__':
    print(Solution().fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20))
