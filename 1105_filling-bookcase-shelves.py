import functools


class Solution:
    def minHeightShelves(self, books, shelf_width: int) -> int:

        @functools.lru_cache(None)
        def get_height(index):
            if index >= len(books):
                return 0
            current_width, current_height = 0, 0
            min_height_possible = float('inf')
            for i in range(index, len(books)):
                current_width += books[i][0]
                if current_width > shelf_width:
                    break
                current_height = max(current_height, books[i][1])
                min_height_possible = min(min_height_possible, current_height + get_height(i + 1))
            return min_height_possible
        return get_height(0)

    """
    Attempt: Fired
    Accepted
    """
    def minHeightShelves(self, books, shelf_width: int) -> int:
        @functools.lru_cache(None)
        def getHeight(index):
            if index == len(books):
                return 0
            current_width, current_max = 0, 0
            ans = float('inf')
            for i in range(index, len(books)):
                if current_width + books[i][0] > shelf_width:
                    break
                current_max = max(current_max, books[i][1])
                current_width += books[i][0]
                ans = min(ans, current_max + getHeight(i + 1))

            return ans

        return getHeight(0)









if __name__ == '__main__':
    print(Solution().minHeightShelves(books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], shelf_width = 4))
    print(Solution().minHeightShelves(books = [[1,3],[2,4],[3,2]], shelf_width = 6))
