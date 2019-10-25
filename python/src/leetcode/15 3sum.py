# -*- coding: utf-8 -*-

# __author__ = xiaobao
# __date__ = 2019/08/27 09:10:57

# desc: desc
# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

# 注意：答案中不可以包含重复的三元组。

# 例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/3sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def threeSum(self, nums):
        if len(nums) <= 2:
            return []

        dictCount = {}
        for i in nums:
            dictCount[i] = dictCount.get(i,0) + 1

        nums = sorted(dictCount)
        nMaxRight = len(nums) - 1

        listReturn = []
        dictInSum = {}

        for i, nValue0 in enumerate(nums):
            if dictCount[nValue0] > 1:
                if nValue0 == 0:
                    if dictCount[nValue0] > 2:
                        listReturn.append([0,0,0])
                else:
                    if -2*nValue0 in dictCount:
                        listReturn.append([nValue0, nValue0, -2*nValue0])

            if nValue0 < 0:
                nSum = -nValue0
                nLeft = i + 1
                nRight = nMaxRight
                while nLeft < nRight:
                    nSumTemp = nums[nLeft] + nums[nRight]
                    if nSumTemp > nSum:
                        nRight = nRight - 1
                    elif nSumTemp < nSum:
                        nLeft = nLeft + 1
                    else:
                        listReturn.append([nValue0, nums[nLeft], nums[nRight]])
                        nLeft = nLeft + 1
                        nRight = nRight - 1

        return listReturn

    def threeSum1(self, nums):
        ans=[]
        counts={}
        for i in nums:
            counts[i] = counts.get(i, 0) + 1
        nums=sorted(counts)
        for i,num in enumerate(nums):
            if counts[num]>1:
                if num==0:
                    if counts[num]>2:
                        ans.append([0,0,0])
                else:
                    if -num*2 in nums:
                        ans.append([num,num,-2*num])
            if num<0:
                twosum=-num
                left=bisect.bisect_left(nums,(twosum-nums[-1]),i+1)
                for i in nums[left:bisect.bisect_right(nums,(twosum//2),left)]:
                    j=twosum-i
                    if j in counts and j!=i:
                        ans.append([num,i,j])
        return ans

solution = Solution()
assert(len(solution.threeSum([-1, 0]))==0) # 不足三个数
assert(len(solution.threeSum([-1, 0, 2]))==0)  # 三个数，但组合个数为0
assert(len(solution.threeSum([-1, 0, 1]))==1)  # 三个数，有一个组合
assert(len(solution.threeSum([-1, 0, 1, -1]))==1)  # 三个数，有一个组合，且还存在重复组合数
assert(len(solution.threeSum([-1, 0, 1, 2, -1, -4]))==2) # 正常情况

print(solution.threeSum([-1, 0, 1, 2, -1, -4]))