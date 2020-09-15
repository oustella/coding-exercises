# Recursive integer multiplication

# # this version is not accurate for large numbers due to the inaccuracy in `int()`.
# import math
# def intMul(x, y):
#     if x < 10 and y < 10:
#         r = x * y
#     else:
#         n = len(str(int(x)))
#         m = len(str(int(y)))
#         nc = max(n,m)
        
#         b = int(str(int(x))[-math.ceil(nc/2):])
#         a = int((x-b)/(10**(math.ceil(nc/2))))
#         d = int(str(int(y))[-math.ceil(nc/2):])
#         c = int((y-d)/(10**(math.ceil(nc/2))))
# #         print(x, y, a, b, c, d)
#         r = 10**(2*math.ceil(nc/2)) * intMul(a, c) + 10**(math.ceil(nc/2)) * (intMul(a, d) + intMul(b, c)) + intMul(b, d)
#     return r


# this version utilizing modulus operation and floor division to return accurate integers.
def intMul(x, y):
    if x < 10 and y < 10:
        r = x * y
    else:
        n = len(str(int(x)))
        m = len(str(int(y)))
        nc = max(n, m)  # this takes care of integers with unequal length

        b = x % (10**(nc//2))
        a = (x-b) // (10**(nc//2))
        d = y % (10**(nc//2))
        c = (y-d) // (10**(nc//2))

#         print(x, a, b, y, d, c)

        r = (10**(2*(nc//2)) * intMul(a, c) 
             + 10**(nc//2) * (intMul(a, d) 
                + intMul(b, c)) + intMul(b, d))
    return r


# further optimization with three recursion calls
def intMul2(x, y):
    ''' Karatsuba multiplication'''
    if x < 10 and y < 10:
        r = x * y
    else:
        n = len(str(int(x)))
        m = len(str(int(y)))
        nc = max(n, m)  # this takes care of integers with unequal length

        b = x % (10**(nc//2))
        a = (x-b) // (10**(nc//2))
        d = y % (10**(nc//2))
        c = (y-d) // (10**(nc//2))

        ac = intMul2(a, c)
        bd = intMul2(b, d)
        adbc = intMul2(a+b, c+d) - ac - bd

        r = (10**(2*(nc//2)) * ac + 10 ** (nc//2) * adbc + bd)
    return r


a = 3141592653589793238462643332795028841971693993751058209749445925
b = 2718281828459045235360287713526624977572470936999595749669676273
print(intMul(a, b) == a * b)
print(intMul2(a, b) == a * b)
