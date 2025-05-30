class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        configuration = [0, 0, 0]

        for i in instructions:
            if i == "G":
                posx, posy, d = configuration
                configuration = [posx + directions[d][0], posy + directions[d][1], d]
            elif i == "L":
                configuration[2] = (configuration[2] - 1) % 4
            elif i == "R":
                configuration[2] = (configuration[2] + 1) % 4

        x, y, d = configuration
        return (x == 0 and y == 0) or d != 0

    """
    This is a slightly easier method to understand this.
    """
    def isRobotBounded(self, instructions: str) -> bool:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        configuration = [0, 0, 0]

        for _ in range(4):
            for i in instructions:
                if i == "G":
                    posx, posy, d = configuration
                    configuration = [posx + directions[d][0], posy + directions[d][1], d]
                elif i == "L":
                    configuration[2] = (configuration[2] - 1) % 4
                elif i == "R":
                    configuration[2] = (configuration[2] + 1) % 4
            if configuration == [0, 0, 0]:
                return True

        return False


if __name__ == '__main__':
    print(Solution().isRobotBounded(instructions = "GLGRGR"))
