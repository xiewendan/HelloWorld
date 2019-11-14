# -*- coding: utf-8 -*-

# __author__ = xiaobao
# __date__ = 2019/11/13 12:39:48

# desc: desc

# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。

# 注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

# 示例 1:

# 输入: [2,4,1], k = 2
# 输出: 2
# 解释: 在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
# 示例 2:

# 输入: [3,2,6,5,0,3], k = 2
# 输出: 7
# 解释: 在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
#      随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 思路

# 复杂度（时间/空间）
# 时间
# 空间
# 代码
import sys
class Solution:
    # def maxProfit(self, k: int, prices: List[int]) -> int:
    def maxProfit(self, k, prices):
        nLen = len(prices)

        if nLen <= 1 or k == 0:
            return 0

        # k = 正无穷
        if k >= nLen//2:
            dp_i_0 = 0
            dp_i_1 = -sys.maxsize

            for i in range(nLen):
                temp = dp_i_0
                dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
                dp_i_1 = max(dp_i_1, temp - prices[i])
            
            return dp_i_0
        
        # k = 有限次数
        dp_i_k_0 = []
        for i in range(nLen+1):
            dp_i_k_0.append([0]*(k+1))

        dp_i_k_1 = []
        for i in range(nLen+1):
            dp_i_k_1.append([0]*(k+1))

        for j in range(k+1):
            dp_i_k_1[0][j] = -sys.maxsize
        for i in range(nLen+1):
            dp_i_k_1[i][0] = -sys.maxsize

        for i in range(1, nLen+1):
            for j in range(k,0,-1):
                dp_i_k_0[i][j] = max(dp_i_k_0[i-1][j], dp_i_k_1[i-1][j] + prices[i-1])
                dp_i_k_1[i][j] = max(dp_i_k_1[i-1][j], dp_i_k_0[i-1][j-1] - prices[i-1])
        

        return dp_i_k_0[nLen][k]
    
# 边界
solution = Solution()
## len(prices) <= 1
assert(solution.maxProfit(1, []) == 0)
assert(solution.maxProfit(1, [1]) == 0)

## len(prices) = 2
assert(solution.maxProfit(1, [1,4]) == 3)
assert(solution.maxProfit(2, [1,4]) == 3)
assert(solution.maxProfit(2, [4,1]) == 0)

## len(prices) = 3
assert(solution.maxProfit(1, [1,4,8]) == 7)
assert(solution.maxProfit(1, [1,8,4]) == 7)
assert(solution.maxProfit(1, [4,1,8]) == 7)
assert(solution.maxProfit(1, [4,8,1]) == 4)
assert(solution.maxProfit(1, [8,1,4]) == 3)
assert(solution.maxProfit(1, [8,4,1]) == 0)

## len(prices) >= 4
### 0次交易
assert(solution.maxProfit(1, [7,6,4,3,1]) == 0)
### 1次交易
assert(solution.maxProfit(1, [1,2,3,4,5]) == 4)
### 2次交易
assert(solution.maxProfit(1, [7,1,5,3,6,4]) == 5)
assert(solution.maxProfit(2, [7,1,5,3,6,4]) == 7)
### 3次交易
assert(solution.maxProfit(0, [7,1,5,3,6,4,7]) == 0)
assert(solution.maxProfit(1, [7,1,5,3,6,4,7]) == 6)
assert(solution.maxProfit(2, [7,1,5,3,6,4,7]) == 8)
assert(solution.maxProfit(3, [7,1,5,3,6,4,7]) == 10)
assert(solution.maxProfit(4, [7,1,5,3,6,4,7]) == 10)
assert(solution.maxProfit(5, [7,1,5,3,6,4,7]) == 10)