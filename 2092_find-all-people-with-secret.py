import collections
import heapq


class DSU:
    def __init__(self, elements):
        self.representative = {i: i for i in elements}
        self.size = {i: 1 for i in elements}

    def find(self, element):
        if self.representative[element] == element:
            return element

        self.representative[element] = self.find(self.representative[element])
        return self.representative[element]

    def combine(self, element1, element2):
        representative_element1 = self.find(element1)
        representative_element2 = self.find(element2)

        if representative_element1 == representative_element2:
            return

        if self.size[representative_element1] > self.size[representative_element2]:
            self.representative[representative_element2] = representative_element1
            self.size[element1] += self.size[element2]
        else:
            self.representative[representative_element1] = representative_element2
            self.size[representative_element2] += self.size[representative_element1]


class Solution:
    def findAllPeople(self, n: int, meetings, firstPerson: int):
        queue = []
        for p1, p2, time in meetings:
            heapq.heappush(queue, (time, p1, p2))
        # queue = [(time, p1, p2) for p1, p2, time in meetings]

        meetings.sort(key=lambda x: x[2])
        ptr1, N = 0, len(meetings)
        current_meeting_time = meetings[ptr1][2]

        dsu = DSU([i for i in range(n)])
        wise_people = set()
        wise_people.add(0)
        wise_people.add(firstPerson)
        dsu.combine(firstPerson, 0)

        elements = set()
        while len(queue) > 0:
            # graph = collections.defaultdict(list)
            latestElement = heapq.heappop(queue)
            if latestElement[0] != current_meeting_time:
                for element in elements:
                    if dsu.find(element) != dsu.find(0):
                        dsu.representative[element] = element
                    else:
                        wise_people.add(element)
                elements = set()
                current_meeting_time = latestElement[0]

            dsu.combine(latestElement[1], latestElement[2])
            elements.add(latestElement[1])
            elements.add(latestElement[2])

        for element in elements:
            if dsu.find(element) != dsu.find(0):
                dsu.representative[element] = element
            else:
                wise_people.add(element)

        return list(wise_people)

    # def findAllPeople(self, n: int, meetings, firstPerson: int):
    #     meetings.sort(key=lambda x: x[2])
    #     ptr1, N = 0, len(meetings)
    #     current_meeting_time = meetings[ptr1][2]
    #
    #     dsu = DSU([i for i in range(n)])
    #     wise_people = set()
    #     wise_people.add(0)
    #     wise_people.add(firstPerson)
    #     dsu.combine(firstPerson, 0)
    #
    #     while ptr1 < N:
    #         # graph = collections.defaultdict(list)
    #         elements = set()
    #         while ptr1 < N and meetings[ptr1][2] == current_meeting_time:
    #             dsu.combine(meetings[ptr1][0], meetings[ptr1][1])
    #             elements.add(meetings[ptr1][0])
    #             elements.add(meetings[ptr1][1])
    #             ptr1 += 1
    #
    #         for element in elements:
    #             if dsu.find(element) != dsu.find(0):
    #                 dsu.representative[element] = element
    #             else:
    #                 wise_people.add(element)
    #
    #         if ptr1 < N:
    #             current_meeting_time = meetings[ptr1][2]
    #
    #     return list(wise_people)


# # TLE
# def findAllPeople(self, n: int, meetings, firstPerson: int):
#     meetings.sort(key=lambda x: x[2])
#     ptr1, N = 0, len(meetings)
#     current_meeting_time = meetings[ptr1][2]
#
#     wise_people = set()
#     wise_people.add(0)
#     wise_people.add(firstPerson)
#
#     while ptr1 < N:
#         graph = collections.defaultdict(list)
#         stack = []
#         while ptr1 < N and meetings[ptr1][2] == current_meeting_time:
#             graph[meetings[ptr1][0]].append(meetings[ptr1][1])
#             graph[meetings[ptr1][1]].append(meetings[ptr1][0])
#             if meetings[ptr1][0] in wise_people: stack.append(meetings[ptr1][0])
#             if meetings[ptr1][1] in wise_people: stack.append(meetings[ptr1][1])
#             ptr1 += 1
#
#         # DFS
#         # stack = list(wise_people)
#         while len(stack) > 0:
#             popped = stack.pop()
#             for i in graph[popped]:
#                 if i not in wise_people:
#                     stack.append(i)
#             wise_people.add(popped)
#
#         if ptr1 < N:
#             current_meeting_time = meetings[ptr1][2]
#
#     return list(wise_people)


if __name__ == '__main__':
    print(Solution().findAllPeople(n = 4, meetings = [[3,1,3],[1,2,2],[0,3,3]], firstPerson = 3))
