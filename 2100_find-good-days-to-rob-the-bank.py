class Solution:
    def goodDaysToRobBank(self, security, time: int):
        n = len(security)
        next_decreasing = [n] * n
        stack = []
        for i in range(n):
            if stack and security[i] < security[stack[-1]]:
                while stack:
                    next_decreasing[stack.pop()] = i
            stack.append(i)

        prev_decreasing = [-1] * n
        stack = []
        for i in range(n - 1, -1, -1):
            if stack and security[i] < security[stack[-1]]:
                while stack:
                    prev_decreasing[stack.pop()] = i
            stack.append(i)

        ans = []
        for i in range(n):
            if i - prev_decreasing[i] > time and next_decreasing[i] - i > time:
                ans.append(i)
        return ans


if __name__ == '__main__':
    print(Solution().goodDaysToRobBank(security = [5,3,3,3,5,6,2], time = 2))
    print(Solution().goodDaysToRobBank(security = [1,1,1,1,1], time = 0))
    print(Solution().goodDaysToRobBank(security = [1,2,3,4,5,6], time = 2))
    print(Solution().goodDaysToRobBank(security = [1,2,3,4,5,6], time = 1))
