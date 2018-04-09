

# n ^ 2 -> 双重for循环


# for a in range(0, n):
#     for b in range(0, n):
#         c = 1000 - a - b
#         if a ** 2 + b ** 2 == c **2:
#             print('a, b, c为：%d'%(a, b, c))

# T(1000) = 1000 * 1000 * (1 + 1)
# T(n) = n * n * (1 + max(1, 0))
#  = n ^ 2 * 2
#  = O(n ^ 2)
# 

