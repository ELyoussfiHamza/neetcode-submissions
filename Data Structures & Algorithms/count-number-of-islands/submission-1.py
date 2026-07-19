class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def MarkTheIsland(i,j,grid,visited):
            if visited.get((i, j), False) or grid[i][j]=="0":
                return
            visited[i,j] = True
            if i+1<len(grid):
                MarkTheIsland(i+1,j,grid,visited)
            if i-1>=0:
                MarkTheIsland(i-1,j,grid,visited)
            if j+1<len(grid[0]):
                MarkTheIsland(i,j+1,grid,visited)
            if j-1>=0:
                MarkTheIsland(i,j-1,grid,visited)
        start = (0,0)
        visited  = {} # tuple <==> boolean 
        n = len(grid)
        m = len(grid[0])
        counter = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]=="1" and not visited.get((i, j), False):
                    MarkTheIsland(i,j,grid,visited)
                    counter+=1
        return counter
        