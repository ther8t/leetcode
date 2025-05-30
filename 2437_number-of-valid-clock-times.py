class Solution:
    def countTime(self, time: str) -> int:
        time = list(time)
        ans = 1

        def getPermutations(time, index):
            if index == 4:
                return 10
            if index == 3:
                return 6
            if index == 1:
                if time[0] == '0' or time[0] == '1':
                    return 10
                if time[0] == '2':
                    return 4
                if time[0] == "?":
                    return 24
            if index == 0:
                if time[1] == "?":
                    return 1
                if 4 <= int(time[1]) <= 9:
                    return 2
                else:
                    return 3

        a = [1, 1, 1, 1, 1]
        for i in [0, 1, 3, 4]:
            if time[i] != "?":
                continue
            a[i] = getPermutations(time, i)

        for i in [0, 1, 3, 4]:
            ans *= a[i]

        return ans


if __name__ == '__main__':
    print(Solution().countTime("?5:00"))
    print(Solution().countTime("??:??"))
    print(Solution().countTime("0?:0?"))
