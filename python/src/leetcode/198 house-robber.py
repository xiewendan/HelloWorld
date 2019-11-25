# -*- coding: utf-8 -*-

# __author__ = xiaobao
# __date__ = 2019/11/09 21:07:05

# desc: desc

# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

# 给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

# 示例 1:

# 输入: [1,2,3,1]
# 输出: 4
# 解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
#      偷窃到的最高金额 = 1 + 3 = 4 。
# 示例 2:

# 输入: [2,7,9,3,1]
# 输出: 12
# 解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
#      偷窃到的最高金额 = 2 + 9 + 1 = 12 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/house-robber
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 思路

# 代码
class Solution:
    # def rob(self, nums: List[int]) -> int:
    def rob(self, nums):
        nLen = len(nums)
        if nLen == 0:
            return 0
        if nLen <= 2:
            return max(nums)
        
        dp_pre2 = nums[0]
        dp_pre1 = max(nums[0:2])

        for i in range(2, nLen):
            temp = max(dp_pre1, dp_pre2 + nums[i])
            dp_pre2 = dp_pre1
            dp_pre1 = temp

        return dp_pre1
    
# 边界
solution = Solution()
# len(nums) == 0
assert(solution.rob([]) == 0)

# len(nums) == 1
assert(solution.rob([10]) == 10)

# len(nums) == 2
assert(solution.rob([10, 20]) == 20)
assert(solution.rob([20, 10]) == 20)

# len(nums) == 3
assert(solution.rob([10, 20, 15]) == 25)
assert(solution.rob([10, 40, 15]) == 40)

# 个数为0
assert(solution.rob([1,2,3,1]) == 4)
assert(solution.rob([2,7,9,3,1]) == 12)
