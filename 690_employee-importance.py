
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates



class Solution:
    def getImportance(self, employees, id: int) -> int:
        employees = {i.id: i for i in employees}

        stack = []
        visited = {}

        stack.append(employees[id])

        importance = 0
        while len(stack) > 0:
            popped = stack.pop()
            if popped.id not in visited:
                importance += popped.importance
                for subordinate in popped.subordinates:
                    if subordinate not in visited:
                        stack.append(employees[subordinate])

        return importance

if __name__ == '__main__':
    print(Solution().getImportance(employees=[Employee(1,2,[5]), Employee(5,-3,[])], id=5))
