def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    # print(list(filter(str.isalnum, s.lower())))
    s_list = list(s)
    print(s_list)
    flag = True
    changable = True
    i = 0
    j = -1
    while (i - j < len(s_list)):
        if s_list[i] != s_list[j]:
            print("not equal at",i,j)
            if changable == False:
                flag = False
                break
            else:
                if s_list[i + 1] == s_list[j]:
                    changable = False
                    i = i + 1
                    print("i+1")
                elif s_list[i] == s_list[j - 1]:
                    changable = False
                    j = j - 1
                    print("j-1")
                else:
                    print("no way")
                    flag = False
                    break
        else:
            # equal
            pass
        i += 1
        j -= 1
        print(i,j)
    return flag




# print(isPalindrome("cupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupucu"))
print(isPalindrome("cupuuffuupucu"))

