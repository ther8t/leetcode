import collections


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager, informTime) -> int:
        company_tree = collections.defaultdict(list)

        for i in range(n):
            company_tree[manager[i]].append(i)

        max_time = 0
        time = [0 for _ in range(n)]
        queue = [headID]
        while queue:
            popped = queue.pop(0)
            under_popped = company_tree[popped]
            queue += under_popped
            for i in range(len(under_popped)):
                time[under_popped[i]] += (informTime[popped] + time[popped])
                max_time = max(max_time, time[under_popped[i]])

        return max_time

    def numOfMinutes(self, n: int, headID: int, manager, informTime) -> int:
        company_tree = collections.defaultdict(list)

        for i in range(n):
            company_tree[manager[i]].append(i)

        max_time = 0
        queue = [(0, headID)]
        while queue:
            time, popped = queue.pop(0)
            max_time = max(max_time, time)
            under_popped = company_tree[popped]
            for i in under_popped:
                queue.append((informTime[popped] + time, i))

        return max_time

    # # TLE
    # def numOfMinutes(self, n: int, headID: int, manager, informTime) -> int:
    #     def news_time(position):
    #         if position == -1:
    #             return 0
    #         return informTime[position] + news_time(manager[position])
    #
    #     time = [0 for _ in range(n)]
    #     for i in range(n):
    #         time[i] = news_time(i) - informTime[i]
    #     return max(time)


if __name__ == '__main__':
    print(Solution().numOfMinutes(7, 6, [1,2,3,4,5,6,-1], [0,6,5,4,3,2,1]))
