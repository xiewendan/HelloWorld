# -*- coding: utf-8 -*-

# __author__ = xiaobao
# __date__ = 2019/11/12 19:15:43

# desc: desc
# 给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。

# 示例:

# 输入: 3
# 输出:
# [
#   [1,null,3,2],
#   [3,2,null,1],
#   [3,1,null,null,2],
#   [2,1,3],
#   [1,null,2,null,3]
# ]
# 解释:
# 以上的输出对应以下 5 种不同结构的二叉搜索树：

#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/unique-binary-search-trees-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 思路
# 

# 复杂度（时间/空间）
# 时间
# 空间
# 代码
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # def generateTrees(self, n: int) -> List[TreeNode]:
    def generateTrees(self, n):
        if n == 0:
            return []

        return self.generateTreesByStartEnd(1,n)
    
    def generateTreesByStartEnd(self, nStart, nEnd):
        if nStart > nEnd:
            return [None]

        if nStart == nEnd:
            return [TreeNode(nStart)]
        
        listTrees = []
        for i in range(nStart, nEnd + 1):
            leftTrees = self.generateTreesByStartEnd(nStart, i-1)
            rightTrees = self.generateTreesByStartEnd(i+1, nEnd)

            for leftTree in leftTrees:
                for rightTree in rightTrees:
                    middleTree = TreeNode(i)
                    middleTree.left = leftTree
                    middleTree.right = rightTree
                    listTrees.append(middleTree)
        
        return listTrees
    
# 边界
solution = Solution()
print(solution.generateTrees(0))
print(solution.generateTrees(1))
print(solution.generateTrees(2))
a = solution.generateTrees(3)
print(a)