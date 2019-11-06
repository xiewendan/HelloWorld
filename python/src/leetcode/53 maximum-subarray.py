# -*- coding: utf-8 -*-

# __author__ = xiaobao
# __date__ = 2019/11/06 19:12:23

# desc: desc

# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

# 示例:

# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
# 进阶:

# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximum-subarray
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# 思路

# 复杂度（时间/空间）
# 时间
# 空间
# 代码
class Solution:
    # o(n*n*n)
    # def maxSubArray(self, nums: List[int]) -> int:
    # def maxSubArray(self, nums):
    #     nLen = len(nums)
    #     assert(nLen > 0 )

    #     nMax = nums[0]
    #     for i in range(nLen):
    #         for j in range(i, nLen):
    #             sum = 0
    #             for k in range(i,j+1):
    #                 sum += nums[k]
    #             if sum > nMax:
    #                 nMax = sum

    #     return nMax

    # o(n*n)
    # def maxSubArray(self, nums: List[int]) -> int:
    # # def maxSubArray(self, nums):
    #     nLen = len(nums)
    #     assert(nLen > 0 )

    #     listMaxSum = [ 0 for i in range(nLen)]
    #     listMaxSum[0] = nums[0]
    #     for i in range(1, nLen):
    #         # i开始往前加的最大值
    #         sum = 0
    #         nMaxSum = nums[i]
    #         for j in range(i,-1,-1):
    #             sum += nums[j]
    #             nMaxSum = max(nMaxSum, sum)

    #             # 剪枝
    #             if sum < 0:
    #                 break
    #             if j > 0 and nMaxSum + listMaxSum[j-1] < listMaxSum[i-1]:
    #                 break
            
    #         # 比较 maxsum和listMaxSum[i-1]
    #         listMaxSum[i] = max(nMaxSum, listMaxSum[i-1])
        
    #     return listMaxSum[nLen-1]

    # o(n)
    # def maxSubArray(self, nums: List[int]) -> int:
    def maxSubArray(self, nums):
        pass


    
# 边界
solution = Solution()
assert(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])==6)

## 一个元素
assert(solution.maxSubArray([-2])==-2)      # 负数
assert(solution.maxSubArray([0])==0)      # 0
assert(solution.maxSubArray([2])==2)      # 正数

## 两个元素
assert(solution.maxSubArray([-2, -1])==-1)      # 负数
assert(solution.maxSubArray([0,0])==0)      # 0
assert(solution.maxSubArray([2,1])==3)      # 正数
assert(solution.maxSubArray([-2, 1])==1)      # 一个正，一个负数


