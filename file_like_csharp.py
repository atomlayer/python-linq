from linq_like_csharp import List


class File:

    @staticmethod
    def ReadAllLines(file_name: str, encoding='utf-8') -> List:
        with open(file_name, mode='r', encoding=encoding) as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        return List(content)

    @staticmethod
    def ReadAllText(file_name: str, encoding='utf-8') -> str:
        with open(file_name, mode='r', encoding=encoding) as f:
            content = f.read()
        return content

    @staticmethod
    def ReadAllBytes(file_name: str):
        with open(file_name, mode="rb") as f:
            content = f.read()
        return content

    @staticmethod
    def AppendAllLines(file_name: str, list, encoding='utf-8'):
        with open(file_name, mode="a+", encoding=encoding) as f:
            f.seek(0)
            data = f.read(100)
            if len(data) > 0:
                f.write("\n")
            for i, n in enumerate(list):
                f.write(n)
                if i != len(list) - 1:
                    f.write("\n")

    @staticmethod
    def AppendAllText(file_name: str, contents: str, encoding='utf-8'):
        with open(file_name, mode="a", encoding=encoding) as f:
            f.write(contents)

    @staticmethod
    def WriteAllLines(file_name: str, list, encoding='utf-8'):
        with open(file_name, mode="w", encoding=encoding) as f:
            f.writelines(list)

    @staticmethod
    def WriteAllText(file_name: str, contents: str, encoding='utf-8'):
        with open(file_name, mode="w", encoding=encoding) as f:
            f.write(contents)

    @staticmethod
    def WriteAllBytes(file_name: str, contents, encoding='utf-8'):
        with open(file_name, mode="wb", encoding=encoding) as f:
            f.write(contents)
