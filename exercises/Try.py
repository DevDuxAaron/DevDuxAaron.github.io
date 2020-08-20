# sw = True
# while sw:
#     try:
#         n = int(input())
#         # n = 11
#         b = bin(n)
#         c = b[-1:0:-1]+b[0]
#         c = int("0b"+str(c[0:-2]),2)
#         print(n-c)
#     except EOFError:
#         break


# def isDivisible(x):
#     if x % 2 == 0:
#         return True
#     elif x % 5 == 0:
#         return True
#     elif x % 11 == 0:
#         return True
#     return False
# n = int(input())
# for i in range(n):
#     x, y = map(int,input().split())
#     sw = True
#     while isDivisible(x) or isDivisible(y):
#         if x % 2 == 0:
#             x //= 2
#         elif x % 5 == 0:
#             x //= 5
#         elif x % 11 == 0:
#             x //= 11
#         if y % 2 == 0:
#             y //= 2
#         elif y % 5 == 0:
#             y //= 5
#         elif y % 11 == 0:
#             y //= 11
#     res = 'Si' if x == y else 'No'
#     print(res)


while True:
    try:
        x,y,m = map(int,input().split())
        res = x * y
        while x * y > m:
            if (x-1) * y <= m:
                res = (x-1) * y
            elif (x) * (y-1) <= m:
                res = (x) * (y-1)
            elif (x-1) * (y-1) <= m:
                res = (x-1) * (y-1)
            else:
                x -= 1
                y -= 1
        print(res)
    except EOFError:
        break