import collections


class Solution:
    def countStudents(self, students, sandwiches) -> int:
        counter = collections.Counter(students)

        while len(counter) > 1:
            if students[0] == sandwiches[0]:
                top = students[0]
                students.pop(0)
                sandwiches.pop(0)
                counter[top] -= 1
                if counter[top] == 0:
                    del counter[top]
            else:
                students.append(students.pop(0))

        while students and sandwiches and students[0] == sandwiches[0]:
            students.pop(0)
            sandwiches.pop(0)

        return len(students)


if __name__ == '__main__':
    print(Solution().countStudents(students = [1,1,0,0], sandwiches = [0,1,0,1]))
    print(Solution().countStudents(students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]))
