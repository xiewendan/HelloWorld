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

# 思路一 
# 1、统计每个数的个数，将相同元素去除
# 2、排序
# 3、将四个数之和转为三个数
# 4、将三个数之和转为两个数
# 5、两个数之和一次遍历，用dict缓存结果即可得到结果

# 注：常用减枝条件：判断target小于最小值，或大于最大值，可以提前结束

# 复杂度（时间/空间）
# 时间：排序 o(nlogn) + 四个数之和o(n*n*n) = o(n*n*n)
# 空间：需要用dict额外存储结果：o(n)

# 代码
# class Solution:
#     def oneSum(self, listDiffNums: List[int], nBeginIndex: int, nLen: int, dictNum2Count, target: int, listResult: List[int], value1: int, value2: int, value3: int):
#     # def oneSum(self, listDiffNums, nBeginIndex, nLen, dictNum2Count, target, listResult, value1, value2, value3):
#         if target in dictNum2Count and target > value3:
#             listResult.append([value1, value2, value3, target])

#     def twoSum(self, listDiffNums: List[int], nBeginIndex: int, nLen: int, dictNum2Count, target: int, listResult: List[int], value1: int, value2: int):
#     # def twoSum(self, listDiffNums, nBeginIndex, nLen, dictNum2Count, target, listResult, value1, value2):
#         if nBeginIndex >= nLen:
#             return

#         if target < 2 * listDiffNums[nBeginIndex] or target > 2 * listDiffNums[nLen - 1]:
#             return

#         for nIndex3 in range(nBeginIndex, nLen):
#             value3 = listDiffNums[nIndex3]
#             value3Count = dictNum2Count[value3]

#             self.oneSum(listDiffNums, nIndex3 + 1, nLen, dictNum2Count, target-value3, listResult, value1, value2, value3)

#         if True:
#             value3 = target / 2
#             if value3 > value2 and value3 in dictNum2Count and dictNum2Count[value3] >= 2:
#                 listResult.append([value1, value2, value3, value3])

#     def threeSum(self, listDiffNums: List[int], nBeginIndex: int, nLen: int, dictNum2Count, target: int, listResult: List[int], value1: int):
#     # def threeSum(self, listDiffNums, nBeginIndex, nLen, dictNum2Count, target, listResult, value1):
#         if nBeginIndex >= nLen:
#             return

#         if target < 3 * listDiffNums[nBeginIndex] or target > 3 * listDiffNums[nLen-1]:
#             return

#         for nIndex2 in range(nBeginIndex, nLen):
#             value2 = listDiffNums[nIndex2]
#             value2Count = dictNum2Count[value2]

#             self.twoSum(listDiffNums, nIndex2 + 1, nLen, dictNum2Count, target - value2, listResult, value1, value2)
            
#             if value2Count >= 2:
#                 self.oneSum(listDiffNums, nIndex2 + 1, nLen, dictNum2Count, target - 2 * value2, listResult, value1, value2, value2)

#         if True:
#             value2 = target / 3
#             if value2 >= value1 and value2 in dictNum2Count and dictNum2Count[value2] >= 3:
#                 listResult.append([value1, value2, value2, value2])

#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
#     # def fourSum(self, nums, target):
#         dictNum2Count = {}
#         listDiffNums = []
#         listResult = []

#         for value in nums:
#             if value in dictNum2Count:
#                 dictNum2Count[value] += 1
#             else:
#                 dictNum2Count[value] = 1
#                 listDiffNums.append(value)
        
#         listDiffNums.sort()

#         nLen = len(listDiffNums)
#         if nLen < 1:
#             return []

#         if target < 4 * listDiffNums[0] or target > 4 * listDiffNums[nLen - 1]:
#             return []

#         # 个数为1和个数为2
#         for nIndex1 in range(nLen):
#             value1 = listDiffNums[nIndex1]
#             value1Count = dictNum2Count[value1]

#             self.threeSum(listDiffNums, nIndex1 + 1, nLen, dictNum2Count, target - value1, listResult, value1)

#             if value1Count >= 2:
#                 self.twoSum(listDiffNums, nIndex1 + 1, nLen, dictNum2Count, target - 2 * value1, listResult, value1, value1)
            
#             if value1Count >= 3:
#                 self.oneSum(listDiffNums, nIndex1 + 1, nLen, dictNum2Count, target - 3 * value1, listResult, value1, value1, value1)

#         # 个数为4
#         if True:
#             value1 = target / 4
#             if value1 in dictNum2Count and dictNum2Count[value1] >= 4:
#                 listResult.append([value1, value1, value1, value1])
        
#         return listResult
    
