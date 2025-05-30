class Solution:
    def letterCombinations(self, digits: str):
        map = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
               '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}

        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return map.get(digits)

        subCombinations = self.letterCombinations(digits[1:])
        myDigit = digits[0]
        myMap = map.get(myDigit)
        mySubCombination = []

        for i in range(len(myMap)):
            for j in range(len(subCombinations)):
                mySubCombination.append(myMap[i] + subCombinations[j])
        return mySubCombination


if __name__ == '__main__':
    print(Solution().letterCombinations("2345"))
