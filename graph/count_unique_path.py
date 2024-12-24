grid = [[0,0,0,0], [1,1,0,0],[0,0,0,1],[0,1,0,0]]


def count_unique_path(grid, r, c, visit):
    ROWS, COLS = len(grid), len(grid[0])

    if (min(r,c)<0 or r == ROWS or c==COLS or (r,c) in visit or grid[r][c]==1):
        return 0
    if r==ROWS-1 and c==COLS-1:
        return 1

    visit.add((r,c))

    count = 0
    count+= count_unique_path(grid,r-1,c, visit)
    count+= count_unique_path(grid, r+1, c, visit)
    count+= count_unique_path(grid,r, c-1, visit)
    count+= count_unique_path(grid, r, c+1, visit)

    visit.remove((r,c))
    return count


print(count_unique_path(grid,0,0, set()))