# 思路二
# 两层变量
# 1、先删除超过四个的元素
# 2、处理四个相同元素
# 3、处理三个相同元素
# 4、排序
# 5、缓存两个数之和
# 6、将四个数之和转为两个数之和的问题
# 注：剪枝条件
class Solution:
    # def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    def fourSum(self, nums, target):
        dictNum2Count = {}
        listDiffNums = []

        listResult = []

        for value in nums:
            if value in dictNum2Count:
                dictNum2Count[value] += 1
            else:
                dictNum2Count[value] = 1
                listDiffNums.append(value)
        
        listDiffNums.sort()

        nLen = len(listDiffNums)
        if nLen < 1:
            return []

        if target < 4 * listDiffNums[0] or target > 4 * listDiffNums[nLen - 1]:
            return []
        
        # 四个相同的数
        if True:
            value1 = target / 4
            if value1 in dictNum2Count and dictNum2Count[value1] >= 4:
                listResult.append([value1, value1, value1, value1])
            
        # 三个相同的数
        for nIndex1 in range(nLen):
            value1 = listDiffNums[nIndex1]
            value1Count = dictNum2Count[value1]
            if value1Count >= 3:
                value2 = target - 3 * value1 

                if value2 in dictNum2Count and value2 != value1:
                    if value1 > value2:
                        listResult.append([value2, value1, value1, value1])
                    else:
                        listResult.append([value1, value1, value1, value2])

        # 其它情况：四个都不同；两个相同+两个不同；两个相同+两个相同
        dictTwoSum = {}

        minSum = 2 * listDiffNums[0]
        maxSum = 2 * listDiffNums[nLen-1]


        for nIndex1 in range(nLen):
            value1 = listDiffNums[nIndex1]
            value1Count = dictNum2Count[value1]

            # 剪枝
            if 2 * value1 + minSum > target:
                break

            # 剪枝
            if value1 + listDiffNums[-1] + maxSum < target:
                continue

            if value1Count >= 2:
                sum = value1 + value1

                if sum not in dictTwoSum:
                    dictTwoSum[sum] = [[nIndex1, nIndex1]]
                else:
                    dictTwoSum[sum].append([nIndex1, nIndex1])

            for nIndex2 in range( nIndex1 + 1, nLen):
                value2 = listDiffNums[nIndex2]
                sum = value1 + value2

                # 剪枝
                if sum + minSum > target:
                    break

                if sum not in dictTwoSum:
                    dictTwoSum[sum] = [[nIndex1, nIndex2]]
                else:
                    dictTwoSum[sum].append([nIndex1, nIndex2])
        
        dictSumEdit = {}
        for twoSum, listlistIndex in dictTwoSum.items():
            leftSum = target - twoSum

            if twoSum in dictSumEdit or leftSum in dictSumEdit:
                continue
            else:
                dictSumEdit[twoSum] = True
                dictSumEdit[leftSum] = True

                if leftSum in dictTwoSum:
                    leftListIndex = dictTwoSum[leftSum]

                    for listIndex in listlistIndex:
                        for leftIndex in leftListIndex:
                            if listIndex[0] not in leftIndex and listIndex[1] not in leftIndex:
                                result = sorted([listDiffNums[listIndex[0]], listDiffNums[listIndex[1]], listDiffNums[leftIndex[0]], listDiffNums[leftIndex[1]]])
                                if result not in listResult:
                                    listResult.append(result)
            
        return list(listResult)


def ListEqual(l1, l2):
    nLen1 = len(l1)
    nLen2 = len(l2)
    
    if nLen1 != nLen2:
        return False

    l1Temp = l1.copy()
    l2Temp = l2.copy()

    l1Temp.sort()
    l2Temp.sort()

    for i in range(nLen1):
        if l1Temp[i] != l2Temp[i]:
            return False
    
    return True

def ListListEqual(l1,l2):
    nLen1 = len(l1)
    nLen2 = len(l2)
    
    if nLen1 != nLen2:
        return False

    for i in range(nLen1):
        if not ListEqual(l1[i], l2[i]):
            return False
        
    return True




# 边界
solution = Solution()

# 元素个数 < 4:  返回空 list
assert(ListListEqual(solution.fourSum([], 0), []))
assert(ListListEqual(solution.fourSum([0], 0), []))
assert(ListListEqual(solution.fourSum([0, -2], 0), []))
assert(ListListEqual(solution.fourSum([0, -2, 2], 0), []))

# 元素个数 >= 4：
#  存在一组
#   四个元素相同：
assert(ListListEqual(solution.fourSum([1, 1, 1, 1], 4), [[1, 1, 1, 1]]))
assert(ListListEqual(solution.fourSum([1, 1, 1, 1], 5), []))
#  三个元素相同：
assert(ListListEqual(solution.fourSum([2, 1, 1, 1], 5), [[1, 1, 1, 2]]))
assert(ListListEqual(solution.fourSum([2, 1, 1, 1], 6), []))
#   两个元素相同：
print(solution.fourSum([2, 2, 1, 1], 6))

assert(ListListEqual(solution.fourSum([2, 2, 1, 1], 6), [[1, 1, 2, 2]]))
assert(ListListEqual(solution.fourSum([2, 2, 1, 1], 7), []))
#   没有元素相同
print(solution.fourSum([2, 3, 4, 1], 10))
assert(ListListEqual(solution.fourSum([2, 3, 4, 1], 10), [[1, 2, 3, 4]]))
assert(ListListEqual(solution.fourSum([2, 3, 4, 1], 11), []))

# 存在多组
assert(ListListEqual(solution.fourSum([1, 0, -1, 0, -2, 2], 0), [[-2, -1, 1, 2],[-2, 0, 0, 2], [-1, 0, 0, 1]]))
import datetime
timeNow = datetime.datetime.now()

for i  in range(1, 10):
    print(solution.fourSum([-491,-486,-481,-479,-463,-453,-405,-393,-388,-385,-381,-380,-347,-340,-334,-333,-326,-325,-321,-321,-318,-317,-269,-261,-252,-241,-233,-231,-209,-203,-203,-196,-187,-181,-169,-158,-138,-120,-111,-92,-86,-74,-33,-14,-13,-10,-5,-1,8,32,48,73,80,82,84,85,92,134,153,163,192,199,199,206,206,217,232,249,258,326,329,341,343,345,363,378,399,409,428,431,447,449,455,476,493], 2328))
print(datetime.datetime.now() - timeNow)


# 其它