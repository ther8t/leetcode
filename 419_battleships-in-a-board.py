class Solution:
    def countBattleships(self, board) -> int:
        rows, cols = len(board), len(board[0])
        visited = set()
        battleship = 0

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "." or (r, c) in visited:
                    continue
                battleship += 1
                queue = [(r, c)]

                while queue:
                    popped = queue.pop(0)
                    visited.add(popped)
                    for nr, nc in [(popped[0], popped[1] + 1), (popped[0] + 1, popped[1])]:
                        if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'X':
                            queue.append((nr, nc))

        return battleship


if __name__ == '__main__':
    print(Solution().countBattleships(board = [["."]]))
    print(Solution().countBattleships(board = [["X","X","X","X"],[".",".",".","X"],[".",".",".","X"]]))
