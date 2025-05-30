from itertools import accumulate


class Solution:
    """
    Revision 2 : The logic is that a sentence be accomodated multiple times in a single row so we pre-calculate the number of times a sentence is repeated in a single row.
    We add that to the sentence count as row * sentence_count_in_one_row. The remaining space is the one in which we try and fit more sentences.
    For that we make the effort just as if the space was not enough to fit one sentence. Add these two up.
    """
    def wordsTyping(self, sentence, rows: int, cols: int) -> int:
        word_ptr = -1
        sentence_count = 0
        sentence_length = 0
        for word in sentence:
            sentence_length += len(word)
        sentence_length += len(sentence) - 1
        sentences_accomodated_in_one_col = (cols) // (sentence_length + 1)
        cols = cols % (sentence_length + 1)

        def next_word():
            if word_ptr == len(sentence) - 1:
                return sentence[0]
            return sentence[word_ptr + 1]

        def word_chosen(word_ptr, sentence_count):
            if word_ptr == len(sentence) - 1:
                word_ptr = -1
            if word_ptr == len(sentence) - 2:
                sentence_count += 1
            word_ptr += 1
            return word_ptr, sentence_count

        for _ in range(rows):
            space_available = cols
            sentence_count += sentences_accomodated_in_one_col
            while space_available >= len(next_word()):
                space_available -= (len(next_word()) + 1)
                word_ptr, sentence_count = word_chosen(word_ptr, sentence_count)

        return sentence_count

    # # TLE
    # def wordsTyping(self, sentence, rows: int, cols: int) -> int:
    #     word_ptr = -1
    #     sentence_count = 0
    #
    #     def next_word():
    #         if word_ptr == len(sentence) - 1:
    #             return sentence[0]
    #         return sentence[word_ptr + 1]
    #
    #     def word_chosen(word_ptr, sentence_count):
    #         if word_ptr == len(sentence) - 1:
    #             word_ptr = -1
    #         if word_ptr == len(sentence) - 2:
    #             sentence_count += 1
    #         word_ptr += 1
    #         return word_ptr, sentence_count
    #
    #     for _ in range(rows):
    #         space_available = cols
    #         while space_available >= len(next_word()):
    #             space_available -= (len(next_word()) + 1)
    #             word_ptr, sentence_count = word_chosen(word_ptr, sentence_count)
    #
    #     return sentence_count


if __name__ == '__main__':
    print(Solution().wordsTyping(["try", "to", "be", "better"], 10000, 9001))
