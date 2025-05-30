class Solution:
    def visibleMountains(self, peaks) -> int:
        peaks.sort(key=lambda x: x[1])

        def slope(upper, lower):
            if upper[0] == lower[0]:
                return float('inf')
            return (upper[1] - lower[1]) / (upper[0] - lower[0])

        ptr = 0
        ans = 0
        while ptr < len(peaks):
            is_visible = True
            for i in range(ptr + 1, len(peaks)):
                s = slope(peaks[i], peaks[ptr])
                if peaks[i] == peaks[ptr] or s >= 1 or s <= -1:
                    is_visible = False
                    break
            if is_visible:
                ans += 1
            while ptr + 1 < len(peaks) and peaks[ptr] == peaks[ptr + 1]:
                ptr += 1
            ptr += 1

        return ans


if __name__ == '__main__':
    print(Solution().visibleMountains(peaks = [[2,2],[6,3],[5,4]]))
    print(Solution().visibleMountains(peaks = [[1,3],[1,3]]))
    print(Solution().visibleMountains([[3,19],[39,7],[15,39],[23,13],[8,28],[2,26],[38,15],[38,7],[16,17]]))
