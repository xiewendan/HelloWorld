# -*- coding: utf-8 -*-

# __author__ = xiaobao
# __date__ = 2019/08/26 12:09:31

# desc: desc
class Solution:
    def reverse(self, x: int) -> int:
        nR = 0
        nZ = 1
        if x < 0:
            x = -x
            nZ = -1
        nMax = 1 << 32 -1
        while x != 0:
            nY = x % 10
            x = x // 10
            nR = nR * 10 + nY
            if nR > nMax:
                return 0
        nR = nR * nZ
        return nR