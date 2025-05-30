class Solution:
    def findShortestWay(self, maze, ball, hole) -> str:
        rows, cols = len(maze), len(maze[0])
        dp = [[float('inf')] * cols for _ in range(rows)]

        def end_position(ball_position, direction):
            directions = {"u": (-1, 0), "d": (1, 0), "l": (0, -1), "r": (0, 1)}
            dr, dc = directions[direction]
            r, c = ball_position
            distance = 0

            while 0 <= r + dr < rows and 0 <= c + dc < cols and maze[r + dr][c + dc] == 0:
                r, c = r + dr, c + dc
                distance += 1
                if [r, c] == hole:
                    break
            return distance, (r, c)

        holes = []
        queue = [(0, tuple(ball), "")]
        while queue:
            distance, (r, c), moves = queue.pop(0)
            if [r, c] == hole:
                holes.append((distance, moves))
                dp[r][c] = min(dp[r][c], distance)
                continue

            for d in ["u", "d", "l", "r"]:
                delta, (end_r, end_c) = end_position([r, c], d)
                if delta == 0:
                    continue
                if distance + delta <= dp[end_r][end_c]:
                    dp[end_r][end_c] = distance + delta
                    queue.append((distance + delta, (end_r, end_c), moves + d))

        holes.sort()

        return holes[0][1] if holes else "impossible"


if __name__ == '__main__':
    print(Solution().findShortestWay(
        maze=[[0, 0, 0, 0, 0], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0], [0, 1, 0, 0, 1], [0, 1, 0, 0, 0]], ball=[4, 3],
        hole=[0, 1]))
    print(Solution().findShortestWay(maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], ball = [4,3], hole = [3,0]))
    print(Solution().findShortestWay(maze = [[0,0,0,0,0,0,0],[0,0,1,0,0,1,0],[0,0,0,0,1,0,0],[0,0,0,0,0,0,1]], ball = [0,4], hole = [3,5]))
