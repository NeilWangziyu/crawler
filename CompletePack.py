# W:worth价值
W = [4,3,5,6,14]
# C:cost花销
C = [3,2,4,5,6]
# N:背包容量
N = 10
F = [0 for i in range(0,N+1)]
n = len(C)
#n:物品种类

def CompletePack(cost, worth):
    for i in range(cost, N+1):
        F[i] = max(F[i],F[i-cost]+worth)

for i in range(0, n):
    CompletePack(C[i], W[i])
print(F)

