class Solution:
    def partition(self, s: str):
        def isPalindrom(s):
            if not s:
                return False
            for i in range(len(s) // 2 + 1):
                if s[i] != s[len(s) - 1 - i]:
                    return False
            return True

        ans = []
        def dfs(index, pending, stack):
            if index == len(s):
                if isPalindrom(pending):
                    ans.append(stack + [pending])
                return
            if isPalindrom(pending):
                dfs(index + 1, s[index], stack + [pending])
            dfs(index + 1, pending + s[index], stack)

        dfs(0, "", [])
        return ans




if __name__ == '__main__':
    print(Solution().partition(s = "aab"))
    print(Solution().partition(s = "a"))
