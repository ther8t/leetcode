class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int):
        ans = []
        visited = set()
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def move(r, c, direction, force):
            if len(ans) == rows * cols:
                return
            if 0 <= r < rows and 0 <= c < cols:
                ans.append([r, c])
                visited.add((r, c))
            if (r + d[force][0], c + d[force][1]) not in visited:
                move(r + d[force][0], c + d[force][1], force, (force + 1) % 4)
            else:
                move(r + d[direction][0], c + d[direction][1], direction, force)

        ans.append([rStart, cStart])
        visited.add((rStart, cStart))
        move(rStart, cStart + 1, 0, 1)
        return ans




































    """
    Attempt #2
    
    """
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int):
        ans = []
        visited = set()
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def move(r, c, direction, force):
            if len(ans) == rows * cols:
                return
            if 0 <= r < rows and 0 <= c < cols:
                ans.append([r, c])
            visited.add((r, c))
            if (r + d[force][0], c + d[force][1]) not in visited:
                new_direction = force
                new_force = (force + 1) % 4
                move(r + d[force][0], c + d[force][1], new_direction, new_force)
            else:
                move(r + d[direction][0], c + d[direction][1], direction, force)

        ans.append([rStart, cStart])
        visited.add((rStart, cStart))
        move(rStart, cStart + 1, 1, 2)

        return ans


if __name__ == '__main__':
    print(Solution().spiralMatrixIII(rows = 1, cols = 4, rStart = 0, cStart = 0))
    print(Solution().spiralMatrixIII(rows = 5, cols = 6, rStart = 1, cStart = 4))
