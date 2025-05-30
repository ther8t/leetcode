class Solution:
    def maxLength(self, arr) -> int:
        arr_map = {}
        for word in arr:
            hash = 0
            char_set = set()
            should_add = True
            for char in word:
                if char not in char_set:
                    hash += 1 << ord(char) - ord('a')
                    char_set.add(char)
                else:
                    should_add = False
                    break

            if should_add:
                arr_map[word] = hash
        arr = list(arr_map.keys())
        max_score = 0

        def count(index, hash, score):
            nonlocal max_score
            if index == len(arr):
                max_score = max(max_score, score)
                return

            if arr_map[arr[index]] & hash == 0:
                count(index + 1, arr_map[arr[index]] + hash, score + len(arr[index]))
            count(index + 1, hash, score)

        count(0, 0, 0)
        return max_score


    """
    Attempt#2
    Misunderstood the question.
    """
    def maxLength(self, arr) -> int:
        max_length = 0

        def get_score(word):
            score = 0
            for char in word:
                score += (1 << (ord(char) - ord('a')))
            return score

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if get_score(arr[i]) & get_score(arr[j]) == 0:
                    max_length = max(max_length, len(arr[i]) + len(arr[j]))
        return max_length



    """
    Attempt#2
    Accepted 97%
    The trick is to reduce the time complexity by reducing the time it takes to compare strings. This can be done by binary.
    """
    def maxLength(self, arr) -> int:
        def get_score(word):
            score = 0
            chars = set()
            for char in word:
                if char in chars:
                    return 0
                chars.add(char)
                score += (1 << (ord(char) - ord('a')))
            return score

        temp_arr = []
        score_map = {}
        for word in arr:
            score = get_score(word)
            if score != 0:
                score_map[word] = score
                temp_arr.append(word)
        arr = temp_arr
        n = len(arr)

        def maxLengthRec(current_word, current_score, index):
            if index == n:
                return len(current_word)

            max_len = len(current_word)
            for i in range(index, n):
                index_score = score_map[arr[i]]
                if current_score & index_score == 0:
                    max_len = max(max_len, maxLengthRec(current_word + arr[i], current_score + index_score, i + 1))

            return max_len

        return maxLengthRec("", 0, 0)







if __name__ == '__main__':
    print(Solution().maxLength(arr = ["un","iq","ue"]))
    print(Solution().maxLength(arr = ["cha","r","act","ers"]))
    print(Solution().maxLength(arr = ["abcdefghijklmnopqrstuvwxyz"]))
    print(Solution().maxLength(["aa","bb"]))
    print(Solution().maxLength(["a", "abc", "d", "de", "def"]))
