grid =  [
    [1,1,1,1,0],
    [1,1,0,1,0],
    [1,1,0,0,1],
    [0,0,1,0,0]
]
from collections import deque


def get_no_of_islands(grid):
    if not grid:
        return 0
    
    def bfs(r,c):
        queue = deque([(r,c)])
        visited.add((r,c))
        
        while queue:
            row,col = queue.popleft()
            directions = [(1,0), (0,1), (0,-1), (-1,0)]
            for dr, dc in directions:
                r = row + dr
                c = col + dc
                if r in range(rows) and c in range(cols) and (r,c) not in visited and grid[r][c] == 1:
                    queue.append((r,c))
                    visited.add((r,c))
    
    visited = set()
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1 and (row, col) not in visited:
                bfs(row, col)
                count += 1
                
    return count      
        

def main():
    print(get_no_of_islands(grid))
    
if  __name__ == '__main__':
    main()
    