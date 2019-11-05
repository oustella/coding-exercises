# Given a 9x9 array. Check if the filled nums satisfy Sudoku rules

from collections import Counter  # Note Counter is capitalized

def sudoku2(grid):

    print('checking rows...')
    for row in grid:
        counts = Counter(row)
        for key, val in counts.items():
            if key != '.' and val != 1:
                return False

    print('checking columns...')
    for c in range(len(grid)):  # need to start the for loop with column
        col_tracker = []  # this is where you need to initiate a new column checker
        for r in range(len(grid)):
            if grid[r][c] != '.':
                if grid[r][c] not in col_tracker:
                    col_tracker.append(grid[r][c])
                else:
                    return False

    print('checking blocks...')
    block_rows = [0, 3, 6]  # find the upper left corner of every 3x3 block.
    block_columns = [0, 3, 6]
    for i in block_rows:  # use nested for loops to formulate the 9 starting point of a block
        for j in block_columns:
            block = [x[j:j + 3] for x in grid[i:i + 3]]  # creates the block for checking. This line is the MEAT.
            block_tracker = []  # initiate tracker AFTER the block is created
            for row in block:
                for val in row:
                    if val != '.':
                        if val not in block_tracker:
                            block_tracker.append(val)
                        else:
                            return False

    return True


# Note there are repeated codes for checking duplicates that should be avoided by creating a universal helper function.


# Another way of traversing through a column of an array is
def getColumns(arr):
    for i in range(len(arr)):
        column = [row[i] for row in arr]
        print(column)


test_arr = [
        [".",".",".","1","4",".",".","2","."],
        [".",".","6",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".","1",".",".",".",".",".","."],
        [".","6","7",".",".",".",".",".","9"],
        [".",".",".",".",".",".","8","1","."],
        [".","3",".",".",".",".",".",".","6"],
        [".",".",".",".",".","7",".",".","."],
        [".",".",".","5",".",".",".","7","."]
]

getColumns(test_arr)




