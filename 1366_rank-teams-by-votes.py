import collections


class Solution:

    """
    Accepted: 75%
    Interesting question, Didn't realise you could also sort arrays. The trick is to create the sort function smartly.
    The place where I made one mistake was that I failed to understand that the rank is sorted desc and the alphabetical order is sorted asc
    """
    def rankTeams(self, votes) -> str:
        max_rank = len(votes[0])
        rank_char_map = collections.defaultdict(lambda: collections.defaultdict(int))
        for vote in votes:
            for rank, team in enumerate(vote):
                rank_char_map[team][rank] += 1


        def getSortFunc(team):
            a = [rank_char_map[team][i] for i in range(max_rank)]
            return a + [-ord(team)]

        ans = []
        for rank in range(max_rank - 1, -1, -1):
            order = sorted(rank_char_map, key=lambda x: getSortFunc(x), reverse=True)
            selected = order[0]
            ans.append(selected)
            del rank_char_map[selected]

        return "".join(ans)


if __name__ == '__main__':
    # print(Solution().rankTeams(["ABC","ACB","ABC","ACB","ACB"]))
    # print(Solution().rankTeams(votes = ["WXYZ","XYZW"]))
    # print(Solution().rankTeams(votes = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]))
    print(Solution().rankTeams(["BCA","CAB","CBA","ABC","ACB","BAC"]))
