# -*- coding: utf-8 -*-

# __author__ = xiaobao
# __date__ = 2019/10/25 12:21:19

# desc: 

# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

# 注意：

# 答案中不可以包含重复的四元组。

# 示例：

# 给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

# 满足要求的四元组集合为：
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/4sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 思路
# 1、排序
# 2、将四个数之和转为三个数
# 3、将三个数之和转为两个数
# 4、两个数之和一次遍历，用dict缓存结果即可得到结果

# 复杂度（时间/空间）
# 时间：排序 o(nlogn) + 四个数之和o(n*n*n) = o(n*n*n)
# 空间：需要用dict额外存储结果：o(n)

# 代码
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        pass
    
# 边界
# 
solution = Solution()
assert(solution)