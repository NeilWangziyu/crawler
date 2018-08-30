# std1 = {'name':'Michael','score':98}
# std2 = {'name':'Bob', 'score':81}
#
# def print_score(Std):
#     print('%s %s' %(Std['name'], Std['score']))
#
# print_score(std1)


class Student(object):
    count = 0

    def __init__(self, name, score):
        self.name = name
        self.__class__.count = self.count + 1
        # score变成私有变量，无法外部访问只能内部访问
        self.__score = score

    def get_socre(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('socre is wrong')

    def print_score(self):
        print('%s %s' %(self.name, self.__score))

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

    def get_count(self):
        print(self.count)

class Animal(object):
    def run(self):
        print('Animal is running')

class Dog(Animal):
    def run(self):
        print('Dog is running')

class Cat(Animal):
    pass



if __name__ == '__main__':
    print(Student.count)
    bart = Student('Bart Simpson', 59)
    print(Student.count)
    lisa = Student('lisa simpston', 87)
    # print(lisa.name)
    # bart.print_score()
    # lisa.print_score()
    # grade = bart.get_grade()
    # print(grade)
    # bart.set_score(60)
    # bart.print_score()
    print(Student.count)

    # bart.set_score(101)

    # dog = Dog()
    # dog.run()
    # print(dir(bart))


