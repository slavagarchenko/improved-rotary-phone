# #1
# data = input()
# N,d,r = map(float, data.split(' '))
# print(2*d+2*r)*N

# # 2
# number = float(input())
# num = number
# while num > 2:
#     num = number**0.5
#     number = num
#     print(round(num, 3))

# # 3
# ice = int(input())
# for i in range(215, ice):
#     if ice % i == 0:
#         print(i)
#         break

# # 4
# count = 0
# digit = int(input())
# while digit != 0:
#     digit = int(input())
#     if digit % 4 == 0:
#         count += 1
# print(count-1)

# # 5
# for i in range(100000, 999999):
#     if str(i)[1] == str(i)[5] and str(i)[2] == str(i)[4]:
#         if str(i+1)[1] == str(i+1)[5] and str(i+1)[2] == str(i+1)[4]:
#             if str(i+2)[1] == str(i+2)[4] and str(i+2)[2] == str(i+2)[3]:
#                 if str(i+3)[0] == str(i+3)[5] and str(i+3)[1] == str(i+3)[4] and str(i+3)[2] == str(i+3)[4]:
#                     print(i)

# #6
# for i in range(10,100):
#     if i**2%100 == i:
#         break
# print(f' {i}\n*{i}\n___\n\n {i**2}')

# # 7
# for i in range(10000, 19999):
#     m = i // 10000
#     o = i % 10000 // 1000
#     n = i % 1000 // 100
#     e = i % 100 // 10
#     y = i % 10

#     if len({m, o, n, e, y}) != 5:
#         continue

#     for s in range(1, 10):
#         for d in range(1, 10):
#             for r in range(1, 10):
#                 if (s == d or s == r or d == r or
#                         s in {m, o, n, e, y} or
#                         d in {m, o, n, e, y} or
#                         r in {m, o, n, e, y}):
#                     continue

#                 send = s * 1000 + e * 100 + n * 10 + d
#                 more = m * 1000 + o * 100 + r * 10 + e

#                 if send + more == i:
#                     print(f"SEND = {send}, MORE = {more}, MONEY = {i}")

# # 8
# x = int(input())
# count = 0
# for i in range(1, x-1):
#     for k in range(1, x-1):
#         if i**2 + k**2 == x:
#             count += 1
# print(round(count/2))

# # 9
# N = int(input())
# count = 0
# for i in range(N+1):
#     for k in range(N+1):
#         count += k
#     count += i
# print(count)

# # 10
# n = int(input())
# count = 0
# stairs = [0] * n
# level = 1
# stairs[0] = n
# while level > 0:
#     stairs[level - 1] -= 1
#     remaining = sum(stairs[:level])
#     if stairs[level - 1] <= 0:
#         level -= 1
#         continue
#     if remaining == 0:
#         count += 1
#         level -= 1
#     elif remaining > stairs[level - 1]:
#         stairs[level] = min(stairs[level - 1], remaining)
#         level += 1
# print(count)
