class Solution:
    def asteroidCollision(self, asteroids):
        n = len(asteroids)
        stack = []
        for i in range(n):
            doomed = False
            while stack and asteroids[i] < 0 and asteroids[stack[-1]] > 0 and abs(asteroids[stack[-1]]) <= abs(asteroids[i]):
                last_popped = stack.pop()
                if abs(asteroids[last_popped]) == abs(asteroids[i]):
                    doomed = True
                    break
            if asteroids[i] < 0 and ((stack and asteroids[stack[-1]] >= -asteroids[i]) or doomed):
                continue
            stack.append(i)

        out = [asteroids[stack[i]] for i in range(len(stack))]
        return out


    """
    Revision 2:
    I thought about two monotonic stacks on either side of the array. The code works but after a lot of edge cases which I could only accomplish after running the code and finding the edge cases and then debugging them.
    The code gets accepted but because of the two passes, by 5%.
    The above is a far simpler solution to understand and implement. It's more straightforward than the solution proposed below.
    """
    def asteroidCollision(self, asteroids):
        n = len(asteroids)
        death_by = [None] * n
        stack = []
        for i in range(n):
            if asteroids[i] > 0:
                stack.append(i)
                continue
            doomed = False
            while stack and abs(asteroids[stack[-1]]) <= abs(asteroids[i]):
                if asteroids[stack[-1]] > 0:
                    popped = stack.pop()
                    death_by[popped] = i
                    if stack and abs(asteroids[popped]) == abs(asteroids[i]):
                        doomed = True
                        break
                else:
                    stack.pop()
            if not doomed:
                stack.append(i)

        stack = []
        for i in range(n - 1, -1, -1):
            if asteroids[i] < 0:
                stack.append(i)
                continue
            doomed = False
            while stack and abs(asteroids[stack[-1]]) <= abs(asteroids[i]):
                if asteroids[stack[-1]] < 0:
                    popped = stack.pop()
                    death_by[popped] = i
                    if stack and abs(asteroids[popped]) == abs(asteroids[i]):
                        doomed = True
                        break
                else:
                    stack.pop()
            if not doomed:
                stack.append(i)

        out = [asteroids[i] for i in range(n) if death_by[i] == None]

        return out




if __name__ == '__main__':
    print(Solution().asteroidCollision(asteroids=[5,10,-5]))
    print(Solution().asteroidCollision(asteroids=[8,-8]))
    print(Solution().asteroidCollision(asteroids=[10,2,-5]))
    print(Solution().asteroidCollision([-2,-2,-2,-2]))
    print(Solution().asteroidCollision([-2,1,-1,-1]))
    print(Solution().asteroidCollision([-2,1,2,-2]))
    print(Solution().asteroidCollision([1,1,-1,-1]))
    print(Solution().asteroidCollision([1,2,-2,-1]))
    a = [1, 2, 3, 4, 5]
    a[2:2] = [9, 8, 7, 6]
    print(a)
