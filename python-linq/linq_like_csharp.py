# https://metanit.com/sharp/tutorial/15.1.php
# https://github.com/rogerwcpt/python-linq-samples
from itertools import groupby


class List(list):

    def Select(self, fun):
        """
        Defines the projection of the selected values
        """
        return List([fun(x) for x in self])

    def SelectMany(self, fun_selector=None):
        """
        creates an output sequence with a one-to-many projection from the input sequence
        """

        output = List()
        for n in self:
            for x in n:
                if fun_selector is None:
                    output.append(x)
                else:
                    output.append(fun_selector(x))
        return output

    def Where(self, fun):
        """Defines a sampling filter"""

        return List(x for x in self if fun(x))

    def GroupBy(self, fun_key_selector):
        """Groups elements by key"""

        output = []
        for key, group in groupby(self, fun_key_selector):
            group_ = {'key': key, 'values': List([x for x in group])}
            output.append(group_)
        return List(output)

    def Except(self, input_list):
        """returns a sequence containing all the elements of the first sequence that are not in the second sequence"""

        return List([x for x in self if x not in input_list])

    def Single(self):
        """selects a single element of the collection;
        if the collection contains more or less than one element, an exception is thrown"""

        if len(self) > 1:
            raise Exception("Sequence contains more than one element")
        return self[0]

    def SingleOrDefault(self, default_value):
        """Selects the first element of the collection or returns the default value"""

        if len(self) != 1:
            return default_value
        return self[0]

    def Join(self, inner_list, fun_outher_key_selector, fun_inner_key_selector, result_selector):
        """как в sql - inner join"""

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

    def Concat(self, input_list):
        """Combines two homogeneous collections"""

        return List(self + input_list)

    def Intersect(self, input_list):
        """Returns the intersection of two collections, that is, those elements that appear in both collections"""

        return List(set(self).intersection((set(input_list))))

    def Count(self, fun=None):
        """Counts the number of elements of a collection that satisfy a certain condition"""

        if fun is None:
            return len(self)
        else:
            return len([x for x in self if fun(x)])

    def Sum(self):
        """counts the sum of numeric values in a collection"""

        return sum(self)

    def Average(self):
        """Calculates the average of the numeric values in a collection"""

        return sum(self) / float(len(self))

    def Min(self):
        """Finds the minimum value"""

        return min(self)

    def Max(self):
        """Finds the maximum value"""

        return max(self)

    def Take(self, count_of_elements):
        """Selects a certain number of elements"""

        return List(self[:count_of_elements])

    def Skip(self, count_of_elements):
        """Skips a certain number of elements"""

        return List(self[count_of_elements:])

    def TakeWhile(self, fun):
        """Returns a chain of sequence elements as long as the condition is true"""

        output = []
        for n in self:
            if fun(n) == True:
                output.append(n)
            else:
                break
        return List(output)

    def SkipWhile(self, fun):
        """Skips elements in a sequence as long as they satisfy a given condition,
         and then returns the remaining elements"""

        for i, n in enumerate(self):
            if fun(n) == False:
                return List(self[i:])

    def First(self):
        """Selects the first element of the collection"""

        return self[0]

    def FirstOrDefault(self, default_value):
        """Selects the first element of the collection or returns the default value"""

        return self[0] if len(self) > 0 else default_value

    def ElementAt(self, element_index):
        """Selects a sequence element at a specific index"""

        return self[element_index]

    def ElementAtOrDefault(self, element_index, default_value):
        """Selects a collection element at a specific index or returns a default value if the index is out of range"""

        return self[element_index] if element_index < len(self) else default_value

    def Last(self):
        """Selects the last element of the collection"""

        return self[-1]

    def LastOrDefault(self, default_value):
        """Selects the last element of the collection or returns the default value"""

        return self[-1] if len(self) > 0 else default_value

    def OrderBy(self, fun=None):
        """Arranges elements in ascending order"""

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

    def Reverse(self):
        """Arranges elements in reverse order"""

        self.reverse()
        return self

    def Zip(self, second_list, fun_result_selector):
        """Combines two collections according to a certain condition"""

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

    def IndexOf(self, element):
        """Returns the index of the first occurrence of an element in a list"""

        self.index(element)

    def Insert(self, index, element):
        """Inserts the element element in the list at position index"""

        self.insert(index, element)

    def Remove(self, element):
        """Removes the item element from the list"""

        self.remove(element)

    def RemoveAt(self, index):
        """Removing an element at the specified index index"""

        del self[index]

    def Union(self, second_list):
        """Returns the union of sets from two source sequences"""

        return List(list(set(self + second_list)))
