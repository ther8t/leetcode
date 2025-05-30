import collections
from collections import defaultdict


class Solution:

    """
    Revision 2:
    I remembered the lesson from last time that there are multiple layes. It's not sufficient to evaluate a, c if we have a, b and b, c. There maybe a case where a, c is used in c, d to produce a, d.
    I used queue as in bfs to go deeper.
    There was some confusion with the variable names and arrangement while writing the code. Aside from that the logic was impeccable.
    This is another way of solving it.
    I had solved it in a much different way earlier.

    The proposed solution from the first attempt is exactly the same as the one I have written in the attempt 2.
    It's just that they use queue when required and I have prepared the list beforehand.
    """
    def calcEquation(self, equations, values, queries):
        variable_value_map = collections.defaultdict(float)
        a_variables_map = collections.defaultdict(list)

        for (a, b), val in zip(equations, values):
            variable_value_map[(a, b)] = val
            variable_value_map[(b, a)] = 1 / val
            a_variables_map[a].append((a, b))
            a_variables_map[b].append((b, a))

        while equations:
            a, b = equations.pop(0)
            if a == b:
                continue

            # searching for c, d such that a, b and c, d form a, d and c == b
            for c, d in a_variables_map[b]:
                if (a, d) not in variable_value_map:
                    variable_value_map[(a, d)] = variable_value_map[(a, b)] * variable_value_map[(c, d)]
                    variable_value_map[(d, a)] = variable_value_map[(d, c)] * variable_value_map[(b, a)]
                    a_variables_map[a].append((a, d))
                    a_variables_map[a].append((d, a))
                    equations.append((a, d))
                    equations.append((d, a))

            # searching for c, d such that b, a and c, d form b, d and a == c
            for c, d in a_variables_map[a]:
                if (b, d) not in variable_value_map:
                    variable_value_map[(b, d)] = variable_value_map[(b, a)] * variable_value_map[(c, d)]
                    variable_value_map[(d, b)] = variable_value_map[(d, c)] * variable_value_map[(a, b)]
                    a_variables_map[a].append((b, d))
                    a_variables_map[a].append((d, b))
                    equations.append((b, d))
                    equations.append((d, b))

        ans = []
        for a, b in queries:
            # This though true is not a part of the problem, not my concern.
            # if a == b:
            #     ans.append(1.0)
            #     continue
            ans.append(variable_value_map[(a, b)] if (a, b) in variable_value_map else -1.0)

        return ans





    # def calcEquation(self, equations, values, queries):
    #     numerator_denominator_map = defaultdict(list)
    #     pair_value_map = defaultdict(float)
    #
    #     def add_pair(a, b, val):
    #         numerator_denominator_map[a].append(b)
    #         numerator_denominator_map[b].append(a)
    #         pair_value_map[(a, b)] = val
    #         pair_value_map[(b, a)] = 1 / val
    #
    #     def find(a, b):
    #         if a not in numerator_denominator_map or b not in numerator_denominator_map:
    #             return -1.0
    #         if a == b:
    #             return 1.0
    #         visited = set()
    #         queue = [(a, 1)]
    #         visited.add(a)
    #
    #         while queue:
    #             current_numerator, multiplier = queue.pop(0)
    #             for denominator in numerator_denominator_map[current_numerator]:
    #                 if denominator == b:
    #                     return multiplier * pair_value_map[(current_numerator, denominator)]
    #                 if denominator not in visited:
    #                     queue.append((denominator, multiplier * pair_value_map[(current_numerator, denominator)]))
    #                     visited.add(denominator)
    #         return -1.0
    #
    #     for (a, b), val in zip(equations, values):
    #         add_pair(a, b, val)
    #
    #     ans = []
    #     for a, b in queries:
    #         ans.append(find(a, b))
    #
    #     return ans


    # def calcEquation(self, equations, values, queries):
    #     variable_equation_map = defaultdict(list)
    #     pair_value_map = defaultdict(float)
    #
    #     def add_pair(a, b, val):
    #         pair_value_map[(a, b)] = val
    #         pair_value_map[(b, a)] = 1 / val
    #         variable_equation_map[a].append((a, b))
    #         variable_equation_map[a].append((b, a))
    #         variable_equation_map[b].append((a, b))
    #         variable_equation_map[b].append((b, a))
    #
    #     for (a, b), val in zip(equations, values):
    #         for c, d in variable_equation_map[a]:
    #             if a == d:
    #                 add_pair(c, b, val * pair_value_map[(c, d)])
    #
    #         for c, d in variable_equation_map[b]:
    #             if b == c:
    #                 add_pair(a, d, val * pair_value_map[(c, d)])
    #         add_pair(a, b, val)
    #
    #
    #     ans = []
    #     for a, b in queries:
    #         if a not in variable_equation_map or b not in variable_equation_map:
    #             ans.append(-1.0)
    #             continue
    #         if a == b:
    #             ans.append(1.0)
    #             continue
    #         ans.append(pair_value_map[(a, b)] if (a, b) in pair_value_map else -1.0)
    #
    #     return ans


if __name__ == '__main__':
    print(Solution().calcEquation([["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]], [3.0,4.0,5.0,6.0], [["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]))
    # print(Solution().calcEquation(equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))
    # print(Solution().calcEquation(equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]))
    # print(Solution().calcEquation(equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]))
    # print(Solution().calcEquation([["a","b"],["e","f"],["b","e"]], [3.4,1.4,2.3], [["b","a"],["a","f"],["f","f"],["e","e"],["c","c"],["a","c"],["f","e"]]))
    # print(Solution().calcEquation([["a","b"],["b","c"],["a","c"],["d","e"]], [2.0,3.0,6.0,1.0], [["a","c"],["b","c"],["a","e"],["a","a"],["x","x"],["a","d"]]))
