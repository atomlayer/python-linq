# https://metanit.com/sharp/tutorial/15.1.php
# https://github.com/rogerwcpt/python-linq-samples
from itertools import groupby

class List(list):


    # определяет проекцию выбранных значений
    def Select(self, fun):
        return List([fun(x) for x in self])

    # создает выходную последовательность с проекцией "один ко многим" из входной последовательности
    def SelectMany(self, fun_selector=None):
        output = List()
        for n in self:
            for x in n:
                if fun_selector is None:
                    output.append(x)
                else:
                    output.append(fun_selector(x))
        return output


    # определяет фильтр выборки
    def Where(self, fun):
        return List(x for x in self if fun(x))

    # группирует элементы по ключу
    def GroupBy(self, fun_key_selector):
        output = []
        for key, group in groupby(self, fun_key_selector):
            group_ = {'key':key, 'values': List([x for x in group])}
            output.append(group_)
        return List(output)


    # возвращает последовательность, содержащую все элементы первой последовательности,
    # которых нет во второй последовательности
    def Except(self, input_list):
        return List([x for x in self if x not in input_list])


    # выбирает единственный элемент коллекции, если коллекция содердит больше или меньше одного элемента,
    # то генерируется исключение
    def Single(self):
        if len(self)>1:
            raise Exception("Последовательность содержит более одного элемента")
        return self[0]

    # выбирает первый элемент коллекции или возвращает значение по умолчанию
    def SingleOrDefault(self, default_value):
        if len(self)!=1:
            return default_value
        return self[0]


    # как в sql - inner join
    def Join(self, inner_list, fun_outher_key_selector, fun_inner_key_selector, result_selector):
        output = List()
        for n in self:
            for o in inner_list:
                if fun_outher_key_selector(n) == fun_inner_key_selector(o):
                    output.append(result_selector(n, o))
        return output


    def Any(self, fun):
        return any([fun(x) for x in self])

    def All(self, fun):
        return all([fun(x) for x in self])

    def Contains(self, element):
        return element in self

    def Distinct(self):
        return List(list(set(self)))

    # объединяет две однородные коллекции
    def Concat(self, input_list):
        return List(self + input_list)

    # возвращает пересечение двух коллекций, то есть те элементы, которые встречаются в обоих коллекциях
    def Intersect(self, input_list):
        return List(set(self).intersection((set(input_list))))

    # подсчитывает количество элементов коллекции, которые удовлетворяют определенному условию
    def Count(self, fun=None):
        if fun is None:
            return len(self)
        else:
            return len([x for x in self if fun(x)])

    # подсчитывает сумму числовых значений в коллекции
    def Sum(self):
        return sum(self)

    # подсчитывает cреднее значение числовых значений в коллекции
    def Average(self):
        return sum(self) / float(len(self))

    # находит минимальное значение
    def Min(self):
        return min(self)

    # находит максимальное значение
    def Max(self):
        return max(self)

    # выбирает определенное количество элементов
    def Take(self, count_of_elements):
        return List(self[:count_of_elements])

    # пропускает определенное количество элементов
    def Skip(self, count_of_elements):
        return List(self[count_of_elements:])

    # возвращает цепочку элементов последовательности, до тех пор, пока условие истинно
    def TakeWhile(self, fun):
        output = []
        for n in self:
            if fun(n) == True:
                output.append(n)
            else: break
        return List(output)

    # пропускает элементы в последовательности, пока они удовлетворяют заданному условию,
    # и затем возвращает оставшиеся элементы
    def SkipWhile(self, fun):
        for i, n in enumerate(self):
            if fun(n) == False:
                return List(self[i:])

    # выбирает первый элемент коллекции
    def First(self):
        return self[0]

    # выбирает первый элемент коллекции или возвращает значение по умолчанию
    def FirstOrDefault(self, default_value):
        return self[0] if len(self)>0 else default_value

    # выбирает элемент последовательности по определенному индексу
    def ElementAt(self, element_index):
        return self[element_index]

    # выбирает элемент коллекции по определенному индексу или возвращает значение по умолчанию,
    # если индекс вне допустимого диапазона
    def ElementAtOrDefault(self, element_index, default_value):
        return self[element_index] if element_index < len(self) else default_value

    # выбирает последний элемент коллекции
    def Last(self):
        return self[-1]

    # выбирает последний элемент коллекции или возвращает значение по умолчанию
    def LastOrDefault(self, default_value):
        return self[-1] if len(self) > 0 else default_value

    # упорядочивает элементы по возрастанию
    def OrderBy(self, fun=None):
        if fun is None:
            self.sort()
        else:
            self.sort(key=fun)
        return self

    def OrderByDescending(self, fun=None):
        if fun is None:
            self.sort(reverse=True)
        else:
            self.sort(reverse=True, key=fun)
        return self

    # располагает элементы в обратном порядке
    def Reverse(self):
        self.reverse()
        return self


    # Zip: объединяет две коллекции в соответствии с определенным условием
    def Zip(self, second_list, fun_result_selector):
        count = len(self) if len(self) < len(second_list) else len(second_list)
        output = List()
        for i in range(count):
            output.append(fun_result_selector(self[i], second_list[i]))
        return output


    def ToPythonList(self):
        return self

    def ForEach(self, fun):
        for n in self:
            fun(n)


    def Add(self, new_element):
        self.append(new_element)

    def AddRange(self, input_list):
        if type(input_list) is list:
            self.extend(input_list)
        if type(input_list) is List:
            self.extend(input_list.ToPythonList())
        else:
            raise ValueError()

    # возвращает индекс первого вхождения элемента в списке
    def IndexOf(self, element):
        self.index(element)

    # вставляет элемент element в списке на позицию index
    def Insert(self, index, element):
        self.insert(index, element)

    # удаляет элемент item из списка
    def Remove(self, element):
        self.remove(element)

    # удаление элемента по указанному индексу index
    def RemoveAt(self, index):
        del self[index]

    # возвращает объединение множеств из двух исходных последовательностей
    def Union(self, second_list):
        return List(list(set(self + second_list)))






