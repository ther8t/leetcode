class Solution:
    def minimumHealth(self, damage, armor: int) -> int:
        max_damage = max(damage)
        return sum(damage) - max_damage + (max_damage - min(max_damage, armor)) + 1


if __name__ == '__main__':
    print(Solution().minimumHealth(damage = [3,3,3], armor = 0))
