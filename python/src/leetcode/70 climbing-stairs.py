# -*- coding: utf-8 -*-

# __author__ = xiaobao
# __date__ = 2019/11/08 19:28:47

# desc: desc

# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

# 注意：给定 n 是一个正整数。

# 示例 1：

# 输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶
# 示例 2：

# 输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/climbing-stairs
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 思路
# 动态规划
# dp_step[n] = dp_step[n-1] + dp_step[n-2]
# dp_step[1] = 1
# dp_step[2] = 2

# 复杂度（时间/空间）
# 时间 o(n)
# 空间 o(1)
# 代码
class Solution:
    def climbStairs(self, n: int) -> int:
        assert(n>0)
        if n <= 2:
            return n
        
        dp_step_pre2 = 1
        dp_step_pre1 = 2
        dp_step = 0
        for i in range(3, n+1):
            dp_step = dp_step_pre1 + dp_step_pre2
            dp_step_pre2 = dp_step_pre1
            dp_step_pre1 = dp_step
        
        return dp_step
    
# 边界
solution = Solution()
assert(solution.climbStairs(1) == 1)
assert(solution.climbStairs(2) == 2)
assert(solution.climbStairs(3) == 3)
assert(solution.climbStairs(4) == 5)