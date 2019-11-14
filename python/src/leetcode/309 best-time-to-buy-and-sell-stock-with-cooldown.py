# -*- coding: utf-8 -*-

# __author__ = xiaobao
# __date__ = 2019/11/13 12:40:44

# desc: desc

# 给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​

# 设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

# 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
# 示例:

# 输入: [1,2,3,0,2]
# 输出: 3 
# 解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 思路

# 复杂度（时间/空间）
# 时间
# 空间
# 代码
import sys
class Solution:
    # def maxProfit(self, prices: List[int]) -> int:
    def maxProfit(self, prices) -> int:
        nLen = len(prices)

        if nLen <= 1:
            return 0

        dp_i_0 = [0] * (nLen+1)
        dp_i_1 = [-sys.maxsize] * (nLen+1)

        for i in range(1, nLen+1):
            dp_i_0[i] = max(dp_i_0[i-1], dp_i_1[i-1] + prices[i-1])

            if i == 1:
                dp_i_1[i] = max(dp_i_1[i-1], - prices[i-1])
            else:
                dp_i_1[i] = max(dp_i_1[i-1], dp_i_0[i-2] - prices[i-1])

        
        return dp_i_0[nLen]
    
# 边界
solution = Solution()
## len(prices) <= 1
# assert(solution.maxProfit([]) == 0)
# assert(solution.maxProfit([1]) == 0)

## len(prices) = 2
assert(solution.maxProfit([1,4]) == 3)
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
assert(solution.maxProfit([7,1,5,3,6,4]) == 5)
assert(solution.maxProfit([7,1,5,1,3,6,4]) == 7)
### 3次交易
assert(solution.maxProfit([7,1,5,3,6,4,7]) == 7)   # 两次交易
assert(solution.maxProfit([7,1,5,5,3,6,4,7]) == 8) # 两次交易
assert(solution.maxProfit([7,1,5,5,3,6,6,4,7]) == 10)   # 三次交易