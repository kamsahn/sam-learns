"""
In this exercise, you will develop a function named decode(message_file).
This function should read an encoded message from a .txt file and return its decoded version as a string.

Note that you can write your code using any language and IDE you want (Python is preferred if possible, but not mandatory).

Your function must be able to process an input file with the following format:

3 love
6 computers
2 dogs
4 cats
1 I
5 you
In this file, each line contains a number followed by a word.
The task is to decode a hidden message based on the arrangement of these numbers into a "pyramid" structure.
The numbers are placed into the pyramid in ascending order, with each line of the pyramid having one more number than the line above it.
The smallest number is 1, and the numbers increase consecutively, like so:

1
2 3
4 5 6
The key to decoding the message is to use the words corresponding to the numbers at the end of each pyramid line (in this example, 1, 3, and 6).
You should ignore all the other words. So for the example input file above, the message words are:

1: I
3: love
6: computers
and your function should return the string "I love computers".
"""


"""
    This code will:
    Read all the lines of a text file in the same directory named "coding_qual_input.txt". Lines will be read using Python built-in functions specifically used to read separate lines of a file that are separated by line breaks.
    Sort the words into a list using the number associated to each word i.e. "195 land" will be the 194th index and "1 down" will be the 0th index. Each line will be sorted by another Python built-in called sorted. We can assign a custom key with a lambda function. The key will be the integer present at the beginning of each line, separated from the remaining word by a space. Lastly, we will return a list of only words (strings) by again using some array slicing and the string method `split`.
    Arrange the words into a pyramid structure using a while loop. Using a step counter, we will create a sublist of words that will have the following shape:
      1
     2 3
    4 5 6
    and we will select the last word in each line using list slicing. We add this to a string variable initialized outside the while loop to hold our answer. After each iteration, we will decrease the size of the list (with more list slicing) until we don't have a large enough list to make the pyramid shape.
    Return the secret code string created by our while loop.
"""


def get_file_lines(filename: str) -> list[str]:
    file = open(filename, "r")
    lines = file.readlines()
    file.close()
    return lines


def mutate_lines(lines: list[str]) -> list[str]:
    sorted_lines = sorted(lines, key=lambda x: int(x.split(" ")[0]))
    sorted_words = []
    for line in sorted_lines:
        word = line.split(" ")[1][:-1]  # remove the line break from the end of each word
        sorted_words.append(word)
    return sorted_words


def assemble_code(lines: list[str]) -> str:
    secret_code = ""
    step = 1
    while len(lines) > 0 and len(lines) >= step:
        sub_lines = lines[:step]
        secret_code += f"{sub_lines[-1]} "
        lines = lines[step:]
        step += 1

    return secret_code[:-1]  # remove the trailing space
    

def main(filename: str) -> str:
    file_lines = get_file_lines(filename)
    mutated_lines = mutate_lines(file_lines)
    secret_code = assemble_code(mutated_lines)
    return secret_code


if __name__ == "__main__":
    filename = "coding_qual_input.txt"
    ans = main(filename)    
    # print(ans)  # for testing
