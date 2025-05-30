class Solution:
    def judgePoint24(self, cards) -> bool:
        if len(cards) == 1:
            return True if float('%.1f' % cards[0]) == 24.0 else False

        for i in range(len(cards) - 1):
            for j in range(i + 1, len(cards)):
                a, b = cards[i], cards[j]
                temp_cards = cards[::]
                temp_cards.remove(a)
                temp_cards.remove(b)
                if self.judgePoint24([a + b] + temp_cards) or self.judgePoint24(
                        [a * b] + temp_cards) or self.judgePoint24([a - b] + temp_cards) or self.judgePoint24(
                    [b - a] + temp_cards) or (b != 0 and self.judgePoint24([a / b] + temp_cards)) or (
                        a != 0 and self.judgePoint24(
                    [b / a] + temp_cards)):
                    return True
        return False


if __name__ == '__main__':
    print(Solution().judgePoint24([3, 3, 8, 8]))
