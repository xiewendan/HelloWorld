# -*- coding: utf-8 -*-

# __author__ = xiaobao
# __date__ = 2019/11/09 18:42:47

# desc: desc

# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

# 如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

# 注意你不能在买入股票前卖出股票。

# 示例 1:

# 输入: [7,1,5,3,6,4]
# 输出: 5
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
#      注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
# 示例 2:

# 输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 思路
# 将当前值减去之前的最小值，如果大于最大收益，则覆盖，否则继续往后

# 代码
class Solution:
    def maxProfit(self, prices) -> int:
        nLen = len(prices)
        if nLen <= 1:
            return 0

        nMin = prices[0]
        nMaxProfit = 0
        for i in range(1, nLen):
            nMin = min(nMin, prices[i])
            nMaxProfit = max(nMaxProfit, prices[i] - nMin)

        return nMaxProfit
    
# 边界
solution = Solution()

# len(prices) <= 1
assert(solution.maxProfit([]) == 0)
assert(solution.maxProfit([1]) == 0)

# len(prices) == 2
assert(solution.maxProfit([2,1]) == 0)
assert(solution.maxProfit([1,4]) == 3)

# len(prices) == 3
assert(solution.maxProfit([1,4,7]) == 6)
assert(solution.maxProfit([1,7,4]) == 6)
assert(solution.maxProfit([4,1,7]) == 6)
assert(solution.maxProfit([4,7,1]) == 3)
assert(solution.maxProfit([7,4,1]) == 0)
assert(solution.maxProfit([7,1,4]) == 3)

# 其它
assert(solution.maxProfit([7,1,5,3,6,4]) == 5)
assert(solution.maxProfit([7,6,4,3,1]) == 0)
