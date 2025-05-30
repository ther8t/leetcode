class Solution:
    def deckRevealedIncreasing(self, deck):
        s1, s2 = [i for i in reversed(range(len(deck)))], []
        sorted_deck = sorted(deck, reverse=True)

        out = [-1] * len(deck)

        while s1 or s2:
            # place one
            out[s1[-1]] = sorted_deck[-1]
            sorted_deck.pop()
            s1.pop()

            # skip one
            if not s1:
                s1 = s2
                s2 = []

            if s1:
                s2 = [s1.pop()] + s2

                if not s1:
                    s1 = s2
                    s2 = []

        return out


if __name__ == '__main__':
    # print(Solution().deckRevealedIncreasing([999999991,9]))
    print(Solution().deckRevealedIncreasing(deck = [17,13,11,2,3,5,7]))
    print(Solution().deckRevealedIncreasing(deck = [1,1000]))
