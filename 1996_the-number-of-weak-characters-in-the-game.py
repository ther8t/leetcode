import collections

from sortedcontainers import SortedList


class Solution:
    """
    This is a clever bit of code.
    """
    def numberOfWeakCharacters(self, properties) -> int:
        max_d = [0] * 100002
        res = 0
        # We try and group the characters based on their attack strengths to find the max defense an attack strength can possess.
        for p in properties:
            max_d[p[0]] = max(max_d[p[0]], p[1])

        # For a character i the question really is - Is there a player who can attack me, which would make me weak?
        # None of the players who have less attack value can attack me, so out of all those who have attack more than mine, is there anyone who has more defense value than mine.
        # If yes I am weak, if not I am strong.
        for i in range(10000, -1, -1):
            max_d[i - 1] = max(max_d[i - 1], max_d[i])
        for p in properties:
            res += max_d[p[0] + 1] > p[1]
        return res

    # Accepted 24%
    """
    This question is similar to 354_russian-doll-envelope.
    """
    # def numberOfWeakCharacters(self, properties) -> int:
    #     properties.sort(key=lambda x: (x[0], -x[1]))
    #     arr = SortedList()
    #
    #     counter = 0
    #     for a, d in reversed(properties):
    #         index = arr.bisect_right(d)
    #         if index < len(arr):
    #             counter += 1
    #         arr.add(d)
    #
    #     return counter



    """
    Revision 2:
    I tried two methods.
    The idea is to keep track of the max attack strength and max defense strength. If my player's attack < max_attack and defense < max_defense, it's a weak player. This does not work.
    Why? Because, there max attack and max defense cannot does not necessarily exist in the same player. Even though the our current player has attack < max attack and defense < max defense, it can still be strong because for the player who has max attack might have lower defense or the player with max defense may have lower attack than ours, making our player NOT WEAK if not stronger.
    
    The second idea was to keep track of the players with max attack and max defense.
    and only if our current player has both attack and defense less than the players with max attack and max defense will it be strong. Which is true but this doesnt mean that our player is not weak. Being strong != not weak. A player can be not strong and not weak at the same time.
    That is why this algo recognises the strong players accurately but fails to distinguish between not strong and weak.
    
    The question must be treated the same way as russian envelope.
    Wrong Answer ↓
    """
    # def numberOfWeakCharacters(self, properties) -> int:
    #     properties.sort()
    #     max_attack_player_index, max_defense_player_index = len(properties) - 1, len(properties) - 1
    #
    #     counter = 0
    #     for index in range(len(properties) - 1, -1, -1):
    #         a, d = properties[index]
    #         if (a < properties[max_attack_player_index][0] and d < properties[max_attack_player_index][1]) or (a < properties[max_defense_player_index][0] and d < properties[max_defense_player_index][1]):
    #             counter += 1
    #         if a > properties[max_attack_player_index][0]:
    #             max_attack_player_index = index
    #         if d > properties[max_defense_player_index][1]:
    #             max_defense_player_index = index
    #
    #     return counter


    def numberOfWeakCharacters(self, properties) -> int:
        properties.sort(key= lambda x: (x[0], -x[1]))
        s = SortedList()

        counter = 0
        for a, d in reversed(properties):
            index = s.bisect_right(d)
            if index < len(s):
                counter += 1
            s.add(d)

        return counter


    def numberOfWeakCharacters(self, properties) -> int:
        a_d_map = {}
        for a, d in properties:
            if a not in a_d_map:
                a_d_map[a] = d
            else:
                a_d_map[a] = max(a_d_map[a], d)

        max_d = [0] * 100002
        for a in range(100000, -1, -1):
            if a not in a_d_map:
                max_d[a] = max_d[a + 1]
                continue
            max_d[a] = max(max_d[a + 1], a_d_map[a])

        counter = 0
        for a, d in properties:
            if d < max_d[a + 1]:
                counter += 1

        return counter


    """
    Attempt: Fired
    Accepted: 5%
    """
    def numberOfWeakCharacters(self, properties) -> int:
        """
        This question is similar to 354_russian-doll-envelope.
        The trick here is a bit difficult to comprehend at first. I had the idea in my head but I got the order misplaced.
        Were no two numbers to repeat the question makes a lot more sense. Sort the list by attack and see if defense is not the highest, because attack is obviously lower than others.
        The problem arises in the edge case where the attack value is equal (3, 2), (3, 3)
        The problem here is that for equals if I let (3, 3) go first, incoming (3, 2) will compare 2 and 3 and since 2 < 3, 2 is not the strongest. It concludes that since all attacks are greater than my attacks, and my defense is not the strongest, I must be a weak character.
        But if I send (3, 2) before (3, 3), 2 and 3 are compare, but this time 3 is still higher than 2, which means that even if 3 is not the strongest at defense, but that would be comparing it with playrs other than (3, 2)
        """
        properties.sort(key=lambda x: (x[0], -x[1]))
        s = SortedList()

        counter = 0
        for a, d in reversed(properties):
            index = s.bisect_right(d)
            if index < len(s):
                counter += 1
            s.add(d)
        return counter


if __name__ == '__main__':
    print(Solution().numberOfWeakCharacters(properties = [[5,5],[6,3],[3,6]]))
    print(Solution().numberOfWeakCharacters(properties = [[2,2],[3,3]]))
    print(Solution().numberOfWeakCharacters(properties = [[1,5],[10,4],[4,3]]))
    print(Solution().numberOfWeakCharacters([[7,9],[10,7],[6,9],[10,4],[7,5],[7,10]])) #2
    print(Solution().numberOfWeakCharacters([[37,70],[9,76],[44,30],[97,85],[96,59],[96,67]])) #5
