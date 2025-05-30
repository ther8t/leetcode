import math


class Solution:
    """
    Revision 2:
    This is how I figured it out. I thought really hard, gave a look, pretended I was thinking and had an intuition.
    I thought what if we could club the binary of the number attempts number of times. So 100 100 100 100 would be 4 pigs for 3 attempts.
    It was wrong.
    Then I started to think starting from the smallest possible 3 attempts, 7 buckets, how many pigs?
    I had intuited that we could use the number of attempts to reduce the number of pigs and combine (pig number, attempt) to figure out which bucket has the poison.
        P1  P2
    0 - 0   0
    1 - 0   1
    2 - 0   2
    3 - 1   0
    4 - 1   1
    5 - 1   2
    6 - 2   0

    0, 1, 2 represent attempts # 1, 2, 3.
    So Pig 1 in his attempt 0 eats from bucket 0, 1 and 2. Pig 2 eats from bucket 3 and bucket 6.
    What happens next?

        🐷1 🐷2
    0 - 😵  😵
    1 - 😵  😁
    2 - 😵  😁
    3 - 😁  😵
    6 - 😁  😵

    If both of our piggies die we end up with bucket 0. No need for further violence (Oh! but the piggies are already dead).
    Unfortunately for the other cases one of them dies and one of them lives. Even more unfortunately, you need to play russian roulette with piggie#2's life once again.
    If both of them survive the first attempt of assassination. The buckets must be between 4 or 5. You have 2 buckets, 2 more attempts and two virtual piggies who never did any harm to you. You now have a tough choice to make. Which virtual piggie would you save?

    """
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        s = (minutesToTest//minutesToDie) + 1
        return math.ceil(float('%.5f' % math.log(buckets, s)))


if __name__ == '__main__':
    print(Solution().poorPigs(125, 1, 4))
