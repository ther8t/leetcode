# """
# This is FontInfo's API interface.
# You should not implement it, or speculate about its implementation
# """
import collections


class FontInfo(object):
    # Return the width of char ch when fontSize is used.
    def getWidth(self, fontSize, ch):
        """
        :type fontSize: int
        :type ch: char
        :rtype int
        """

    def getHeight(self, fontSize):
        """
        :type fontSize: int
        :rtype int
        """


class Solution:
    def maxFont(self, text: str, w: int, h: int, fonts, fontInfo: 'FontInfo') -> int:
        text_map = collections.defaultdict(int)
        for char in text:
            text_map[char] += 1

        def is_fit(font):
            text_height = fontInfo.getHeight(font)
            if text_height > h:
                return False

            text_width = 0
            for char in text_map:
                text_width += text_map[char] * fontInfo.getWidth(font, char)
            if text_width > w:
                return False
            return True

        def search_font(ptr_l, ptr_r):
            l_fit = is_fit(fonts[ptr_l])
            r_fit = is_fit(fonts[ptr_r])
            if r_fit:
                return fonts[ptr_r]
            if not l_fit:
                return -1
            if ptr_r - ptr_l <= 1:
                if l_fit:
                    # this step is cruitial. I made a mistake in thinking that a higher font always fits and a lower font never fits. IT's the other way round.
                    return fonts[ptr_l]

            ptr_mid = (ptr_l + ptr_r) // 2
            mid_fit = is_fit(fonts[ptr_mid])
            if mid_fit:
                return search_font(ptr_mid, ptr_r)
            else:
                return search_font(ptr_l, ptr_mid)

        return search_font(0, len(fonts) - 1)


if __name__ == '__main__':
    print(Solution().maxFont())
