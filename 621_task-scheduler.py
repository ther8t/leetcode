import collections


class Solution:
    """
    Attempt: Fired
    Accepted: 5%
    """
    def leastInterval(self, tasks, n: int) -> int:
        queue = []
        task_set = collections.defaultdict(int)
        tasks_counter = collections.Counter(tasks)

        current_time = 0

        def getNextTask():
            for task in sorted(tasks_counter.keys(), key=lambda x: -tasks_counter[x]):
                if task not in task_set or current_time - task_set[task] > n:
                    return task
            return None

        while len(tasks_counter) > 0:
            next_task = getNextTask()

            while queue and queue[0][1] < current_time:
                task, entry_time = queue.pop(0)

            if not next_task:
                current_time = max(current_time, queue[0][1] + n + 1 if queue else current_time + 1)
            else:
                tasks_counter[next_task] -= 1
                queue.append((next_task, current_time))
                task_set[next_task] = current_time
                if tasks_counter[next_task] == 0:
                    del tasks_counter[next_task]
                current_time += 1

        return current_time





if __name__ == '__main__':
    # print(Solution().leastInterval(tasks = ["A","A","A","B","B","B"], n = 2))
    # print(Solution().leastInterval(tasks = ["A","C","A","B","D","B"], n = 1))
    # print(Solution().leastInterval(tasks = ["A","A","A", "B","B","B"], n = 3))
    # print(Solution().leastInterval(tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 1))
    print(Solution().leastInterval(["A","A","A","B","B","B","C","D","E","F","G","H","I","J","K"], 7))
