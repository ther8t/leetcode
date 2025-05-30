class Solution:
    def sumSubarrayMins(self, arr) -> int:
        n = len(arr)
        nse = [n] * n
        ps = [-1] * n

        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                nse[stack.pop()] = i
            stack.append(i)

        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                ps[stack.pop()] = i
            stack.append(i)


        ans = 0
        MOD = 10 ** 9 + 7
        for i in range(n):
            left, right = i - ps[i] - 1, nse[i] - i - 1
            ans = (ans + arr[i] * (left + right + left * right + 1)) % MOD

        return ans


if __name__ == '__main__':
    print(Solution().sumSubarrayMins(arr = [3,1,2,4]))
    print(Solution().sumSubarrayMins(arr = [11,81,94,43,3]))
