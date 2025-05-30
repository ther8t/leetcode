import bisect
import collections


"""
Accepted 91%
"""
class TopVotedCandidate:

    def __init__(self, persons, times):
        self.times = times
        self.persons = persons
        total_votes = len(times)
        highest_voted = persons[0]
        highest_vote_count = 1
        self.highest_voted_at_time = []
        votes_count = collections.defaultdict(int)

        for i in range(total_votes):
            votes_count[persons[i]] += 1
            if highest_vote_count <= votes_count[persons[i]]:
                highest_vote_count = votes_count[persons[i]]
                highest_voted = persons[i]
            self.highest_voted_at_time.append(highest_voted)

    def q(self, t: int) -> int:
        index = bisect.bisect_right(self.times, t)
        return self.highest_voted_at_time[index - 1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)


if __name__ == '__main__':
    t = TopVotedCandidate([0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30])
    print(t.q(3))
    print(t.q(12))
    print(t.q(25))
    print(t.q(15))
    print(t.q(24))
    print(t.q(8))
