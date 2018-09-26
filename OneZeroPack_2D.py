# two kinds of Cost:C and D
# worth:W
W = [6,3,5,8,3,1,6,9]
C = [3,2,6,7,1,4,9,5]
D = [6,2,4,6,7,3,8,5]
V = 20
U = 25

#n: number of item kinds
n = len(C)

F = [[0]*(U+1) for i in range(V+1)]
# F is  a (V+1)*(U+1) matrix

def OneZeroPack_2D(cost1, cost2, worth):
    for j in reversed(range(cost1, V+1)):
        for m in reversed(range(cost2, U+1)):
            F[j][m] = max(F[j][m], F[j-cost1][m-cost2]+worth)


# for i in range(0, n):
#     for j in reversed(range(C[i], V+1)):
#         for m in reversed(range(D[i], U+1)):
#             F[j][m] = max(F[j][m], F[j-C[i]][m-D[i]]+W[i])


for i in range(0, n):
    OneZeroPack_2D(C[i], D[i], W[i])

print(F)
print('result:',F[V][U])
