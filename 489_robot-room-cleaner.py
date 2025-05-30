# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
class Robot:
    def move(self):
        """
        Returns true if the cell in front is open and robot moves into the cell.
        Returns false if the cell in front is blocked and robot stays in the current cell.
        :rtype bool
        """

    def turnLeft(self):
        """
        Robot will stay in the same cell after calling turnLeft/turnRight.
        Each turn will be 90 degrees.
        :rtype void
        """

    def turnRight(self):
        """
        Robot will stay in the same cell after calling turnLeft/turnRight.
        Each turn will be 90 degrees.
        :rtype void
        """

    def clean(self):
        """
        Clean the current cell.
        :rtype void
        """


class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """

        def make_move(move):
            if move == "m":
                return robot.move()
            if move == "c":
                robot.clean()
                return True
            if move == "l":
                robot.turnLeft()
                return True
            if move == "r":
                robot.turnRight()
                return True

        def align(target):
            nonlocal current_direction
            target_direction = (target[0] - current_location[0], target[1] - current_location[1])
            target_direction_index = directions.index(target_direction)

            while target_direction_index != current_direction:
                if current_direction < target_direction_index:
                    make_move("l")
                    current_direction += 1
                    current_direction %= 4
                else:
                    make_move("r")
                    current_direction -= 1
                    current_direction %= 4

            return True

        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        current_location = (0, 0)
        current_direction = 0
        cleaned = set()
        visited = set()
        visited.add(current_location)
        stack = [current_location]

        while stack:
            found = False
            for d in directions:
                target = (current_location[0] + d[0], current_location[1] + d[1])
                if target not in cleaned and target not in visited:
                    align(target)
                    can_move = make_move("m")
                    if can_move:
                        current_location = target
                        stack.append(target)
                        visited.add(target)
                        found = True
                        break

            if not found:
                make_move("c")
                popped = stack.pop()
                visited.remove(popped)
                cleaned.add(popped)

                if stack:
                    target = stack[-1]
                    align(target)
                    make_move("m")
                    current_location = target


if __name__ == '__main__':
    r = Robot()
    print(Solution().cleanRoom(r))
