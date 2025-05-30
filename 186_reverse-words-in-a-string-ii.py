class Solution:
    def reverseWords(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(left, right):
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        reverse(0, len(s) - 1)
        start = 0
        for i in range(len(s) + 1):
            if i == len(s) or s[i] == " ":
                reverse(start, i - 1)
                start = i + 1




if __name__ == '__main__':
    Solution().reverseWords(s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"])
    Solution().reverseWords(s = ["a"])
