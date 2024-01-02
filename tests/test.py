from python_linq.linq_like_csharp import List
from python_linq.file_like_csharp import File

def join_test():
    x = [
        {"m": 6, 'id': 1},
        {"m": 8, 'id': 5},
        {"m": 7, 'id': 2},
        {"m": 0, 'id': 4}
    ]

    y = [
        {"b": 3300, 'id': 0},
        {"b": 45343, 'id': 11},
        {"b": 45635643, 'id': 1},
        {"b": 456356, 'id': 4}
    ]

    r = List(x).Join(y, lambda n: n['id'],
                     lambda o: o['id'],
                     lambda n, o: {"id": n['id'], 'm': n['m'], 'b': o['b']})

    print(r)


#  result:   [{'id': 1, 'm': 6, 'b': 45635643}, {'id': 4, 'm': 0, 'b': 456356}]


def select_many_test():
    x = [[10, 10, 220, 30], [60, 50, 33, 1, 52]]
    r = List(x).SelectMany(lambda y: y * 10)

    print(r)


# result: [100, 100, 2200, 300, 600, 500, 330, 10, 520]


def test_linq():
    x = List([10, 20, 1, 60, 30, 10, 10, -10]) \
        .Select(lambda x: x * 2) \
        .Where(lambda x: x < 40) \
        .OrderByDescending() \
        .GroupBy(lambda x: x)
    print(x)

    File.ReadAllLines("test.txt") \
        .Select(lambda x: int(x)) \
        .Where(lambda x: x < 60) \
        .OrderBy() \
        .ForEach(print)



def union_test():
    x = [20, 10, 30, 50]
    y = [60, 20, 30, 60]
    print(List(x).Union(y))


# result: [10, 50, 20, 60, 30]


def zip_test():
    x = ["A", "B", "C", "D", "E"]
    y = [1, 2, 3]

    print(List(x).Zip(y, lambda n, o: n + str(o)))


# ['A1', 'B2', 'C3']


def append_all_lines_to_file_test():
    file_name = 'test.txt'
    array = ["10", "44532"]

    File.AppendAllLines(file_name, array)




if __name__ == '__main__':

    # List(['dfvdfv','dfvdfv']).Select(lambda x:x+"  666").ForEach(print)

    List(['dfvdfv','dfv']).Where(lambda x:len(x)==3).ForEach(print)


    