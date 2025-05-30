class Solution:
    def reorderLogFiles(self, logs):
        def get_key(log):
            identifier, l = log.split(" ", maxsplit=1)
            return (0, l, identifier) if l[0].isalpha() else (1, )
        return sorted(logs, key=lambda x: get_key(x))


if __name__ == '__main__':
    print(Solution().reorderLogFiles(logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]))
