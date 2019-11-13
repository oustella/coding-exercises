# https://leetcode.com/contest/weekly-contest-159/problems/check-if-it-is-a-straight-line/


def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
    try:
        check = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
        for i, c in enumerate(coordinates):
            if i > 0:
                k = (c[1] - coordinates[0][1]) / (c[0] - coordinates[0][0])
                if k != check:
                    return False
    except:  # when the line is parallel to y-axis, all x_i need to be equal
        for i, c in enumerate(coordinates):
            if c[0] != coordinates[0][0]:
                return False
    return True
