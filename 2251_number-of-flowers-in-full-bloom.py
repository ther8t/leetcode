class Solution:
    """
    Accepted: 92%
    This question is similar to the depth of the bracket question
    723_my-calendar-iii
    """
    def fullBloomFlowers(self, flowers, people):
        a = []
        bloom_counter = {}
        for s, e in flowers:
            a.append((s, 1))
            a.append((e + 1, -1))

        for p in people:
            a.append((p, 2))

        a.sort()

        counter = 0
        for time, increment in a:
            if increment == 2:
                bloom_counter[time] = counter
            else:
                counter += increment

        return [bloom_counter[time] for time in people]


if __name__ == '__main__':
    print(Solution().fullBloomFlowers(flowers = [[1,6],[3,7],[9,12],[4,13]], people = [2,3,7,11]))
    print(Solution().fullBloomFlowers(flowers = [[1,10],[3,3]], people = [3,3,2]))
