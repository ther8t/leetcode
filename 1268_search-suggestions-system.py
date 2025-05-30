import collections

Trie = lambda : collections.defaultdict(Trie)
IS_WORD = ""

class Solution:
    # Accepted 5%
    def suggestedProducts(self, products, searchWord: str):
        trie = Trie()

        def add_to_trie(word):
            temp = trie

            for char in word:
                temp = temp[char]
            temp[IS_WORD] = True

        def get_all_words(t, word):
            if len(search_result) == 3:
                return True
            if IS_WORD in t:
                search_result.append(word)
            for key in sorted(t):
                if key == IS_WORD:
                    continue
                found = get_all_words(t[key], word + key)
                if found:
                    return True

        for p in products:
            add_to_trie(p)

        search_builder = ""
        out = []
        temp = trie
        for char in searchWord:
            search_builder += char
            if not temp or char not in temp:
                temp = None
                out.append([])
                continue

            temp = temp[char]
            search_result = []
            get_all_words(temp, search_builder)
            out.append(search_result)

        return out


if __name__ == '__main__':
    print(Solution().suggestedProducts(products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"))
