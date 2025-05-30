import collections


class Solution:
    def exist(self, board, word: str) -> bool:
        rows, cols = len(board), len(board[0])
        counter_word = collections.Counter(word)
        counter_board = collections.Counter()
        for r in range(rows):
            for c in range(cols):
                counter_board[board[r][c]] += 1

        for char in counter_word.keys():
            if char not in counter_board or counter_board[char] < counter_word[char]:
                return False

        def backtrack(r, c, i):
            if i == len(word) - 1:
                return True
            for nr, nc in [(r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)]:
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and board[nr][nc] == word[i + 1]:
                    visited.add((nr, nc))
                    if backtrack(nr, nc, i + 1):
                        return True
                    visited.remove((nr, nc))

            return False

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    visited = set()
                    visited.add((r, c))
                    if backtrack(r, c, 0):
                        return True

        return False


if __name__ == '__main__':
    print(Solution().exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"))
    print(Solution().exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"))
    print(Solution().exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"))
    print(Solution().exist([["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"]], "AAAAAAAAAAAAAAB"))
