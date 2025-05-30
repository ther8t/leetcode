class Solution:
    """
    Revision 2:
    This could be done by regex as well. But the difficult part would be balancing the brackets.
    """
    def decodeString(self, s: str) -> str:
        k_ptr_start = 0
        while k_ptr_start < len(s) and not ord('0') <= ord(s[k_ptr_start]) <= ord('9'):
            k_ptr_start += 1

        k_ptr_end = k_ptr_start
        while k_ptr_end < len(s) and ord('0') <= ord(s[k_ptr_end]) <= ord('9'):
            k_ptr_end += 1

        bracket_start = k_ptr_end
        bracket_end = bracket_start + 1
        bracket_count = 1
        while bracket_end < len(s) and bracket_count != 0:
            if s[bracket_end] == "[":
                bracket_count += 1
            elif s[bracket_end] == "]":
                bracket_count -= 1
            bracket_end += 1

        if k_ptr_start < len(s):
            repeating_substring = self.decodeString(s[bracket_start + 1:bracket_end - 1])
            decoded = ""
            for i in range(int(s[k_ptr_start:k_ptr_end])):
                decoded += repeating_substring
            return s[0:k_ptr_start] + decoded + self.decodeString(s[bracket_end:])
        else:
            return s


if __name__ == '__main__':
    print(Solution().decodeString(s = "2[abc]3[cd]ef"))
