class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if start == target:
            return True
        n = len(start)
        if start.replace("_", "") != target.replace("_", ""):
            return False
        start_char_position, target_char_position = 0, 0
        while start_char_position < n and target_char_position < n:
            while start_char_position < n and start[start_char_position] == "_":
                start_char_position += 1
            while target_char_position < n and target[target_char_position] == "_":
                target_char_position += 1
            if start_char_position < n and target_char_position < n and ((start[start_char_position] == 'L' and start_char_position < target_char_position) or (start[start_char_position] == 'R' and start_char_position > target_char_position)):
                return False
            start_char_position += 1
            target_char_position += 1
        return True


if __name__ == '__main__':
    print(Solution().canChange(start = "_L__R__R_", target = "L______RR"))
    print(Solution().canChange(start = "R_L_", target = "__LR"))
    print(Solution().canChange(start = "_R", target = "R_"))
    print(Solution().canChange("__", "__"))
    print(Solution().canChange("___L___", "_L_____"))
