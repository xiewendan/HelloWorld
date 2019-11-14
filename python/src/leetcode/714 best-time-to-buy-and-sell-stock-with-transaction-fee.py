# -*- coding: utf-8 -*-

# __author__ = xiaobao
# __date__ = 2019/11/13 12:41:38

# desc: desc

# 给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。

# 你可以无限次地完成交易，但是你每次交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。

# 返回获得利润的最大值。

# 示例 1:

# 输入: prices = [1, 3, 2, 8, 4, 9], fee = 2
# 输出: 8
# 解释: 能够达到的最大利润:  
# 在此处买入 prices[0] = 1
# 在此处卖出 prices[3] = 8
# 在此处买入 prices[4] = 4
# 在此处卖出 prices[5] = 9
# 总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
# 注意:

# 0 < prices.length <= 50000.
# 0 < prices[i] < 50000.
# 0 <= fee < 50000.

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 思路

# 复杂度（时间/空间）
# 时间
# 空间
# 代码

import sys
class Solution:
    # def maxProfit(self, prices: List[int]) -> int:
    def maxProfit(self, prices, fee):
        nLen = len(prices)

        if nLen <= 1:
            return 0
        
        dp_i_0 = 0
        dp_i_1 = -sys.maxsize

        for i in range(nLen):
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, temp - prices[i] - fee)
        
        return dp_i_0
    
# 边界
solution = Solution()
## len(prices) <= 1
assert(solution.maxProfit([], 2) == 0)
assert(solution.maxProfit([1], 2) == 0)

## len(prices) = 2
assert(solution.maxProfit([1,4], 2) == 1)
assert(solution.maxProfit([4,1], 2) == 0)

## len(prices) = 3
assert(solution.maxProfit([1,4,8], 2) == 5)
assert(solution.maxProfit([1,8,4], 2) == 5)
assert(solution.maxProfit([4,1,8], 2) == 5)
assert(solution.maxProfit([4,8,1], 2) == 2)
assert(solution.maxProfit([8,1,4], 2) == 1)
assert(solution.maxProfit([8,4,1], 2) == 0)

## len(prices) >= 4
### 0次交易
assert(solution.maxProfit([7,6,4,3,1], 2) == 0)
### 1次交易
assert(solution.maxProfit([1,2,3,4,5], 2) == 2)
### 2次交易
assert(solution.maxProfit([7,1,5,3,6,4], 2) == 3)
### 3次交易
assert(solution.maxProfit([7,1,5,3,6,4,7], 2) == 4)



