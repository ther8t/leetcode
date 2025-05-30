import collections


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret_map = collections.defaultdict(int)
        guess_map = collections.defaultdict(int)
        a, b = 0, 0
        for secret_digit, guess_digit in zip(secret, guess):
            if secret_digit == guess_digit:
                a += 1
            else:

                if guess_map[secret_digit] > 0:
                    guess_map[secret_digit] -= 1
                    b += 1
                else:
                    secret_map[secret_digit] += 1

                if secret_map[guess_digit] > 0:
                    secret_map[guess_digit] -= 1
                    b += 1
                else:
                    guess_map[guess_digit] += 1

        return str(a) + "A" + str(b) + "B"

    # # Accepted
    # def getHint(self, secret: str, guess: str) -> str:
    #     secret_map = collections.defaultdict(int)
    #     guess_map = collections.defaultdict(int)
    #
    #     for digit in secret:
    #         secret_map[int(digit)] += 1
    #
    #     for digit in guess:
    #         guess_map[int(digit)] += 1
    #
    #     a = 0
    #     for secret_digit, guess_digit in zip(secret, guess):
    #         if secret_digit == guess_digit:
    #             secret_map[int(secret_digit)] -= 1
    #             guess_map[int(secret_digit)] -= 1
    #             a += 1
    #
    #     b = 0
    #     for i in range(10):
    #         b += min(secret_map[i], guess_map[i])
    #
    #     return str(a) + "A" + str(b) + "B"

    """
    Revision 2 :
    """
    def getHint(self, secret: str, guess: str) -> str:
        secret_map, guess_map = collections.defaultdict(set), collections.defaultdict(set)

        bull_count = 0
        for index, (secret_number, guess_number) in enumerate(zip(secret, guess)):
            if secret_number == guess_number:
                bull_count += 1
                continue
            secret_map[secret_number].add(index)
            guess_map[guess_number].add(index)

        cow_count = 0
        for i in range(10):
            i = str(i)
            cow_count += len(min(secret_map[i], guess_map[i], key=len))

        return str(bull_count) + "A" + str(cow_count) + "B"




if __name__ == '__main__':
    print(Solution().getHint(secret="1123", guess="0111"))
    print(Solution().getHint(secret = "1807", guess = "7810"))
