import collections


class Solution:
    """
    Revision 2:
    This is a fresher implementation of the code. I don't know what I had done earlier but this algo is simpler, easier to understand and best of all greeeedy.
    We simply sort the chars in a reverse order of their frequencies and remove the required frequencies of characters which are greater than their predecessors, so that it becomes just lower than it.
    Accepted 98%.
    """
    def minDeletions(self, s: str) -> int:
        counter = collections.Counter(s)

        changes = 0
        sorted_char_count_map_key = sorted(counter, key=lambda x: counter[x], reverse=True)
        for i in range(len(sorted_char_count_map_key) - 1):
            if counter[sorted_char_count_map_key[i]] <= counter[sorted_char_count_map_key[i + 1]]:
                old_next_value = counter[sorted_char_count_map_key[i + 1]]
                new_next_value = max(0, counter[sorted_char_count_map_key[i]] - 1)
                changes += (old_next_value - new_next_value)
                counter[sorted_char_count_map_key[i + 1]] = new_next_value

        return changes


    # def minDeletions(self, s: str) -> int:
    #     counter = collections.Counter(s)
    #     count_char_map = collections.defaultdict(list)
    #     for char in counter:
    #         count_char_map[counter[char]].append(char)
    #
    #     changes = 0
    #     keys = list(count_char_map.keys())[::]
    #     for count in keys:
    #         while len(count_char_map[count]) > 1:
    #             popped_char = count_char_map[count].pop()
    #             new_count = 0
    #             for i in range(count - 1, 0, -1):
    #                 if i in count_char_map:
    #                     continue
    #                 else:
    #                     new_count = i
    #                     break
    #             changes += count - new_count
    #             if new_count:
    #                 count_char_map[new_count].append(popped_char)
    #     return changes


if __name__ == '__main__':
    print(Solution().minDeletions(s = "aab"))
    print(Solution().minDeletions(s = "abcabc"))
    print(Solution().minDeletions(s = "bbcebab"))
    print(Solution().minDeletions(s = "aaabbbcc"))
    print(Solution().minDeletions(s = "ceabaacb"))
