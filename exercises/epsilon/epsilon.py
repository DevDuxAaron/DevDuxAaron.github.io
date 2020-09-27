epsilon = 1
sw = True
while sw:
    if epsilon + 1 <= 1:
        break
    epsilon /=2
epsilon = 2 * epsilon
print("Epsilon en Python", epsilon)

# 0.193 seconds
# 2.220446049250313e-16
