import collections


class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        map = collections.defaultdict(list)
        for i in range(numCourses):
            map[i] = []
        reverse_map = collections.defaultdict(list)

        for course, prerequisite in prerequisites:
            map[course].append(prerequisite)
            reverse_map[prerequisite].append(course)

        while len(map):
            no_required_course = min(map, key=lambda x: len(map[x]))
            if len(map[no_required_course]) > 0:
                return False
            for i in reverse_map[no_required_course]:
                if i in map:
                    map[i].remove(no_required_course)
            del map[no_required_course]

        return True

if __name__ == '__main__':
    print(Solution().canFinish(numCourses=2, prerequisites=[[1, 0]]))
    print(Solution().canFinish(numCourses=4, prerequisites=[[1, 0], [2, 0], [3, 1], [3, 2]]))
    print(Solution().canFinish(numCourses=1, prerequisites=[]))
    print(Solution().canFinish(2, [[0, 1], [1, 0]]))
