# https://leetcode.com/problems/rotate-image/submissions/
# Given a 2D nxn matrix, rotate it by 90 degrees clockwise in place.

matrix = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]

# rotated matrix should become
# [
#   [15,13, 2, 5],
#   [14, 3, 4, 1],
#   [12, 6, 8, 9],
#   [16, 7,10,11]
# ]

# [1] termination condition based on four numbers need to switch places
# [2] the most important thing is to figure out the rotated indices relationship
# (i, j) -> (j, n-1-i)
# [3] rotate the matrix one hollow square at a time
# i controls the ith hollow square. If n = 4, there are 4/2=2 squares.
# If n = 5, there are 5//2 = 2 squares. The center piece one number does not need rotation.
# j controls the numbers that are needed to intiate the four-way rotation
# These are numbers on the top edge of a square but leaving the upper right corner alone
# E.g. To rotate:
# 5  1  9  11
# 2        10
# 13       7
# 15 14 12 16
# Only 5, 1, 9 need to intiate the rotate helper
# Another example, if n = 6, then the inner most hollow square has range(6//2) = [0,1,2]
# when i = 2, n-i = 4, ie the 3rd row, 4th number of the matrix is the upper right corner of the sub square
# then we want one number to the left of the upper right corner n-i-1 = 3
# then range(i, n-i-1) gets us the correct indices range(2,3) = [2]

def rotate(matrix):
    if len(matrix) <= 1:
        return
    
    def rotate_helper(matrix, i, j, target, count):
        if count == 4:  # [1]
            return
        n = len(matrix)-1
        count += 1
        save = matrix[j][n-i]  # [2] save the destination number for next
        matrix[j][n-i] = target
        rotate_helper(matrix, j, n-i, save, count)
    
    width = len(matrix)
    for i in range(width//2):  # [3]
        for j in range(i, width-i-1):  # [3]
            rotate_helper(matrix, i, j, matrix[i][j], 0)

rotate(matrix)
print(matrix)

# Another solution without the helper
# [4] the key for this approach is that only one number needs to be saved aside
# because the number that gets replaced has already been transferred
def rotate(matrix):
    if len(matrix) <= 1:
        return   
    width = len(matrix)
    for i in range(width//2):  # [3]
        for j in range(i, width-i-1):  # [3]
            temp = matrix[i][j] # [4] save the destination number for next
            matrix[i][j] = matrix[j][width-1-i]
            matrix[j][width-1-i] = matrix[width-1-i][width-1-j]
            matrix[width-1-i][width-1-j] = matrix[width-1-j][i]
            matrix[width-1-j][i] = temp

rotate(matrix)
print(matrix)


