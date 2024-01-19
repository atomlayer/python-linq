# https://metanit.com/sharp/tutorial/15.1.php
# https://github.com/rogerwcpt/python-linq-samples
from itertools import groupby


class List(list):

    def Select(self, fun):
        """
        Defines the projection of the selected values by applying the specified function to each element of the collection.

        Args:
        - fun: The function that specifies the projection to be applied to each element.

        Returns:
        A new list containing the results of applying the function to each element of the collection.
        """

        return List([fun(x) for x in self])

    def SelectMany(self, fun_selector=None):
        """
        Creates an output sequence with a one-to-many projection from the input sequence.

        Args:
        - fun_selector: The function that specifies the one-to-many projection to be applied to each element.
        If None, the method flattens the elements of the input sequence.

        Returns:
        A new list containing the results of the one-to-many projection from the input sequence.
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
        """
        Defines a sampling filter by applying the specified function to each element of the collection.

        Args:
        - fun: The function that specifies the condition for the sampling filter.

        Returns:
        A new list containing the elements of the collection that satisfy the specified condition.
        """

        return List(x for x in self if fun(x))

    def GroupBy(self, fun_key_selector):
        """
        Groups elements by key using the specified key selector function.

        Args:
        - fun_key_selector: The function that selects the key for grouping the elements.

        Returns:
        A new list containing groups of elements,
        where each group is represented by a dictionary with 'key' and 'values' fields.
        """

        output = []
        for key, group in groupby(self, fun_key_selector):
            group_ = {'key': key, 'values': List([x for x in group])}
            output.append(group_)
        return List(output)

    def Except(self, input_list):
        """
        Returns a sequence containing all the elements of the first sequence that are not in the second sequence.

        Args:
        - self: The first sequence to be compared.
        - input_list: The second sequence to be compared.

        Returns:
        A sequence containing all the elements of the first sequence that are not present in the second sequence.
        """
        return List([x for x in self if x not in input_list])

    def Single(self):
        """
        Selects a single element from the collection.
        If the collection contains more or less than one element, an exception is thrown.

        Returns:
        The single element from the collection.

        Raises:
        - Exception: If the collection contains more than one element.
        """

        if len(self) > 1:
            raise Exception("Sequence contains more than one element")
        return self[0]

    def SingleOrDefault(self, default_value):
        """
        Selects the first element of the collection or returns the default value if the collection is empty or contains
        more than one element.

        Args:
        - default_value: The default value to be returned if the collection is empty or contains more than one element.

        Returns:
        The first element of the collection or the default value.

        """

        if len(self) != 1:
            return default_value
        return self[0]

    def Join(self, inner_list, fun_outher_key_selector, fun_inner_key_selector, result_selector):
        """
        Performs an inner join operation, similar to the SQL inner join, on two lists.

        Args:
        - self: The first list to be joined.
        - inner_list: The second list to be joined.
        - fun_outer_key_selector: A function that selects the key from the elements of the first list.
        - fun_inner_key_selector: A function that selects the key from the elements of the second list.
        - result_selector: A function that produces the result based on the matching elements from both lists.

        Returns:
        A list containing the result of the inner join operation.
        """

        output = List()
        for n in self:
            for o in inner_list:
                if fun_outher_key_selector(n) == fun_inner_key_selector(o):
                    output.append(result_selector(n, o))
        return output

    def Any(self, fun):
        """
        Determines whether any element of the collection satisfies a given condition specified by the provided function.

        Args:
        - fun: The function that specifies the condition to be satisfied.

        Returns:
        True if at least one element satisfies the condition, otherwise False.
        """

        return any([fun(x) for x in self])

    def All(self, fun):
        """
        Determines whether all elements of the collection satisfy a given condition specified by the provided function.

        Args:
        - fun: The function that specifies the condition to be satisfied.

        Returns:
        True if the condition is satisfied for all elements, otherwise False.
        """

        return all([fun(x) for x in self])

    def Contains(self, element):
        """
        Determines whether the collection contains a specific element.

        Args:
        - element: The element to be checked for presence in the collection.

        Returns:
        True if the element is present in the collection, otherwise False.
        """

        return element in self

    def Distinct(self):
        """
        Returns a new list containing the distinct elements of the collection.

        Returns:
        A new list containing only the distinct elements of the collection.
        """

        return List(list(set(self)))

    def Concat(self, input_list):
        """
        Combines two homogeneous collections into a single list.

        Args:
        - input_list: The second collection to be combined with the current collection.

        Returns:
        A new list containing the elements of both collections combined.
        """

        return List(self + input_list)

    def Intersect(self, input_list):
        """
        Returns a new list containing the intersection of two collections, that is,
        those elements that appear in both collections.

        Args:
        - input_list: The second collection to find the intersection with the current collection.

        Returns:
        A new list containing the elements that appear in both the current collection and the input collection.
        """

        return List(set(self).intersection((set(input_list))))

    def Count(self, fun=None):
        """
        Counts the number of elements of a collection that satisfy a certain condition.

        Args:
        - fun: The condition function used to determine which elements to count.

        Returns:
        - int: The number of elements that satisfy the condition.

        Example:
        # >>> lst = List([1, 2, 3, 4, 5])
        # >>> lst.Count(lambda x: x % 2 == 0)
        2
        """

        if fun is None:
            return len(self)
        else:
            return len([x for x in self if fun(x)])

    def Sum(self):
        """
        Calculates the sum of numeric values in a collection.

        Returns:
        - The sum of numeric values in the collection.

        Example:
        # >>> lst = List([1, 2, 3, 4, 5])
        # >>> lst.Sum()
        15
        """

        return sum(self)

    def Average(self):
        """
        Calculates the average of the numeric values in a collection.

        Returns:
        - The average of the numeric values in the collection.

        Example:
        # >>> lst = List([1, 2, 3, 4, 5])
        # >>> lst.Average()
        3.0
        """

        return sum(self) / float(len(self))

    def Min(self):
        """
        Finds the minimum value in the collection.

        Returns:
        - The minimum value in the collection.

        Example:
        # >>> lst = List([1, 2, 3, 4, 5])
        # >>> lst.Min()
        1
        """

        return min(self)

    def Max(self, fun=None):
        """
        The function Max takes an optional argument fun and returns the maximum value from a given input.
        If the fun argument is not provided, it returns the maximum value from the input.
        If the fun argument is provided, it returns the maximum value based on the result of the function fun.

        Args:
        - fun: The condition function used to determine which elements to count.

        Example:
        # Create a list of numbers
        numbers = [5, 8, 3, 11, 6]

        # Using the Max function without the fun argument
        max_value = Max(numbers)
        print(max_value)  # Output: 11

        # Using the Max function with a custom function
        max_value_custom = Max(numbers, fun=lambda x: x % 2)
        print(max_value_custom)  # Output: 8
        """
        if fun is None:
            return max(self)
        else:
            return max(self, key=lambda pair: pair[0])

    def Take(self, count_of_elements):
        """
        Selects a certain number of elements from the beginning of the collection.

        Args:
        - count_of_elements (int): The number of elements to select.

        Returns:
        - list: The selected elements from the beginning of the collection.

        Example:
        # >>> lst = List([1, 2, 3, 4, 5])
        # >>> lst.Take(3)
        [1, 2, 3]
        """

        return List(self[:count_of_elements])

    def Skip(self, count_of_elements):
        """
        Skips a certain number of elements from the list and returns the remaining elements.

        Args:
        - count_of_elements (int): The number of elements to skip.

        Returns:
        - list: The list of elements after skipping the specified number of elements.

        Example:
        # >>> lst = List([1, 2, 3, 4, 5])
        # >>> Skip(lst, 2)
        [3, 4, 5]
        """

        return List(self[count_of_elements:])

    def TakeWhile(self, fun):
        """
        Returns a chain of sequence elements as long as the condition is true.

        Args:
        - fun: The condition function used to determine whether to include an element.

        Returns:
        - list: A new list containing the elements that satisfy the condition.

        Example:
        # >>> lst = List([1, 2, 3, 4, 5])
        # >>> lst.TakeWhile(lambda x: x < 4)
        [1, 2, 3]
        """

        output = []
        for n in self:
            if fun(n) == True:
                output.append(n)
            else:
                break
        return List(output)

    def SkipWhile(self, fun):
        """
        Skips elements in a sequence as long as they satisfy a given condition, and then returns the remaining elements.

        Args:
        - fun: The condition function used to determine whether to skip an element.

        Returns:
        - list: The remaining elements after skipping the initial elements that satisfy the condition.

        Example:
        # >>> lst = List([1, 2, 3, 4, 5])
        # >>> lst.SkipWhile(lambda x: x < 3)
        [3, 4, 5]
        """

        for i, n in enumerate(self):
            if fun(n) == False:
                return List(self[i:])

    def First(self):
        """
        Selects the first element of the collection.

        Returns:
        - The first element of the collection.

        Example:
        # >>> lst = List([1, 2, 3, 4, 5])
        # >>> lst.First()
        1
        """

        return self[0]

    def FirstOrDefault(self, default_value):
        """
        Selects the first element of the collection or returns the default value if the collection is empty.

        Args:
        - default_value: The default value to return if the collection is empty.

        Returns:
        - The first element of the collection, or the default value if the collection is empty.

        Example:
        # >>> lst = List([1, 2, 3])
        # >>> lst.FirstOrDefault(0)
        1
        """

        return self[0] if len(self) > 0 else default_value

    def ElementAt(self, element_index):
        """
        Selects a sequence element at a specific index.

        Args:
        - element_index (int): The index of the element to select.

        Returns:
        - The element at the specified index.

        Example:
        # >>> lst = List([1, 2, 3, 4, 5])
        # >>> lst.ElementAt(2)
        3
        """

        return self[element_index]

    def ElementAtOrDefault(self, element_index, default_value):
        """
        Selects a collection element at a specific index or returns a default value if the index is out of range.

        Args:
        - element_index (int): The index of the element to select.
        - default_value: The default value to return if the index is out of range.

        Returns:
        - The element at the specified index, or the default value if the index is out of range.

        Example:
        # >>> lst = List([1, 2, 3])
        # >>> lst.ElementAtOrDefault(3, "Not found")
        "Not found"
        """

        return self[element_index] if element_index < len(self) else default_value

    def Last(self):
        """
        Returns the last element of the collection.

        Returns:
        - The last element of the collection.

        Example:
        # >>> lst = List([1, 2, 3, 4, 5])
        # >>> lst.Last()
        5
        """

        return self[-1]

    def LastOrDefault(self, default_value):
        """
        Returns the last element of the collection or the default value if the collection is empty.

        Args:
        - default_value: The default value to return if the collection is empty.

        Returns:
        - The last element of the collection, or the default value if the collection is empty.

        Example:
        # >>> lst = List([1, 2, 3])
        # >>> lst.LastOrDefault(0)
        3
        """

        return self[-1] if len(self) > 0 else default_value

    def OrderBy(self, fun=None):
        """
        Arranges elements in ascending order.

        Args:
        - fun: The function used to specify the sorting order.

        Returns:
        - The list arranged in ascending order.

        Example:
        # >>> lst = List([3, 1, 2])
        # >>> lst.OrderBy()
        [1, 2, 3]
        """

        if fun is None:
            self.sort()
        else:
            self.sort(key=fun)
        return self

    def OrderByDescending(self, fun=None):
        """
        Arranges elements in descending order.

        Args:
        - fun: The function used to specify the sorting order.

        Returns:
        - The list arranged in descending order.

        Example:
        # >>> lst = List([3, 1, 2])
        # >>> lst.OrderByDescending()
        [3, 2, 1]
        """

        if fun is None:
            self.sort(reverse=True)
        else:
            self.sort(reverse=True, key=fun)
        return self

    def Reverse(self):
        """
        Arranges elements in reverse order.

        Returns:
        - The list arranged in reverse order.

        Example:
        # >>> lst = List([1, 2, 3])
        # >>> lst.Reverse()
        [3, 2, 1]
        """

        self.reverse()
        return self

    def Zip(self, second_list, fun_result_selector):
        """
        Combines two collections according to a certain condition.

        Args:
        - second_list (list): The second list to be zipped with the current list.
        - fun_result_selector: The function used to specify the zipping condition.

        Returns:
        - A new list formed by combining elements from both lists according to the specified condition.

        Example:
        # >>> lst1 = [1, 2, 3]
        # >>> lst2 = ['a', 'b', 'c']
        # >>> lst1.Zip(lst2, lambda x, y: str(x) + y)
        ['1a', '2b', '3c']
        """

        count = len(self) if len(self) < len(second_list) else len(second_list)
        output = List()
        for i in range(count):
            output.append(fun_result_selector(self[i], second_list[i]))
        return output

    def ToPythonList(self):
        """
        Returns the list as a standard Python list.

        Returns:
        - list: The list as a standard Python list.

        Example:
        # >>> lst = List([1, 2, 3])
        # >>> lst.ToPythonList()
        [1, 2, 3]
        """

        return self

    def ForEach(self, fun):
        """
        Applies a function to each element of the list.

        Args:
        - fun: The function to be applied to each element.

        Example:
        # >>> lst = List([1, 2, 3])
        # >>> lst.ForEach(lambda x: print(x))
        1
        2
        3
        """

        for n in self:
            fun(n)

    def Add(self, new_element):
        """
        Adds a new element to the list.

        Args:
        - new_element: The new element to be added to the list.
        """

        self.append(new_element)

    def AddRange(self, input_list):
        """
        Adds the elements of the input list to the current list.

        Args:
        - input_list (list or List): The list whose elements are to be added to the current list.

        Raises:
        - ValueError: If the input is not a valid list or List object.
        """

        if type(input_list) is list:
            self.extend(input_list)
        if type(input_list) is List:
            self.extend(input_list.ToPythonList())
        else:
            raise ValueError()

    def IndexOf(self, element):
        """
        Returns the index of the first occurrence of an element in the list.

        Args:
        - element: The element to find the index of.

        Returns:
        - int: The index of the first occurrence of the element.
        """

        self.index(element)

    def Insert(self, index, element):
        """
        Inserts the specified element at the specified index in the list.

        Args:
        - index (int): The index at which to insert the element.
        - element: The element to be inserted.
        """

        self.insert(index, element)

    def Remove(self, element):
        """
        Removes the first occurrence of the specified element from the list.

        Args:
        - element: The element to be removed.
        """

        self.remove(element)

    def RemoveAt(self, index):
        """
        Removes the element at the specified index from the list.

        Args:
        - index (int): The index of the element to be removed.
        """

        del self[index]

    def Union(self, second_list):
        """
        Returns a new list containing the union of elements from two source lists.

        Args:
        - second_list (list): The second list to form the union with.

        Returns:
        - list: A new list containing the union of elements from both lists.
        """

        return List(list(set(self + second_list)))
