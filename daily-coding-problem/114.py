"""
Given a string and a set of delimiters,
reverse the words in the string while maintaining the relative order of the delimiters.
For example, given "hello/world:here", return "here/world:hello"

Follow-up: Does your solution work for the following cases: "hello/world:here/", "hello//world:here"
"""

"""
make a function to split the string into two lists: words, delimiters
reverse word list
zip them back together
"""

# step through string, char by char
# write to two different lists depending on a-z char or other (isalpha())
# zip two lists together with slicing
# return in correct order


def split_string(full_string: str) -> tuple[list[str], list[str]]:
    words = []
    delimiters = []
    alpha = False
    temp = ""
    for char in full_string:
        if char.isalpha():
            if alpha:
                # continue building alpha word
                temp = temp + char
            else:
                # append to delimieters and start new word
                alpha = True
                if temp:
                    delimiters.append(temp)
                    temp = ""
                temp = temp + char
        else:
            if alpha:
                # append to words and start new delimieter
                alpha = False
                if temp:
                    words.append(temp)
                    temp = ""
                temp = temp + char
            else:
                temp = temp + char
    # append the final element
    if temp[0].isalpha():
        words.append(temp)
    else:
        delimiters.append(temp)
        
    words.reverse()
    return words, delimiters


def zip_lists(primary_list: list[str], secondary_list: list[str]) -> str:
    res = [""] * (len(primary_list) + len(secondary_list))  # create a list of proper length
    res[::2] = primary_list  # starting at index 0, slice elements in at every other index
    res[1::2] = secondary_list  # starting at index 1, slice elements in at every other index 
    return "".join(res)  # join single list to string


def main(s: str) -> str:
    starting_alpha = s[0].isalpha()
    words, delimeters = split_string(s)
    return zip_lists(words, delimeters) if starting_alpha else zip_lists(delimeters, words)


if __name__ == "__main__":
    print(main("hello/world:here"))
    print(main("hello/world:here/"))
    print(main("hello//world:here"))
    print(main("/my:name//is--joe["))

            
