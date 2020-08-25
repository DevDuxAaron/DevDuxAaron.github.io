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
        a,b,c = map(int,input().split())
        mul = a*b
        if mul<=c:
            print(mul)
        else:
            while mul>c:
                if a >= b:
                    a -=1
                else:
                    b-=1
                mul = a*b
            print(mul)
    except EOFError:
        break