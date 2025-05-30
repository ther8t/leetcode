import collections
import re


class Solution:
    def getFolderNames(self, names):
        next_iteration_number = collections.defaultdict(int)
        name_set = set()
        ans = []

        def get_next_iteration_number(name, start):
            ptr = start
            while True:
                if name + "(" + ptr + ")" not in name_set:
                    return ptr
                ptr += 1

        for name in names:
            a = re.match("(.*?)((\()(\d+)(\)))?$", name)
            name_without_bracket = a.group(1)
            number = int(a.group(4)) if a.group(4) else 0

            if name in name_set:
                # conflict
                ptr = 1
                while True:
                    if name + "(" + str(ptr) + ")" not in name_set:
                        ans.append(name + "(" + str(ptr) + ")")
                        name_set.add(name + "(" + str(ptr) + ")")
                        break
                    ptr += 1

                while
            else:
                ans.append(name)
                name_set.add(name)
                next_iteration_number[name] = 1
        return ans


if __name__ == '__main__':
    print(Solution().getFolderNames(names = ["pes","fifa","gta","pes(2019)"]))
    print(Solution().getFolderNames(names = ["gta","gta(1)","gta","avalon"]))
    print(Solution().getFolderNames(names = ["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece"]))
    print(Solution().getFolderNames(["kaido","kaido(1)","kaido","kaido(1)"]))
    print(Solution().getFolderNames(["gta(1)","gta","gta"]))
    print(Solution().getFolderNames(["m","t","y(4)","t","a","p","h","h","z","z(2)(2)","x(3)","h(4)(3)","l","z(1)","h","s(1)(2)","y(3)(2)","m(3)","i","h","u","j(1)(4)","q","j(1)","c","n(4)","k","s(1)(4)","p(2)","m","r(1)(4)","k(3)","d(3)(1)","e(4)"]))
