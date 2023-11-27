"""
Using a read7() method that returns 7 characters from a file, implement readN(n) which reads n characters.

For example, given a file with the content “Hello world”, three read7() returns “Hello w”, “orld” and then “”.
"""


def read7(filename: str, n: int = 1) -> str:
    end = 7 * n
    file = open(filename, "r")
    text = file.readlines()[0]
    return text[0:end]


def readN(filename: str, n: int) -> str:
    return read7(filename, n)


if __name__ == "__main__":
    print(readN("082.txt", 3))
