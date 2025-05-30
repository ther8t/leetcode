class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n = len(s)
        ptr1, ptr2, ptr3 = 0, 0, 0
        count = 0
        while ptr2 < n and s[ptr2] == s[ptr1]:
            ptr2 += 1

        while ptr1 < n and ptr2 < n and ptr3 < n:
            ptr3 = ptr2
            while ptr3 < n and s[ptr3] == s[ptr2]:
                ptr3 += 1

            count += min((ptr2 - ptr1), (ptr3 - ptr2))
            ptr1 = ptr2
            ptr2 = ptr3

        return count




    # # Wrong Answer
    # def countBinarySubstrings(self, s: str) -> int:
    #     zeros_stack = []
    #     ones_stack = []
    #
    #     count = 0
    #     for char in s:
    #         if char == "0":
    #             if ones_stack:
    #                 ones_stack.pop()
    #                 count += 1
    #             zeros_stack.append("0")
    #         else:
    #             if zeros_stack:
    #                 zeros_stack.pop()
    #                 count += 1
    #             ones_stack.append("1")
    #
    #     return count


if __name__ == '__main__':
    print(Solution().countBinarySubstrings(s = "00110011"))
    print(Solution().countBinarySubstrings(s = "10101"))
