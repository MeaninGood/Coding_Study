# # a = '#' + input()
# # b = '#' + input()

# # dp = [[0 for i in range(len(b))] for j in range(len(a))]

# # tmp = []
# # for i in range(1, len(a)):
# #     for j in range(1, len(b)):
# #         if a[i] == b[j]:
# #             dp[i][j] = dp[i - 1][j - 1] + 1
# #             tmp.append([a[i], b[j]])
# #         else:
# #             dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

# # idx = 1
# # ans = []
# # for i in range(1, len(a)):
# #     if idx > dp[len(a) - 1][len(b) - 1]:
# #         break
    
# #     for j in range(1, len(b)):
# #         if dp[i][j] == idx:
# #             ans.append(a[i])
# #             idx += 1
# #             break

# # if dp[len(a) - 1][len(b) - 1] == 0:
# #     print(0)
# # else:
# #     idx = 1
# #     ans = []
# #     for i in range(1, len(a)):
# #         if idx > dp[len(a) - 1][len(b) - 1]:
# #             break
        
# #         for j in range(1, len(b)):
# #             if dp[i][j] == idx:
# #                 ans.append(a[i])
# #                 idx += 1
# #                 break


# from pprint import pprint


# def get_lcs(x, y):
#     global res
    
#     if dp[x][y] == 0:
#         return
    
#     if dp[x][y] == dp[x - 1][y]:
#         get_lcs(x - 1, y)
    
#     elif dp[x][y] == dp[x][y - 1]:
#         get_lcs(x, y - 1)
    
#     else:
#         res = a[x] + res
#         get_lcs(x - 1, y - 1)
    
    
    


# a = '#' + input()
# b = '#' + input()

# dp = [[0 for i in range(len(b))] for j in range(len(a))]

# tmp = []
# for i in range(1, len(a)):
#     for j in range(1, len(b)):
#         if a[i] == b[j]:
#             dp[i][j] = dp[i - 1][j - 1] + 1
#             tmp.append([a[i], b[j]])
#         else:
#             dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

# # idx = 1
# # ans = []
# # for i in range(1, len(a)):
# #     if idx > dp[len(a) - 1][len(b) - 1]:
# #         break
    
# #     for j in range(1, len(b)):
# #         if dp[i][j] == idx:
# #             ans.append(a[i])
# #             idx += 1
# #             break
# # pprint(dp)
# # print(ans)

# res = ''
# if dp[len(a) - 1][len(b) - 1] == 0:
#     print(0)
    
# else:
#     print(dp[len(a) - 1][len(b) - 1])
#     get_lcs(len(a) - 1, len(b) - 1)
#     print(res)






def get_lcs(x, y):
    global res
    
    if dp[x][y] == 0:
        return
    
    if dp[x][y] == dp[x - 1][y]:
        get_lcs(x - 1, y)
    
    elif dp[x][y] == dp[x][y - 1]:
        get_lcs(x, y - 1)
    
    else:
        res = a[x] + res
        get_lcs(x - 1, y - 1)
    
    
    


a = '#' + input()
b = '#' + input()

dp = [[0 for i in range(len(b))] for j in range(len(a))]

tmp = []
for i in range(1, len(a)):
    for j in range(1, len(b)):
        if a[i] == b[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            tmp.append([a[i], b[j]])
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

res = ''
if dp[len(a) - 1][len(b) - 1] == 0:
    print(0)
    
else:
    print(dp[len(a) - 1][len(b) - 1])
    get_lcs(len(a) - 1, len(b) - 1)
    print(res)