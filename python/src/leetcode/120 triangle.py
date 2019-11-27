# -*- coding: utf-8 -*-

# __author__ = xiaobao
# __date__ = 2019/11/15 08:59:53

# desc: desc

# 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

# 例如，给定三角形：

# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# 自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

# 说明：

# 如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/triangle
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# 思路

# 复杂度（时间/空间）
# 时间
# 空间
# 代码
class Solution:
    # def minimumTotal(self, triangle: List[List[int]]) -> int:
    def minimumTotal(self, triangle):
        nLen = len(triangle)

        if nLen == 0:
            return 0

        dp_sum = [0] * nLen
        dp_lastsum = [0] * nLen

        dp_lastsum[0] = triangle[0][0]
        
        for i in range(1, nLen):
            dp_sum[0] = triangle[i][0] + dp_lastsum[0]
            dp_sum[i] = triangle[i][i] + dp_lastsum[i-1]
            for j in range(1, i):
                dp_sum[j] = triangle[i][j] + min(dp_lastsum[j], dp_lastsum[j-1])

            dp_sum, dp_lastsum = dp_lastsum, dp_sum
        
        minValue = dp_lastsum[0]
        for i in range(1, nLen):
            minValue = min(minValue, dp_lastsum[i])
        
        return minValue

    
# 边界
solution = Solution()

# 0 行
assert(solution.minimumTotal([]) == 0)

# 1 行
assert(solution.minimumTotal([[1]]) == 1)

# 2 行
assert(solution.minimumTotal([[2], [3,4]]) == 5)

# n 行
assert(solution.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]) == 11)