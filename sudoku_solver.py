import numpy as np

def possible_fills(grid, row, col):
    '''
    Function to calculate possible numbers can be filled in grid[row][col]

    Attributes:
        grid: current state of sudoku grid
        row: row of the empty slot
        col: column of the empty slot
    '''
    nums = set(range(1,10))
    res = nums
    # check against existing numbers in row
    p_fills_row = nums - set(grid[row]) - {0}
    res = res.intersection(p_fills_row)
    # check against existing numbers in column
    p_fills_col = nums - set([grid[i][col] for i in range(9)])
    res = res.intersection(p_fills_col)
    # check against existing numbers in subgrid
    subgrid_row = (row//3)*3
    subgrid_col = (col//3)*3
    p_fills_subgrid = nums - set([grid[i][j] for i in range(subgrid_row, subgrid_row+3) for j in range(subgrid_col, subgrid_col+3)])
    res = res.intersection(p_fills_subgrid)
    return list(res)

def sudoku_solver(grid):
    return fill_sudoku(grid, 0, 0)

def fill_sudoku(grid, row, col):
    '''
    DFS algorithm to find empty slots in sudoku and fill them with possible numbers

    Attributes:
        grid: current state of sudoku grid
        row: row of the slot to start the check
        col: column of the slot to start the check
    '''
    i = row
    j = col
    res = None
    while i < 9:
        while j < 9:
            if grid[i][j] == 0:
                # get possible fills
                p_fills = possible_fills(grid, i, j)
                # if no possible fills for this slot, DFS root fails, return None
                if not p_fills:
                    return res
                else:
                    # try all possible fills for this slot with DFS
                    for fill in p_fills:
                        grid[i][j] = fill
                        new = np.copy(grid)
                        res = fill_sudoku(new, i, j)
                        # if solution found, return solution
                        if type(res) != type(None):
                            return res
                    return res
            j += 1
        j = 0
        i += 1
    return grid

def print_sudoku(grid):
    for row in grid:
        print(row)


if __name__ == '__main__':
    # Define the Sudoku grid
    matrix = [
        [0, 1, 0, 9, 0, 2, 0, 8, 7],
        [0, 6, 3, 0, 8, 5, 0, 0, 0],
        [0, 2, 0, 0, 7, 0, 5, 1, 6],
        [0, 5, 7, 0, 9, 6, 0, 0, 3],
        [3, 0, 6, 2, 1, 0, 7, 0, 4],
        [0, 0, 4, 7, 0, 3, 0, 0, 0],
        [0, 0, 2, 0, 3, 0, 0, 4, 0],
        [8, 0, 0, 0, 4, 9, 0, 0, 5],
        [0, 0, 0, 8, 0, 0, 0, 3, 1]
    ]

    grid = np.array(matrix)
    new_grid = sudoku_solver(grid)
    if type(new_grid) != type(None):
        print_sudoku(new_grid)
    else:
        print('No solution exists')