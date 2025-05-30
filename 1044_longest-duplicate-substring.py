import collections


class Solution:
    # # TLE : 27/61
    # def longestDupSubstring(self, s: str) -> str:
    #     n = len(s)
    #     longest_dup = ""
    #     for i in range(1, n):
    #         ptr1, ptr2 = i, 0
    #         while ptr1 < n and ptr2 < n:
    #             current_dup = ""
    #             if s[ptr1] == s[ptr2]:
    #                 while ptr1 < n and ptr2 < n and s[ptr1] == s[ptr2]:
    #                     current_dup += s[ptr1]
    #                     ptr1 += 1
    #                     ptr2 += 1
    #             else:
    #                 ptr1 += 1
    #                 ptr2 += 1
    #             if len(current_dup) > len(longest_dup):
    #                 longest_dup = current_dup
    #
    #     return longest_dup


    # # TLE
    # def longestDupSubstring(self, s: str) -> str:
    #     twin_map = collections.defaultdict(list)
    #
    #     current_match = ""
    #     for index, char in enumerate(s):
    #         twin_map[char].append(index)
    #         if len(twin_map[char]) > 1:
    #             current_match = char
    #
    #     if not current_match:
    #         return ""
    #
    #     while twin_map:
    #         temp_map = collections.defaultdict(set)
    #         for unit in twin_map:
    #             if len(twin_map[unit]) > 1:
    #                 for match_index in twin_map[unit]:
    #                     if match_index + len(unit) < len(s):
    #                         further_match = unit + s[match_index + len(unit)]
    #                         temp_map[further_match].add(match_index)
    #                         if len(unit) + 1 > len(current_match) and len(temp_map[further_match]) > 1:
    #                             current_match = further_match
    #
    #         twin_map = temp_map
    #
    #     return current_match

    def longestDupSubstring(self, s: str) -> str:
        def rabin_karp(length):
            MOD = 10 ** 9 + 7
            hashmap = collections.defaultdict(list)

            hash = 0
            for i in range(length):
                hash = (hash * 26 + nums[i]) % MOD

            hashmap[hash].append(0)

            for i in range(1, len(s) - length + 1):
                hash = (hash * 26 - nums[i - 1] * pow(26, length, MOD) + nums[i + length - 1]) % MOD
                if hash in hashmap:
                    current_hash_string = s[i:i + length]
                    if any(current_hash_string == s[j:j + length] for j in hashmap[hash]):
                        return i
                hashmap[hash].append(i)
            return -1

        nums = [ord(s[i]) - ord('a') for i in range(len(s))]

        left, right = 1, len(s) - 1
        longest_duplicate_start = -1
        while left <= right:
            mid = (left + right) // 2
            current_duplicate = rabin_karp(mid)
            if current_duplicate != -1:
                longest_duplicate_start = current_duplicate
                left = mid + 1
            else:
                right = mid - 1
        return s[longest_duplicate_start:longest_duplicate_start + left - 1]


if __name__ == '__main__':
    print(Solution().longestDupSubstring(s = "okmzpmxzwjbfssktjtebhhxfphcxefhonkncnrumgduoaeltjvwqwydpdsrbxsgmcdxrthilniqxkqzuuqzqhlccmqcmccfqddncchadnthtxjruvwsmazlzhijygmtabbzelslebyrfpyyvcwnaiqkkzlyillxmkfggyfwgzhhvyzfvnltjfxskdarvugagmnrzomkhldgqtqnghsddgrjmuhpgkfcjkkkaywkzsikptkrvbnvuyamegwempuwfpaypmuhhpuqrufsgpiojhblbihbrpwxdxzolgqmzoyeblpvvrnbnsdnonhpmbrqissifpdavvscezqzclvukfgmrmbmmwvzfpxcgecyxneipexrzqgfwzdqeeqrugeiupukpveufmnceetilfsqjprcygitjefwgcvqlsxrasvxkifeasofcdvhvrpmxvjevupqtgqfgkqjmhtkyfsjkrdczmnettzdxcqexenpxbsharuapjmdvmfygeytyqfcqigrovhzbxqxidjzxfbrlpjxibtbndgubwgihdzwoywqxegvxvdgaoarlauurxpwmxqjkidwmfuuhcqtljsvruinflvkyiiuwiiveplnxlviszwkjrvyxijqrulchzkerbdyrdhecyhscuojbecgokythwwdulgnfwvdptzdvgamoublzxdxsogqpunbtoixfnkgbdrgknvcydmphuaxqpsofmylyijpzhbqsxryqusjnqfikvoikwthrmdwrwqzrdmlugfglmlngjhpspvnfddqsvrajvielokmzpmxzwjbfssktjtebhhxfphcxefhonkncnrumgduoaeltjvwqwydpdsrbxsgmcdxrthilniqxkqzuuqzqhlccmqcmccfqddncchadnthtxjruvwsmazlzhijygmtabbzelslebyrfpyyvcwnaiqkkzlyillxmkfggyfwgzhhvyzfvnltjfxskdarvugagmnrzomkhldgqtqnghsddgrjmuhpgkfcjkkkaywkzsikptkrvbnvuyamegwempuwfpaypmuhhpuqrufsgpiojhblbihbrpwxdxzolgqmzoyeblpvvrnbnsdnonhpmbrqissifpdavvscezqzclvukfgmrmbmmwvzfpxcgecyxneipexrzqgfwzdqeeqrugeiupukpveufmnceetilfsqjprcygitjefwgcvqlsxrasvxkifeasofcdvhvrpmxvjevupqtgqfgkqjmhtkyfsjkrdczmnettzdxcqexenpxbsharuapjmdvmfygeytyqfcqigrovhzbxqxidjzxfbrlpjxibtbndgubwgihdzwoywqxegvxvdgaoarlauurxpwmxqjkidwmfuuhcqtljsvruinflvkyiiuwiiveplnxlviszwkjrvyxijqrulchzkerbdyrdhecyhscuojbecgokythwwdulgnfwvdptzdvgamoublzxdxsogqpunbtoixfnkgbdrgknvcydmphuaxqpsofmylyijpzhbqsxryqusjnqfikvoikwthrmdwrwqzrdmlugfglmlngjhpspvnfddqsvrajviel"))
    print(Solution().longestDupSubstring(s = "banana"))
    print(Solution().longestDupSubstring(s = "nnpxouomcofdjuujloanjimymadkuepightrfodmauhrsy"))
    print(Solution().longestDupSubstring(s = "aa"))