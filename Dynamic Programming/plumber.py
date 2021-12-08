from typing import List


def plumber(grid: List[str]) -> int:

    dp = []

    temp = []

    for i in range (len(grid)):

        dp.append([])

        temp.append([])

        for j in range (len(grid[0])):

            dp[i].append(0)

            temp[i].append(0)

    for i in range (len(grid)):

        for j in range (len(grid[0])):

            if grid[i][j] != 'x':

                if i - 1 != -1 and grid[i - 1][j] != 'x':

                    dp[i][j] = max(dp[i][j], dp[i - 1][j] + (1 if grid[i][j] == 'c' else 0));

                if j - 1 != -1 and grid[i][j - 1] != 'x':

                    dp[i][j] = max(dp[i][j], dp[i][j - 1] + (1 if grid[i][j] == 'c' else 0));

                if j + 1 != len(grid[0]) and grid[i][j + 1] != 'x':

                    dp[i][j] = max(dp[i][j], dp[i][j + 1] + (1 if grid[i][j]== 'c' else 0));
        print("dp \n", dp)
        for j in range (len(grid[0]) - 1, -1, -1):

            if grid[i][j] != 'x':

                if i - 1 != -1 and grid[i - 1][j] != 'x':

                    temp[i][j] = max(temp[i][j], temp[i - 1][j] + (1 if grid[i][j] == 'c' else 0));

                if j - 1 != -1 and grid[i][j - 1] != 'x':

                    temp[i][j] = max(temp[i][j], temp[i][j - 1] + (1 if grid[i][j] == 'c' else 0));

                if j + 1 != len(grid[0]) and grid[i][j + 1] != 'x':

                    temp[i][j] = max(temp[i][j], temp[i][j + 1] + (1 if grid[i][j]== 'c' else 0));
        print('temp \n', temp)
        for j in range (len(grid[0])):

            dp[i][j] = max(dp[i][j], temp[i][j])

            temp[i][j] = dp[i][j]

    return dp[len(grid) - 1][len(grid[0]) - 1]


if __name__ == '__main__':

    # grid = [[".", "x", "c"], ["c", "c", "."]]
    grid = [[".", "x", "c", "c"], [".", ".", ".", "."]]

    res = plumber(grid)

    print(res)