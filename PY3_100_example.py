def tm001_1():
    import itertools
    print('001_1')
    temp_arr = list(itertools.permutations([1,2,3,4],3))
    arr = [100 * t[0] + 10 * t[1] + t[2] for t in temp_arr]
    print(len(arr),'\n',arr)

def tm002():
    money = int(input('净利润(万）:'))
    arr = [100,60,40,20,10,0]
    rat = [0.01,0.015,0.03,0.05,0.075,0.1]
    bonnus = 0
    for i in range(len(arr)):
        if money>arr[i]:
            bonnus += (money - arr[i])*rat[i]
            money = arr[i]
    print(bonnus)

def tm009():
    import time
    a = time.time()
    print(a)
    time.sleep(1)
    b = time.time()
    print(b)
    print(b - a)

def tm009_1():
    import time
    a = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) # time.localtime()时间戳转化成时间元祖
    print(a)
    time.sleep(1)
    b = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    print(b)

def tm010():
    for n in range(100,1000):
        i = n // 100
        j = n // 10 % 10
        k = n % 10
        if n == i ** 3 + j ** 3 + k ** 3:
            print(n,'\n')

def tm011():
    m1 = 1
    m2 = 0
    mm = 0
    print('1 1')
    for i in range(1,10):
        mm = mm + m2
        m2 = m1
        m1 = mm
        print(i+1,mm+m1+m2)

def tm012():
    arr = [2,3]
    for n in range(4,201):
        for t in arr:
            if n % t == 0:
                break
        else:
            arr.append(n)
    # print(arr)
    for i in range(len(arr)):
        if arr[i] > 100:
            l = arr[i:]
            print(len(l),l)
            break

def tm014():
    import math
    num = int(input('input a num\t'))
    arr= [1]
    while num > 1:
        for i in range(2,int(math.sqrt(num))+1):
            if num % i == 0:
                arr.append(i)
                num = num // i
                break
        else:
            arr.append(num)
            break
    print(arr)

def tm015():
    score = int(input('input a score: '))
    if score >= 90:
        print('A')
    elif score >= 60:
        print('B')
    else:
        print('C')

def tm016():
    import time
    print(time.time())
    print(time.localtime())
    print(time.asctime())
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))

    st1 = time.localtime(time.time())  # 时间戳 转化成 时间元祖
    st2 = time.strptime('2018/1/23', '%Y/%m/%d')  # 时间文本 转化成 时间元祖
    date = time.strftime('%Y-%m-%d', st1)  # 时间元祖 转化成 时间文本  '%Y-%m-%d %H:%M:%S'
    print(date)  # 前面两条函数配合着用，相当于将时间文本重新格式化。

def tm017():
    s = input('input a string:\n')
    letters, space, digit, others = 0, 0, 0, 0
    for c in s:
        if c.isalpha():
            letters += 1
        elif c.isspace():
            space += 1
        elif c.isdigit():
            digit += 1
        else:
            others += 1
    print('char = %d,space = %d,digit = %d,others = %d' % (letters, space, digit, others))

def tm018():
    a = 2
    t = 5
    num = 0
    for i in range(1, t + 1):
        num += i * a * (10 ** (t - i))
    print(num)

def tm019():
    for n in range(1,1000):
        arr = []
        for i in range(1,n):
            if n % i == 0:
                arr.append(i)

        if sum(arr) == n:
            print(n)


def tm020():
    total = 0
    m = 100
    total += m
    for i in range(1,10):
        #计算九次
        m = m / 2
        total += 2 * m
    print(total)
    print(m / 2)


def tm021():
    num = 1
    for i in range(9):
        num = (num + 1) * 2
    print(num)


def tm022():
     for a in ['x','y','z']:
         for b in ['x','y','z']:
             for c in ['x','y','z']:
                if a!=b and b!=c and c!=a:
                    if a!='x' and c !='x' and c != 'z' :
                        print('a'+a, 'b'+b, 'c'+c)


def tm023():
    num = 7
    for i in range(num):
        blank = abs(num//2 - i)
        print(' '*blank + '*'*(num - 2*blank) + ' '*blank )


def tm024():
    a,b,num = 2,1,0
    for i in range(20):
        num += a/b
        a = a + b
        b = a - b
    print(num)


def tm025():
    s, t = 0, 1
    for n in range(1,21):
        t = n * n
        s += t
    print(s)

def tm029():
    num = input('input a number')
    print(len(num))
    print(num[::-1])

if __name__ == '__main__':
    # tm001_1()
    # tm002()
    # tm009()
    # tm009_1()
    # tm010()
    # tm011()
    # tm012()
    # tm014()
    # tm015()
    # tm016()
    # tm017()
    # tm018()
    # tm019()
    # tm020()
    # tm021()
    # tm022()
    # tm023()
    # tm024()
    # tm025()
    tm029()

    pass

