import collections


"""
Accepted 30%
"""
class SnakeGame:
    def __init__(self, width: int, height: int, food):
        self.width = width
        self.height = height
        self.food = food
        self.snake = [(0, 0)]
        self.current_food_index = 0

    def move(self, direction: str) -> int:
        dir = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
        snake_head = self.snake[-1]
        snake_head_updated = (snake_head[0] + dir[direction][0], snake_head[1] + dir[direction][1])
        if 0 <= snake_head_updated[0] < self.height and 0 <= snake_head_updated[1] < self.width:
            if self.current_food_index < len(self.food) and snake_head_updated == tuple(self.food[self.current_food_index]):
                self.snake.append(snake_head_updated)
                self.current_food_index += 1
                return self.current_food_index
            else:
                self.snake.pop(0)
                if snake_head_updated in self.snake:
                    return -1
                self.snake.append(snake_head_updated)
                return self.current_food_index
        return -1


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)


if __name__ == '__main__':
    s = SnakeGame(3,3,[[2,0],[0,0],[0,2],[0,1],[2,2],[0,1]])
    print(s.move("D"))
    print(s.move("D"))
    print(s.move("R"))
    print(s.move("U"))
    print(s.move("U"))
    print(s.move("L"))
    print(s.move("D"))
    print(s.move("R"))
    print(s.move("R"))
    print(s.move("U"))
    print(s.move("L"))
    print(s.move("L"))
    print(s.move("D"))
    print(s.move("R"))
    print(s.move("U"))
