def numberToWords(num):
    """
    :type num: int
    :rtype: str
    """
    billion = num // 1000
    billion_str = number_less_three_digit(billion)
    print(billion_str)
    billion_left = num % 1000
    million = billion_left // 1000
    million_str = number_less_three_digit(million)
    print(million_str)
    million_left = billion_left % 1000

    thousand = million_left // 1000
    thousand_str = number_less_three_digit(thousand)
    print(thousand_str)
    thousand_left = million_left % 1000
    interger_str = number_less_three_digit(thousand_left)
    print(interger_str)

def number_less_three_digit(num):
    interger_num_dict = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight',
                         9: 'Nine', 0: '',
                         10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen',
                         16: 'Sixteen', 17: 'Seventeen',18: 'Eighteen', 19: 'Ninteen'}
    decade_num_dict = {2: 'Twenty', 3: 'Thirty', 4:'Fourty', 5:'Fifty', 6:'Sixty', 7:'Seventy', 8:'Eighty', 9:'Ninty'}
    number = []
    hundred = num // 100
    num = num % 100
    if num >= 20:
        decade = num // 10
        integer = num % 10

        number.append(interger_num_dict[hundred])
        number.append(decade_num_dict[decade])
        number.append(interger_num_dict[integer])
    else:
        number.append(interger_num_dict[hundred])
        number.append(interger_num_dict[num])

    if number[0] != '':
        # 存在百位数
        number.insert(1,'Hundred')
        res_str =' '.join(number)
        print(res_str)
    else:
        res_str =' '.join(number)
        print(res_str)
    return number



if __name__ =='__main__':
    res = numberToWords(170)
    print(res)