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


<<<<<<< HEAD
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
=======
<<<<<<< HEAD
# while True:
#     try:
#         a,b,c = map(int,input().split())
#         mul = a * b
#         if mul <= c:
#             print(mul)
#         else:
#             while mul > c:
#                 if a >= b:
#                     a -= 1
#                     A = a * b
#                 else:
#                     b-= 1
#                     B = a * b
#                 mul = min(A,B)
#             print(mul)
#     except EOFError:
#         break

# def verifySecond():
#     global dado
#     res = 0
#     for k in range(2):
#         if (dado[k][1] == 1 and dado[k+2][1] == 6):
#             res +=1
#         if (dado[k][1] == 6 and dado[k+2][1] == 1):
#             res +=1
#         if (dado[k][1] == 3 and dado[k+2][1] == 4):
#             res +=1
#         if (dado[k][1] == 4 and dado[k+2][1] == 3):
#             res +=1
#         if (dado[k][1] == 2 and dado[k+2][1] == 5):
#             res +=1
#         if (dado[k][1] == 5 and dado[k+2][1] == 2):
#             res +=1
#     return res

# def verifyFirst():
#     global dado
#     for j in range(4):
#         if dado[j][0] != 0:
#             if (dado[j][0] == 1 and dado[j][2] == 6):
#                 return True
#             if (dado[j][0] == 6 and dado[j][2] == 1):
#                 return True
#             if (dado[j][0] == 4 and dado[j][2] == 3):
#                 return True
#             if (dado[j][0] == 3 and dado[j][2] == 4):
#                 return True
#             if (dado[j][0] == 2 and dado[j][2] == 5):
#                 return True
#             if (dado[j][0] == 5 and dado[j][2] == 2):
#                 return True
#     return False

# while True:
#     try:
#         dado = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
#         for i in range(4):
#             line = list(map(int,input().split()))
#             if len(line) == 1:
#                 dado[i][1] = line[0]
#             else:
#                 dado[i] = line
#         if verifyFirst() and (verifySecond()==2):
#             print('Bien')
#         else:
#             print('Mal')
#         x = input()
#     except EOFError:
#         break

x = int(input())
for i in range(x):
    n , m = map(int,input().split())
    m = m - (m // 2)
    n = n - 1
    print(m*n)

>>>>>>> 5fe31fb2e3a824b5171489a9f10b5a0b5bb259ef
