class Solution:
    def expressiveWords(self, s: str, words) -> int:
        stretchy_counter = 0
        for word in words:
            ptr_w = ptr_s = 0
            stretchy = True
            while ptr_w < len(word) and ptr_s < len(s):
                if word[ptr_w] != s[ptr_s]:
                    stretchy = False
                    break
                word_group_counter = 1
                while ptr_w + 1 < len(word) and word[ptr_w + 1] == word[ptr_w]:
                    ptr_w += 1
                    word_group_counter += 1
                s_group_counter = 1
                while ptr_s + 1 < len(s) and s[ptr_s + 1] == word[ptr_w]:
                    ptr_s += 1
                    s_group_counter += 1
                if word_group_counter > s_group_counter or (word_group_counter < s_group_counter < 3):
                    stretchy = False
                    break
                ptr_w += 1
                ptr_s += 1
            if stretchy and ptr_s == len(s) and ptr_w == len(word):
                stretchy_counter += 1
        return stretchy_counter


if __name__ == '__main__':
    print(Solution().expressiveWords(s = "zzzzzyyyyy", words = ["zzyy","zy","zyy"]))
