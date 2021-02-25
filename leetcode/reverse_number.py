# This was a nice confidence booster to start my daily challenges
# I had seen the % technique one time so it was nice to test that out for myself

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0

        is_neg = False
        if x < 0:
            is_neg = True

        x = abs(x)
        low = -2**31
        high = 2**31 - 1
        reverse_x = 0
        while x > 0:
            reverse_x = (reverse_x * 10) + (x % 10)
            x = x // 10

        ans = -reverse_x if is_neg else reverse_x
        if ans > high or ans < low:
            return 0

        return ans
