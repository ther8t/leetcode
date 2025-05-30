import heapq


class Solution:
    def slidingPuzzle(self, board) -> int:
        target = ((1, 2, 3), (4, 5, 0))
        zero_index = -1
        for r in [0, 1]:
            for c in range(3):
                if board[r][c] == 0:
                    zero_index = (r, c)

        queue = [(0, zero_index, (tuple(board[0]), tuple(board[1])))]
        visited = set()

        while queue:
            moves, zero_index, current_board = heapq.heappop(queue)
            r, c = zero_index
            if current_board == target:
                return moves

            current_board = [list(current_board[0]), list(current_board[1])]

            for dr, dc in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < 2 and 0 <= nc < 3:
                    current_board[r][c], current_board[nr][nc] = current_board[nr][nc], current_board[r][c]
                    current_board_tuple = (tuple(current_board[0]), tuple(current_board[1]))
                    if current_board_tuple not in visited:
                        if current_board_tuple == target:
                            return moves + 1
                        visited.add(current_board_tuple)
                        heapq.heappush(queue, (moves + 1, (nr, nc), current_board_tuple))
                    current_board[r][c], current_board[nr][nc] = current_board[nr][nc], current_board[r][c]

        return -1


if __name__ == '__main__':
    print(Solution().slidingPuzzle(board = [[1,2,3],[4,5,0]]))
    print(Solution().slidingPuzzle(board = [[1,2,3],[5,4,0]]))
    print(Solution().slidingPuzzle(board = [[4,1,2],[5,0,3]]))
