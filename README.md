# python-linq
python-linq is a library that implements the basic linq C# methods in python.


## Installation

From Github:
```bash
pip install https://github.com/atomlayer/python-linq/archive/master.zip
```

## Example

### Example of operations with lists
```python

from python_linq.linq_like_csharp import List
array = [1, 50, 60, -30, 60, -50]
my_list = List(array).Select(lambda x: x * 3).Where(lambda x: x > 0)
print(my_list)

Result: [3, 150, 180, 180]
```

### Example of file operations
```python

from python_linq.file_like_csharp import File
file_text = File.ReadAllText("example.txt")
```


## Available methods

| Linq methods       | File methods   |
| ------------------ | -------------- |
| Select             | ReadAllLines   |
| SelectMany         | ReadAllText    |
| Where              | ReadAllBytes   |
| GroupBy            | AppendAllLines |
| Except             | AppendAllText  |
| Single             | WriteAllLines  |
| SingleOrDefault    | WriteAllText   |
| Join               | WriteAllBytes  |
| Any                |                |
| All                |                |
| Contains           |                |
| Distinct           |                |
| Concat             |                |
| Intersect          |                |
| Count              |                |
| Sum                |                |
| Average            |                |
| Min                |                |
| Max                |                |
| Take               |                |
| Skip               |                |
| TakeWhile          |                |
| SkipWhile          |                |
| First              |                |
| FirstOrDefault     |                |
| ElementAt          |                |
| ElementAtOrDefault |                |
| Last               |                |
| LastOrDefault      |                |
| OrderBy            |                |
| OrderByDescending  |                |
| Reverse            |                |
| Zip                |                |
| ForEach            |                |
| Add                |                |
| AddRange           |                |
| IndexOf            |                |
| Insert             |                |
| Remove             |                |
| RemoveAt           |                |
| Union                   |                |

