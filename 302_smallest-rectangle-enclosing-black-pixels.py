class Solution:
    def minArea(self, image, x: int, y: int) -> int:
        r, c = x, y
        rows, cols = len(image), len(image[0])
        minx = float('inf')
        miny = float('inf')
        maxx = -float('inf')
        maxy = -float('inf')

        visited = [[False] * cols for _ in range(rows)]
        queue = [(r, c)]

        while queue:
            popped = queue.pop(0)
            r, c = popped[0], popped[1]
            visited[popped[0]][popped[1]] = True

            minx = min(minx, popped[0])
            miny = min(miny, popped[1])
            maxx = max(maxx, popped[0])
            maxy = max(maxy, popped[1])

            for nr, nc in [(r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)]:
                if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == "1" and not visited[nr][nc]:
                    visited[nr][nc] = True
                    queue.append((nr, nc))

        return (maxy - miny + 1) * (maxx - minx + 1)


if __name__ == '__main__':
    print(Solution().minArea(image = [["1"]], x = 0, y = 0))
