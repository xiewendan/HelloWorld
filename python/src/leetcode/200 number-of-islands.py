# -*- coding: utf-8 -*-

# __author__ = xiaobao
# __date__ = 2019/12/28 15:41:18

# desc: desc

# 给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。

# 示例 1:

# 输入:
# 11110
# 11010
# 11000
# 00000

# 输出: 1
# 示例 2:

# 输入:
# 11000
# 11000
# 00100
# 00011

# 输出: 3

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/number-of-islands
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 思路
# 先从一个之前未访问过的点开始，广度遍历，直到没有遍历完，那么这些点是属于一个点
# 然后再找下一个未访问过的点

# 代码

# 广度遍历
# class Solution:
#     def numIslands(self, grid) -> int:
#         nRow = len(grid)
#         if nRow == 0:
#             return 0
#         nCol = len(grid[0])

#         gridTaken = []
#         for i in range(nRow):
#             gridTaken.append([0] * nCol)

#         listQueue = []
#         nIslandCount = 0
#         for i, RowData in enumerate(grid):
#             for j, nValue in enumerate(RowData):
#                 if nValue == "1" and gridTaken[i][j] == 0:
#                     nIslandCount += 1
#                     gridTaken[i][j] = 1
#                     listQueue.append((i, j))

#                     while listQueue:
#                         nX, nY = listQueue.pop(0)
#                         nNextX, nNextY = nX + 1, nY + 1
#                         nPreX, nPreY = nX - 1, nY - 1

#                         if nNextX < nRow and grid[nNextX][nY] == "1" and gridTaken[nNextX][nY] == 0:
#                             gridTaken[nNextX][nY] = 1
#                             listQueue.append((nNextX, nY))
#                         if nNextY < nCol and grid[nX][nNextY] == "1" and gridTaken[nX][nNextY] == 0:
#                             gridTaken[nX][nNextY] = 1
#                             listQueue.append((nX, nNextY))
#                         if nPreX >=0 and grid[nPreX][nY] == "1" and gridTaken[nPreX][nY] == 0:
#                             gridTaken[nPreX][nY] = 1
#                             listQueue.append((nPreX, nY))
#                         if nPreY >= 0 and grid[nX][nPreY] == "1" and gridTaken[nX][nPreY] == 0:
#                             gridTaken[nX][nPreY] = 1
#                             listQueue.append((nX, nPreY))

#         return nIslandCount

# 深度遍历，基于调用栈，先序遍历
class Solution:
    def numIslands(self, grid) -> int:
        nRow = len(grid)
        if nRow == 0:
            return 0
        nCol = len(grid[0])

        gridTaken = []
        for _ in range(nRow):
            gridTaken.append([0] * nCol)
        
        nIslandsCount = 0
        for i, RowData in enumerate(grid):
            for j, nValue in enumerate(RowData):
                if nValue == "1" and gridTaken[i][j] == 0:
                    nIslandsCount += 1
                    self.DFS(i,j,grid, gridTaken, nRow, nCol)
        
        return nIslandsCount

    
    def DFS(self, i, j, grid, gridTaken, nRow, nCol):
        gridTaken[i][j] = 1

        listNextPos = [(i+1,j), (i,j+1), (i-1,j), (i,j-1)]
        for nextPos in listNextPos:
            nextX, nextY = nextPos

            if 0 <= nextX < nRow and 0 <= nextY < nCol and grid[nextX][nextY] == "1" and gridTaken[nextX][nextY] == 0:
                self.DFS(nextX, nextY, grid, gridTaken, nRow, nCol)

# 深度遍历，基于栈
# class Solution:
#     def numIslands(self, grid) -> int:
#         pass

# 边界
solution = Solution()

# 0X0
assert(solution.numIslands([[]]) == 0)

# 1X1
assert(solution.numIslands([["1"]]) == 1)
assert(solution.numIslands([["0"]]) == 0)

# 1X2
assert(solution.numIslands([["1", "0"]]) == 1)
assert(solution.numIslands([["1", "1"]]) == 1)
assert(solution.numIslands([["0", "1"]]) == 1)
assert(solution.numIslands([["0", "0"]]) == 0)

# 2X2
assert(solution.numIslands([["1", "1"], ["1", "1"]]) == 1)
assert(solution.numIslands([["1", "0"], ["0", "1"]]) == 2)

# 其它
assert(solution.numIslands(
    [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]) == 1)
assert(solution.numIslands(
    [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]) == 3)

assert(solution.numIslands(
    [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]) == 1)

assert(solution.numIslands(
    [["1","1","1"],["0","1","0"],["1","1","1"]]) == 1)
