def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    list_res = []
    for i in range(numRows):
        if i == 0:
            result_list = [1]
        elif i == 1:
            result_list = [1,1]
        else:
            result_list = [1]
            for t in range(1, i):
                result_list.append(list_res[i-1][t-1]+list_res[i-1][t])
            result_list.append(1)
        list_res.append(result_list)

    return list_res


print(generate(5))
