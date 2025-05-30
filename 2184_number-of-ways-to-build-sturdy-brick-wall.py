import functools


class Solution:
    """
    Accepted : 24%
    """
    def buildWall(self, height: int, width: int, bricks) -> int:
        MOD = 10 ** 9 + 7
        permutations = []

        def populate_permutation(sum, stack):
            if sum > width:
                return
            if sum == width:
                for i in range(1, len(stack)):
                    stack[i] = stack[i] + stack[i - 1]
                permutations.append(set(stack[:-1]))
                return
            for i in bricks:
                populate_permutation(sum + i, stack + [i])

        populate_permutation(0, [])

        def compare(i, j):
            for a in permutations[i]:
                if a in permutations[j]:
                    return False
            return True

        permutation_connection_map = [set() for _ in range(len(permutations))]
        # There was a problem with creating connection. The rest of the logic and the rest of the intuition, idea, code all was well.
        for i in range(len(permutations)):
            for j in range(len(permutations)):
                if compare(i, j):
                    permutation_connection_map[i].add(j)
                    permutation_connection_map[j].add(i)

        @functools.lru_cache(None)
        def dfs(index, level):
            if level == height:
                return 1

            ans = 0
            for connections in permutation_connection_map[index]:
            # for next_level_permutation_index in range(len(permutations)):
            #     if compare(next_level_permutation_index, index):
                ans += dfs(connections, level + 1)
                ans %= MOD
            return ans

        total_count = 0
        for i in range(len(permutations)):
            total_count += dfs(i, 1)
            total_count %= MOD

        return total_count % MOD


if __name__ == '__main__':
    print(Solution().buildWall(height = 2, width = 3, bricks = [1,2]))
    print(Solution().buildWall(height = 1, width = 1, bricks = [5]))
    print(Solution().buildWall(height = 3, width = 4, bricks = [1,2,3]))
    print(Solution().buildWall(76, 9, [6,3,5,1,9]))
