class Solution:
    def reorderSpaces(self, text: str) -> str:
        split = text.split()
        words = []
        non_space_char_count = 0
        for s in split:
            if len(s) > 0:
                words.append(s)
                non_space_char_count += len(s)

        space_count = len(text) - non_space_char_count

        if len(words) == 1:
            return words[0] + ("".join([" "]*space_count))

        out = ""
        space_divide = space_count//(len(words) - 1)
        for i, word in enumerate(words):
            out += word
            if i != len(words) - 1:
                out += ("".join([" "]*space_divide))
                space_count -= space_divide

        out += ("".join([" "]*space_count))

        return out


if __name__ == '__main__':
    print(Solution().reorderSpaces(text = "a"))
