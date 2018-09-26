def one_zero_bag(N,V,C,W):
    res = [[0 for j in range(V+1)] for i in range(N+1)]
    # res:N*V矩阵
    for i in range(1,N+1):
        # 当前只包含i件物品
        for j in range(1,V+1):
            res[i][j] = res[i-1][j]
            if (j>=C[i-1]) and (res[i-1][j-C[i-1]]+W[i-1]>res[i][j]):
                res[i][j] = res[i-1][j-C[i-1]]+W[i-1]
    return res


def total_bag(N,V,C,W):
    res = [0 for j in range(V+1)]
    # res:1*N矩阵
    for i in range(0, N):
        for j in range(1,V+1):
            if j>=C[i]:
                res[j] = max(res[j],res[j-C[i]]+W[i])

    return res



if __name__ =='__main__':

    N = 5
    V = 10
    # W:worth价值
    W = [4,3,5,6,14]
    # C:cost花销
    C = [2,2,4,5,6]
    print('0-1背包')
    res = one_zero_bag(N, V, C, W)
    print(res)
    # print('total value:',res[N][V])


    print('完全背包')
    res = total_bag(N, V, C, W)
    print(res)
