import pandas as pd

# 二分法
def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = int((low + high)/2)
        print('check:', mid)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

#排序算法
def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index
def seclecionSort(arr):
    newArr=[]
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


#快速排序
def quicksort(array):
    if len(array)<2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        more = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(more)

#合并排序
def mergeSort(arr):
    if (len(arr)<=1):
        return arr
    mid = int(len(arr)/2)
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:len(arr)])
    result = []
    while len(left) > 0 and len(right) > 0:
        if(left[0] > right[0]):
            result.append(right.pop(0))
        else:
            result.append(left.pop(0))
    if(len(left) > 0):
        result.extend(mergeSort(left))
    else:
        result.extend(mergeSort(right))
    return result



voted = {}
def check_voter(name):
    if voted.get(name):
        print('he has voted')
    else:
        voted[name] = True
        print('let him vote')


if __name__ == '__main__':
    my_list = [1,3,4,5,6,7,9,0,4,2,11,4]
    # print(binary_search(my_list,9))
    # print(binary_search(my_list, -1))

    # print(seclecionSort([1,3,4,5,6,7,9]))

    print(quicksort(my_list))
    #
    # print(mergeSort(my_list))

    # check_voter('tom')
    # check_voter('tim')
    # check_voter('tom')

