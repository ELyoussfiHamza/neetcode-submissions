class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()

        n = len(grid)
        m =len(grid[0])

        for i in range(n):
            for j in range(m):
                if (not grid[i][j]):
                    queue.appendleft((i,j))
        #Now we have a queue of treasures 

        # This is a trick  to avoid redundancy in thecode when you work on grids

        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        while (len(queue)!=0):
            (x,y) = queue.popleft()
            for (dx,dy) in directions:
                cell_x = dx+x
                cell_y = dy + y
                if 0<=cell_x<n and 0<=cell_y<m and grid[cell_x][cell_y] == 2147483647:
                    grid[cell_x][cell_y] = grid[x][y] + 1
                    queue.append((cell_x,cell_y))
            