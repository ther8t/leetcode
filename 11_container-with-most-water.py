class Solution:

    """
    Revision 2:
    My first approach was the brute force combination of all nodes. I checked to see the submissions and found that was my first approach then too.
    I was not calm enough to come up with something, so I went downstairs and after I came back listened to some music and then tried to figure it out.

    Approach:
    The area can be large because of large x or large y. Large y is limited by the height of one of the poles.
    To optimise any of these values, we need to sort it either in x or y. Since the array is already sorted on x.
    We take the extreme ends of the array to maximize the x. Assuming a height of y on left as something, the water contained is limited by the height of this or the other end.
    When an end becomes limiting we move it to find a better end while keeping track of the maximum area we can find.
    """
    def maxArea(self, height) -> int:
        maxArea = 0
        ptr1 = 0
        ptr2 = len(height) - 1
        while ptr1 < ptr2:
            maxArea = max((ptr2 - ptr1) * min(height[ptr1], height[ptr2]), maxArea)
            if height[ptr2] > height[ptr1]:
                ptr1 = ptr1 + 1
            else:
                ptr2 = ptr2 - 1

        # for i in range(len(height)):
        #     for j in range(i+1, len(height)):
        #         maxArea = max((j - i)*min(height[i], height[j]), maxArea)
        return maxArea


if __name__ == '__main__':
    print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))
