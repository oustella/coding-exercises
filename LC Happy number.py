# https://leetcode.com/problems/happy-number/

def isHappy(n):
    ''''
    The key is realizing that if the sum of squares has been seen before,
    it's an endless loop
    '''
    mem = []
    while n!=1:
        # access the digits by converting int to str
        n = sum(int(i)**2 for i in str(n))
        if n in mem:
            return False
        else:
            mem.append(n)
    return True


