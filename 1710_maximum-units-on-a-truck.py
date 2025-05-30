class Solution:
    def maximumUnits(self, boxTypes, truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)

        net_value = 0
        for count, value in boxTypes:
            if truckSize > count:
                net_value += count * value
                truckSize -= count
            else:
                net_value += value * truckSize
                break

        return net_value


if __name__ == '__main__':
    print(Solution().maximumUnits(boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4))
    print(Solution().maximumUnits(boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10))
