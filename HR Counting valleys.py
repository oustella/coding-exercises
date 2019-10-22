def countingValleys(n, s):
    count = 0
    level = 0

    for step in s:
        if step == "U":
            level += 1
            if level == 0:
                count += 1
        else:
            level -= 1

    return count