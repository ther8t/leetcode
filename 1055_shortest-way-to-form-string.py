class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        ptr_s, ptr_t = 0, 0

        counter = 0
        while ptr_t < len(target):
            temp = ptr_t
            ptr_s = 0
            while ptr_s < len(source):
                if ptr_t<len(target) and target[ptr_t] == source[ptr_s]:
                    ptr_t+=1
                ptr_s+=1
            counter+=1
            if ptr_t == temp:
                return -1
        return counter

    # # Accepted : 5%
    # def shortestWay(self, source: str, target: str) -> int:
    #     # is source the subsequence of target
    #     def is_subsequence(source, target):
    #         ptr_s = 0
    #         ptr_t = 0
    #         while ptr_s < len(source) and ptr_t < len(target):
    #             if source[ptr_s] == target[ptr_t]:
    #                 ptr_t += 1
    #                 ptr_s += 1
    #             else:
    #                 ptr_t += 1
    #         return ptr_s == len(source)
    #
    #     counter = 0
    #
    #     ptr1, ptr2 = 0, 1
    #     while ptr1 < len(target) and ptr2 <= len(target):
    #         if is_subsequence(target[ptr1:ptr2], source):
    #             ptr2 += 1
    #         else:
    #             if not is_subsequence(target[ptr2 - 1], source):
    #                 return -1
    #             ptr1 = ptr2 - 1
    #             counter += 1
    #     return counter + 1


if __name__ == '__main__':
    print(Solution().shortestWay(source = "xyz", target = "xzyxz"))
