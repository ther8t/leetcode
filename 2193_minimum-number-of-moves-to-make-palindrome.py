class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        def swaps(s):
            if not s or len(s) == 1:
                return 0
            n = len(s)
            if s[0] == s[n - 1]:
                return swaps(s[1: -1])
            ptr = n - 1
            while s[ptr] != s[0]:
                ptr -= 1
            if ptr == 0:
                swaps_needed = len(s) // 2
            else:
                swaps_needed = n - 1 - ptr
            return swaps(s[1: ptr] + s[ptr + 1:]) + swaps_needed

        return swaps(s)




    # # TLE
    # def minMovesToMakePalindrome(self, s: str) -> int:
    #     queue = [(list(s), 0)]
    #     visited = set()
    #     visited.add(tuple(s))
    #
    #     def is_palindrom(word):
    #         for i in range(len(word)//2):
    #             if word[i] != word[-1 -i]:
    #                 return False
    #         return True
    #
    #     while queue:
    #         (current_word, distance) = queue.pop(0)
    #
    #         for i in range(len(current_word) - 1):
    #             swap_word = current_word[::]
    #             swap_word[i], swap_word[i + 1] = swap_word[i + 1], swap_word[i]
    #             if is_palindrom(swap_word):
    #                 return distance + 1
    #             if tuple(swap_word) not in visited:
    #                 visited.add(tuple(swap_word))
    #                 queue.append((swap_word, distance + 1))
    #
    #     return -1


if __name__ == '__main__':
    # print(Solution().minMovesToMakePalindrome("aabb"))
    # print(Solution().minMovesToMakePalindrome("letelt"))
    # print(Solution().minMovesToMakePalindrome("eqvvhtcsaaqtqesvvqch"))
    print(Solution().minMovesToMakePalindrome("skwhhaaunskegmdtutlgtteunmuuludii"))
