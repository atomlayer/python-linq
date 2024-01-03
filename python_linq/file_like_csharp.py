from python_linq.linq_like_csharp import List


class File:

    @staticmethod
    def ReadAllLines(file_name: str, encoding='utf-8') -> List:
        """
        Reads all the lines from a text file and returns them as a list of strings.

        Args:
        - file_name (str): The name of the file to read.
        - encoding (str): The encoding of the file (default is 'utf-8').

        Returns:
        - List: A list of strings representing the lines of the file.

        Example:
        # >>> lines = File.ReadAllLines("example.txt")
        # >>> print(lines)
        ["line 1", "line 2", "line 3"]
        """

        with open(file_name, mode='r', encoding=encoding) as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        return List(content)

    @staticmethod
    def ReadAllText(file_name: str, encoding='utf-8') -> str:
        """
        Reads all the text from a file and returns it as a string.

        Args:
        - file_name (str): The name of the file to read.
        - encoding (str): The encoding of the file (default is 'utf-8').

        Returns:
        - str: The content of the file as a string.

        Example:
        # >>> text = File.ReadAllText("example.txt")
        # >>> print(text)
        "This is the content of the file."
        """

        with open(file_name, mode='r', encoding=encoding) as f:
            content = f.read()
        return content

    @staticmethod
    def ReadAllBytes(file_name: str):
        """
        Reads all the bytes from a binary file and returns them as bytes.

        Args:
        - file_name (str): The name of the binary file to read.

        Returns:
        - bytes: The content of the file as bytes.

        Example:
        # >>> content = File.ReadAllBytes("example.bin")
        """

        with open(file_name, mode="rb") as f:
            content = f.read()
        return content

    @staticmethod
    def AppendAllLines(file_name: str, list, encoding='utf-8'):
        """
        Appends a list of strings as lines to a text file.

        Args:
        - file_name (str): The name of the file to append to.
        - list: The list of strings to append as lines.
        - encoding (str): The encoding of the file (default is 'utf-8').

        Example:
        # >>> lines = ["new line 1", "new line 2"]
        # >>> File.AppendAllLines("example.txt", lines)
        """

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
        """
        Appends text to a file.

        Args:
        - file_name (str): The name of the file to append to.
        - contents (str): The text to append.
        - encoding (str): The encoding of the file (default is 'utf-8').

        Example:
        # >>> File.AppendAllText("example.txt", "additional content")
        """

        with open(file_name, mode="a", encoding=encoding) as f:
            f.write(contents)

    @staticmethod
    def WriteAllLines(file_name: str, list, encoding='utf-8'):
        """
        Writes a list of strings as lines to a text file, overwriting its previous content.

        Args:
        - file_name (str): The name of the file to write to.
        - list: The list of strings to write as lines.
        - encoding (str): The encoding of the file (default is 'utf-8').

        Example:
        # >>> lines = ["new line 1", "new line 2"]
        # >>> File.WriteAllLines("example.txt", lines)
        """

        with open(file_name, mode="w", encoding=encoding) as f:
            f.writelines(list)

    @staticmethod
    def WriteAllText(file_name: str, contents: str, encoding='utf-8'):
        """
        Writes text to a file, overwriting its previous content.

        Args:
        - file_name (str): The name of the file to write to.
        - contents (str): The text to write.
        - encoding (str): The encoding of the file (default is 'utf-8').

        Example:
        # >>> File.WriteAllText("example.txt", "new content")
        """

        with open(file_name, mode="w", encoding=encoding) as f:
            f.write(contents)

    @staticmethod
    def WriteAllBytes(file_name: str, contents, encoding='utf-8'):
        """
        Writes bytes to a binary file, overwriting its previous content.

        Args:
        - file_name (str): The name of the binary file to write to.
        - contents: The bytes to write.
        """

        with open(file_name, mode="wb", encoding=encoding) as f:
            f.write(contents)
