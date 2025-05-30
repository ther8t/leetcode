class Solution:
    """
    What an idiot am I. This question should boost my confidence if nothing else. I was right all along. I had figured out two ways to solve this question and yet I was.
    I am so low on confidence today that I am unable to see that once the solution is reached, it ends there. I was still searching for a minimum.
    This is a greedy kind of a problem.
    """
    def crackSafe(self, n: int, k: int) -> str:
        visited = set()

        def crack(s):
            if len(visited) == pow(k, n):
                return s

            prev = s[len(s) - n + 1:]
            for i in range(k):
                if prev + str(i) not in visited:
                    visited.add(prev + str(i))
                    done = crack(s + str(i))
                    if done:
                        return done
                    visited.remove(prev + str(i))

        visited.add("0" * n)
        ans = crack("0" * n)
        return ans


if __name__ == '__main__':
    print(Solution().crackSafe(n = 1, k = 2))
    print(Solution().crackSafe(n = 2, k = 2))
    print(Solution().crackSafe(n = 2, k = 10))
