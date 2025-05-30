class Solution:
    def findMinDifference(self, timePoints) -> int:
        timeInMinutes = []
        for i in timePoints:
            timeInMinutes.append(self.timeToMinutes(i))

        minDiff = 24 * 60
        timeInMinutes.sort()
        """
        Revision 2:
        This is a smart step. A similar thing was also done in a question where we had to calculate the points in sight. 1610_maximum-number-of-visible-points
        Since we had to turn around and come back to the initial point and go a little further. The complete array was appended to itself.
        We can do that here as well but the complete array doesn't need to be taken into consideration here. All we need to do is to append the first number after 24 hours, i.e. minutes_for_first + 24*60
        """
        timeInMinutes.append(timeInMinutes[0] + 24*60)

        for i in range(len(timeInMinutes) - 1):
            minDiff = min(minDiff, abs(timeInMinutes[i + 1] - timeInMinutes[i]), abs(24*60 - timeInMinutes[i + 1] + timeInMinutes[i]))

        return minDiff

    def timeToMinutes(self, time):
        return int(time[0:2]) * 60 + int(time[3:5]) if time else 0


if __name__ == '__main__':
    # print(Solution().findMinDifference(timePoints=["00:00","04:00","22:00"]))
    print(Solution().findMinDifference(timePoints=["00:02","23:48","23:59"]))
