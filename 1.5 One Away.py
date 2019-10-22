# 1.5
def oneAway(str1, str2):
    if len(str1) == len(str2):
        return oneReplace(str1, str2)
    elif len(str1)+1 == len(str2):
        return oneInsert(str1, str2)
    elif len(str1) == len(str2) + 1:
        return oneInsert(str2, str1)
    else:
        return False

def oneReplace(str1, str2):
    foundDifference = False
    for i, letter in enumerate(str1):
        if letter != str2[i]:
            if foundDifference:  # if there has been a previous difference
                return False
            else:
                foundDifference = True
    return True


def oneInsert(str1, str2):
    i = 0
    j = 0
    while i < len(str1) and j < len(str2):  # the while loop will terminate after the shorter string ends
        # print(i,j)
        if str1[i] != str2[j]:  # if two letters are different at the same position, advance the pointer of the long str by 1; then if the letters still don't match, return false
            if i != j:
                return False
            j += 1
        else:
            i += 1
            j += 1
    return True

oneInsert('appd', 'apple')
oneAway('pale', 'ple')
oneAway('pale', 'bake')
oneAway('ple', 'pale')
oneAway('pale', 'alpe')