# W:worth价值
W = [4,3,5,6,14]
# C:cost花销
C = [2,2,4,5,6]
# M:每种数量， 0代表无限多
M = [3,4,3,1,2]
# N:背包容量
N = 12
F = [0 for i in range(0,N+1)]
n = len(C)
#n:物品种类

def CompletePack(cost, worth):
    for i in range(cost, N+1):
        F[i] = max(F[i],F[i-cost]+worth)

def OneZeroPack(cost, worth):
    for i in reversed(range(cost, N+1)):
        F[i] = max(F[i],F[i-cost]+worth)

def MultiplePack(cost, worth, mul):
    if (cost * mul) >= n:
        # 当该种物品的个数乘以体积大于背包容量，视为有无限个即完全背包
        CompletePack(C[i], W[i])
        return
    tem_number = 1
    # 以上情况不满足，转化为以下情况，具体参考《背包九讲》多重背包的时间优化
    while (tem_number < mul):
        OneZeroPack(tem_number * cost, tem_number * worth)
        mul = mul - tem_number
        tem_number = tem_number * 2  # 转化为1，2，4
    OneZeroPack(mul * cost, mul * worth)



for i in range(0, n):
    if M[i]==1:
        OneZeroPack(C[i], W[i])
    elif M[i]==0:
        CompletePack(C[i], W[i])
    else:
        MultiplePack(C[i], W[i], M[i])

print(F)


