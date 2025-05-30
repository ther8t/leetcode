class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        def get_index(char):
            position = ord(char) - ord('a')
            return position // 5, position % 5

        start_pos = [0, 0]
        move_string = ""
        for index, char in enumerate(target):
            target_pos = get_index(char)
            if char == 'z':
                while start_pos[1] != target_pos[1]:
                    if start_pos[1] < target_pos[1]:
                        start_pos[1] += 1
                        move_string += "R"
                    else:
                        start_pos[1] -= 1
                        move_string += "L"

                while start_pos[0] != target_pos[0]:
                    if start_pos[0] < target_pos[0]:
                        start_pos[0] += 1
                        move_string += "D"
                    else:
                        start_pos[0] -= 1
                        move_string += "U"
            else:
                while start_pos[0] != target_pos[0]:
                    if start_pos[0] < target_pos[0]:
                        start_pos[0] += 1
                        move_string += "D"
                    else:
                        start_pos[0] -= 1
                        move_string += "U"

                while start_pos[1] != target_pos[1]:
                    if start_pos[1] < target_pos[1]:
                        start_pos[1] += 1
                        move_string += "R"
                    else:
                        start_pos[1] -= 1
                        move_string += "L"

            move_string += "!"
        return move_string


if __name__ == '__main__':
    print(Solution().alphabetBoardPath("zozozz"))
