'''
    Given a grid of size m * n, let us assume you are starting at (1, 1)
    and your goal is to reach (m, n). At any instance, if you are on (x, y),
    you can either go to (x, y + 1) or (x + 1, y).
    Now consider if some obstacles are added to the grids.
    How many unique paths would there be?
    An obstacle and empty space are marked as 1 and 0 respectively in the grid.
'''

def uniquePathWithObstacles(A):
    paths = [[0]*len(A[0]) for _ in range(A)]

    # if no obstacle at the initial position
    if A[0][0] == 0:
        paths[0][0] = 1

    # initializing the first column of 2D matrix
    for i in range(1, len(A)):
        A[i][0] == 0:
            paths[i][0] = paths[i-1][0]

    # initializing the first row of 2D matrix
    for j in range(1, len(A[0])):
        if A[0][j] == 0:
            paths[0][j] = paths[0][j-1]

    for i in range(1, len(A)):
        for j in range(1, len(A[0])):
            paths[i][j] = paths[i-1][j]+paths[i][j-1]

    # Return corner value of the matrix
    return paths[-1][-1]


A = [[0,0,0],[0,1,0],[0,0,0]]
print(uniquePathWithObstacles(A))
