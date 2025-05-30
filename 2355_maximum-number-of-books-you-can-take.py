class Solution:
    # Accepted : 41%
    def maximumBooks(self, books) -> int:
        n = len(books)
        stack = []
        terminal_index = [-1] * n
        for i in range(n - 1, -1, -1):
            while stack and books[i] < books[stack[-1]] - (stack[-1] - i):
                terminal_index[stack.pop()] = i
            stack.append(i)

        max_books = -float('inf')
        dp = [0] * n
        for i in range(n):
            j = terminal_index[i]
            if j == -1:
                l = books[i]
                a = max(l - i, 1)
                num = min(i + 1, books[i])
                dp[i] = num * (a + l) // 2
            else:
                l = books[i]
                dp[i] = dp[j] + (i - j) * (2 * l - (i - j - 1)) // 2
            max_books = max(max_books, dp[i])

        return max_books


if __name__ == '__main__':
    print(Solution().maximumBooks(books = [8,5,2,7,9])) #19
    print(Solution().maximumBooks(books = [7,0,3,4,5])) #12
    print(Solution().maximumBooks(books = [8,2,3,7,3,4,0,1,4,3])) #13
    print(Solution().maximumBooks([0,5,5,5])) #12
