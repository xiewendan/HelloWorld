# -*- coding: utf-8 -*-

# __author__ = xiaobao
# __date__ = 2019/10/18 12:02:49

# desc: desc

# 输入: [1,8,6,2,5,4,8,3,7]
# 输出: 49

class Solution:
    def maxArea(self, height) -> int:
        nLen = len(height)

        if nLen <= 1:
            return 0

        nLeftIndex = 0
        nRightIndex = nLen - 1
        nMaxLeftHeight = height[nLeftIndex]
        nMaxRightHeight = height[nRightIndex]

        nMaxArea = 0
        
        while(nLeftIndex < nRightIndex):
            nMaxArea = max(nMaxArea, (nRightIndex - nLeftIndex) * min(nMaxLeftHeight, nMaxRightHeight))
            if nMaxLeftHeight < nMaxRightHeight:
                while(nLeftIndex < nRightIndex):
                    nLeftIndex += 1
                
                    if nMaxLeftHeight < height[nLeftIndex]:
                        nMaxLeftHeight = height[nLeftIndex]
                        break

            else:
                while(nLeftIndex < nRightIndex):
                    nRightIndex -= 1
                    if nMaxRightHeight < height[nRightIndex]:
                        nMaxRightHeight = height[nRightIndex]
                        break
        
        return nMaxArea

solution = Solution()
assert(solution.maxArea([1,8,6,2,5,4,8,3,7]) == 49)