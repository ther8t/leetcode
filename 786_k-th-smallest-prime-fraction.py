class Solution:
    """
    Attempt: Fired
    Wrong Answer: Didn't even run.
    """
    def kthSmallestPrimeFraction(self, arr, k: int):
        n = len(arr)

        def dfs(index):
            if index == n - 1:
                return []
            a = []
            greater = n - 1
            for i in range(n - 1, index, -1):
                if arr[index] / arr[i] > arr[index + 1] / arr[n - 1]:
                    break
                a.append((index, i))
                greater = i

            a += dfs(index + 1)
            for i in range(greater - 1, index, -1):
                a.append((index, i))

            return a

        a = dfs(0)
        print(a)
        return [0, 0]


    def kthSmallestPrimeFraction(self, arr, k: int):
        n = len(arr)

        def check():
            a = []
            highest = (0, n - 1)
            for i in range(n):
                for j in range(n - 1, -1, -1):
                    if arr[i] / arr[j] > mid:
                        break
                    a.append((arr[i], arr[j]))
                    if arr[i] / arr[j] > highest[0] / highest[1]:
                        highest = (arr[i], arr[j])

            return len(a), highest

        lo, hi = 0, 1
        while lo < hi:
            mid = (lo + hi) / 2
            a, highest = check()
            if a > k:
                hi = mid
            if a < k:
                lo = mid
            if a == k:
                return highest

        return -1




if __name__ == '__main__':
    print(Solution().kthSmallestPrimeFraction(arr = [1,2,3,5], k = 3))
    print(Solution().kthSmallestPrimeFraction(arr = [1,7], k = 1))
