# -*- coding: utf-8 -*-

# __author__ = xiaobao
# __date__ = 2019/11/13 12:38:07

# desc: desc

# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

# 设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

# 示例 1:

# 输入: [7,1,5,3,6,4]
# 输出: 7
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
#      随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
# 示例 2:

# 输入: [1,2,3,4,5]
# 输出: 4
# 解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
#      注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
#      因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
# 示例 3:

# 输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 思路
# 动态规划

# 复杂度（时间/空间）
# 时间 
# 空间 
# 代码
import sys
class Solution:
    # def maxProfit(self, prices: List[int]) -> int:
    def maxProfit(self, prices):
        nLen = len(prices)

        if nLen <= 1:
            return 0
        
        dp_i_0 = 0
        dp_i_1 = -sys.maxsize

        for i in range(nLen):
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, temp - prices[i])
        
        return dp_i_0
    
# 边界
solution = Solution()
## len(prices) <= 1
assert(solution.maxProfit([]) == 0)
assert(solution.maxProfit([1]) == 0)

## len(prices) = 2
assert(solution.maxProfit([1,4]) == 3)
assert(solution.maxProfit([4,1]) == 0)

## len(prices) = 3
assert(solution.maxProfit([1,4,8]) == 7)
assert(solution.maxProfit([1,8,4]) == 7)
assert(solution.maxProfit([4,1,8]) == 7)
assert(solution.maxProfit([4,8,1]) == 4)
assert(solution.maxProfit([8,1,4]) == 3)
assert(solution.maxProfit([8,4,1]) == 0)

## len(prices) >= 4
### 0次交易
assert(solution.maxProfit([7,6,4,3,1]) == 0)
### 1次交易
assert(solution.maxProfit([1,2,3,4,5]) == 4)
### 2次交易
assert(solution.maxProfit([7,1,5,3,6,4]) == 7)
### 3次交易
assert(solution.maxProfit([7,1,5,3,6,4,7]) == 10)
