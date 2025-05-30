import collections


class Solution:
    def getSum(self, a: int, b: int) -> int:
        ans = 0
        carry = 0
        base = 0
        while a or b or carry:
            a_remainder, b_remainder = a % 2, b % 2
            c = collections.Counter([a_remainder, b_remainder, carry])
            if c[1] == 1 or c[1] == 3:
                ans = (2 ** (base)) | ans
            if c[1] == 2 or c[1] == 3:
                carry = 1
            else:
                carry = 0
            base += 1
            a //= 2
            b //= 2

        return ans





if __name__ == '__main__':
    print(Solution().getSum(2, 3))
    print(Solution().getSum(34, 57))
