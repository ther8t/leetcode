class RLEIterator:

    """
    Revision 2:
    There is another way to solve this question. We first update all even places to make it such that it's the running sum of the previous and all.
    We then keep a pointer to increment and see if the ptr <= current_sum_index. If it is, it's this number, else it's either forward or we have come to the end of the array and it's not here.

    But I have to say that earlier algo is slightly better because it doesn't do the running sum in initialization. Although it edits the encoding, when needed but there maybe a case when it's not needed.
    The principle remains the same.
    """

    def __init__(self, encoding):
        self.encoding = encoding
        self.ptr = 0

    def next(self, n: int) -> int:
        if n == 0:
            return -1
        last_removed_ptr = self.ptr
        while self.ptr < len(self.encoding) and (self.encoding[self.ptr] == 0 or n > 0):
            current_numbers_available = self.encoding[self.ptr]
            if current_numbers_available == 0:
                self.ptr += 2
            elif current_numbers_available < n:
                n -= current_numbers_available
                self.encoding[self.ptr] = 0
            else:
                self.encoding[self.ptr] -= n
                n = 0
                last_removed_ptr = self.ptr

        if n == 0 and last_removed_ptr < len(self.encoding):
            return self.encoding[last_removed_ptr + 1]
        else:
            return -1

        # if self.encoding[self.ptr] == 0:
        #     if self.ptr + 2 < len(self.encoding):
        #         self.ptr += 2
        #         return self.next(n)
        #     else:
        #         return -1
        # else:
        #     while n > 0 and self.ptr < len(self.encoding):
        #         current_numbers_available = self.encoding[self.ptr]
        #         if current_numbers_available == 0:
        #             self.ptr += 2
        #         elif current_numbers_available < n:
        #             n -= current_numbers_available
        #             self.encoding[self.ptr] -= current_numbers_available
        #         else:
        #             self.encoding[self.ptr] -= n
        #             n = 0
        #         if self.ptr < len(self.encoding):
        #             return self.encoding[self.ptr + 1]
        #         else:
        #             return -1


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)

if __name__ == '__main__':
    e = RLEIterator([3, 8, 0, 9, 2, 5])
    print(e.next(2))
    print(e.next(1))
    print(e.next(1))
    print(e.next(2))
