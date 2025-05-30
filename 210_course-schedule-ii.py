import collections


class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        map = collections.defaultdict(list)
        for i in range(numCourses):
            map[i] = []
        reverse_map = collections.defaultdict(list)

        for course, prerequisite in prerequisites:
            map[course].append(prerequisite)
            reverse_map[prerequisite].append(course)

        order = []
        while len(map):
            no_required_course = min(map, key=lambda x: len(map[x]))
            if len(map[no_required_course]) > 0:
                return []
            order.append(no_required_course)
            for i in reverse_map[no_required_course]:
                if i in map:
                    map[i].remove(no_required_course)
            del map[no_required_course]

        return order


    """
    Revision 2:
    My previous attempt was correct but it did not employ the use of P-Queues.
    A typical Topological sort employs the use of P-Queues.
    Actually now that I realise. It does not even need P-Queues because the only values that go into the array is the ones with indegree 0.
    I can simply make use of Double ended Queues, or simply pop from the end and use simple stack
    No need for PQueues or Dqueues or Any other queue.
    The question can simply be solved with stacks.
    Accepted 77%
    """
    def findOrder(self, numCourses: int, prerequisites):
        course_prerequisite_map = {i: set() for i in range(numCourses)}
        prerequisite_course_map = collections.defaultdict(set)

        for course, prerequisite in prerequisites:
            course_prerequisite_map[course].add(prerequisite)
            prerequisite_course_map[prerequisite].add(course)

        stack = []
        for course in course_prerequisite_map:
            if len(course_prerequisite_map[course]) == 0:
                stack.append(course)

        out = []
        while stack:
            course = stack.pop()
            out.append(course)

            for c in prerequisite_course_map[course]:
                course_prerequisite_map[c].remove(course)
                if len(course_prerequisite_map[c]) == 0:
                    stack.append(c)

        return out if len(out) == numCourses else []





if __name__ == '__main__':
    print(Solution().findOrder(numCourses = 2, prerequisites = [[1,0]]))
    print(Solution().findOrder(numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]))
    print(Solution().findOrder(numCourses = 1, prerequisites = []))
    print(Solution().findOrder(2, [[0,1],[1,0]]))
