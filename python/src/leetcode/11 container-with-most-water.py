# -*- coding: utf-8 -*-

# __author__ = xiaobao
# __date__ = 2019/10/17 22:57:09

# desc: desc

# 给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

# 说明：你不能倾斜容器，且 n 的值至少为 2。

# 示例:

# 输入: [1,8,6,2,5,4,8,3,7]
# 输出: 49

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/container-with-most-water
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def maxArea(self, height):
        nLen = len(height)

        if nLen <= 1:
            return 0

        nMax = 0
        for i in range(nLen-1):
            for j in range(i+1, nLen):
                nMax = max(nMax, min(height[i], height[j]) * (j - i))
        
        return nMax

solutionObj = Solution()
# height <= 1, return 0
assert(solutionObj.maxArea([]) == 0)
assert(solutionObj.maxArea([1]) == 0)
# height = 2  min(a,b) * fbs(a-b)
assert(solutionObj.maxArea([1,3]) == 1)
# height = 3 
## 12构成
assert(solutionObj.maxArea([4,3,1]) == 3)
## 23 构成
assert(solutionObj.maxArea([1,3,4]) == 3)
## 13 构成
assert(solutionObj.maxArea([2,3,4]) == 4)
# height > 3
## 遍历求最大值
# 其它
assert(solutionObj.maxArea([1,8,6,2,5,4,8,3,7]) == 49)