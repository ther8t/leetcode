import collections


class Solution:
    def placeWordInCrossword(self, board, word: str) -> bool:
        def is_match(cross_word, word):
            if len(cross_word) != len(word):
                return False
            are_match = True
            for cw, w in zip(cross_word, word):
                if cw != " " and cw != w:
                    are_match = False

            if are_match:
                return True

            are_match = True
            for cw, w in zip(reversed(cross_word), word):
                if cw != " " and cw != w:
                    are_match = False

            return are_match

        rows, cols = len(board), len(board[0])
        c = 0
        while c < cols:
            ptr1, ptr2 = 0, 0
            while ptr1 < rows and ptr2 < rows:
                while ptr1 < rows and board[ptr1][c] == "#":
                    ptr1 += 1
                ptr2 = ptr1
                entry = ""
                while ptr2 < rows and board[ptr2][c] != "#":
                    entry += board[ptr2][c]
                    ptr2 += 1
                if is_match(entry, word):
                    return True
                ptr1 = ptr2
            c += 1

        r = 0
        while r < rows:
            ptr1, ptr2 = 0, 0
            while ptr1 < cols and ptr2 < cols:
                while ptr1 < cols and board[r][ptr1] == "#":
                    ptr1 += 1
                ptr2 = ptr1
                entry = ""
                while ptr2 < cols and board[r][ptr2] != "#":
                    entry += board[r][ptr2]
                    ptr2 += 1
                if is_match(entry, word):
                    return True
                ptr1 = ptr2
            r += 1

        return False

if __name__ == '__main__':
    print(Solution().placeWordInCrossword(board = [["#", " ", "#"], [" ", " ", "#"], ["#", " ", "c"]], word = "ca"))

