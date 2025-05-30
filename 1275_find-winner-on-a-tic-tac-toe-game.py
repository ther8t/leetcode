class Solution:
    def tictactoe(self, moves) -> str:
        rows, cols = [0] * 3, [0] * 3
        diagonal, antidiagonal = 0, 0

        for index, (r, c) in enumerate(moves):
            player = "A" if index % 2 == 0 else "B"
            score = 1 if index % 2 == 0 else -1
            rows[r] += score
            cols[c] += score
            if r == 1 and c == 1:
                diagonal += score
                antidiagonal += score
            elif r == c:
                antidiagonal += score
            elif r + c == 2:
                diagonal += score
            if any(abs(i) == 3 for i in [rows[r], cols[c], antidiagonal, diagonal]):
                return player

        return "Draw" if len(moves) == 9 else "Pending"


if __name__ == '__main__':
    print(Solution().tictactoe(moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]))
    print(Solution().tictactoe(moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]))
    print(Solution().tictactoe(moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]))

