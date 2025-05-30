import collections


class Solution:
    # def groupAnagrams(self, strs):
    #     hashmap = {}
    #     for presentString in strs:
    #         counter = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0,
    #                    "m": 0,
    #                    "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0,
    #                    "z": 0, }
    #         for i in presentString:
    #             counter[i] += 1
    #         strHash = ""
    #         for i in counter.keys():
    #             strHash += i + str(counter[i])
    #
    #         if hashmap.get(strHash) is None:
    #             hashmap[strHash] = [presentString]
    #         else:
    #             hashmap[strHash].append(presentString)
    #
    #     anagramArray = []
    #     for arrayKey in hashmap.keys():
    #         anagramArray.append(hashmap.get(arrayKey))
    #     return anagramArray

    def groupAnagrams(self, strs):
        map = collections.defaultdict(list)

        def hash(i):
            keys = sorted(i)
            h = ""
            for key in keys:
                h += key + str(i[key])
            return h

        for s in strs:
            map[hash(collections.Counter(s))].append(s)
        return list(map.values())

    # def groupAnagrams(self, strs):
    #     hashmap = {}
    #     for str in strs:
    #         sortedStringArray = sorted(str)
    #         sortedString = ""
    #         for i in sortedStringArray:
    #             sortedString += i
    #         if hashmap.get(sortedString) is None:
    #             hashmap[sortedString] = [str]
    #         else:
    #             hashmap[sortedString].append(str)
    #
    #     anagramArray = []
    #     for arrayKey in hashmap.keys():
    #         anagramArray.append(hashmap.get(arrayKey))
    #     return anagramArray


if __name__ == '__main__':
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
