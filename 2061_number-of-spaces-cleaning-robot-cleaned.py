class Solution:
    def numberOfCleanRooms(self, room) -> int:
        rows, cols = len(room), len(room[0])
        cleaned = set()
        visited = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        r, c, current_direction = 0, 0, 0
        visited.add((r, c, current_direction))
        cleaned.add((r, c))
        while True:
            nr, nc = r + directions[current_direction][0], c + directions[current_direction][1]
            if (nr, nc, current_direction) in visited:
                break
            if 0 <= nr < rows and 0 <= nc < cols and room[nr][nc] == 0:
                cleaned.add((nr, nc))
                visited.add((nr, nc, current_direction))
                r, c = nr, nc
            else:
                visited.add((nr, nc, current_direction))
                current_direction = (current_direction + 1) % 4

        return len(cleaned)


if __name__ == '__main__':
    print(Solution().numberOfCleanRooms(room = [[0,0,0],[1,1,0],[0,0,0]]))
    print(Solution().numberOfCleanRooms(room = [[0,1,0],[1,0,0],[0,0,0]]))




