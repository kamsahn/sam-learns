"""
Write an algorithm to justify text. Given a sequence of words and an integer
line length k, return a list of strings which represents each line, fully
justified.

More specifically, you should have as many words as possible in each line. There
should be at least one space between each word. Pad extra spaces when necessary
so that each line has exactly length k. Spaces should be distributed as equally
as possible, with the extra spaces, if any, distributed starting from the left.

If you can only fit one word on a line, then you should pad the right-hand side
with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words
["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
and k = 16, you should return the following:

[
"the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly
"""

def justify_text(k, word_list):
    """
    First, separate words into even-as-possible lines
    Second, add padding to each line to meet (and not exceed k)
    """
    def add_word(new_line, word):
        new_line += word
        # then add space if room
        if len(new_line) + 1 < k:
            new_line += " "
        return new_line

    def close_line(new_line, lines):
        # trim trailing space
        if new_line[-1] == " ":
            new_line = new_line[:-1]
        # append to lines and start over
        if new_line != "":
            lines.append(new_line)
            new_line = ""
        return new_line, lines

    # break up words into lines of chatacter count < k + (word count - 1)
    lines = []
    new_line = ""
    for word in word_list:
        # add word if room
        if len(new_line) + len(word) < k:
            new_line = add_word(new_line, word)
        # no more room for a word
        else:
            new_line, lines = close_line(new_line, lines)
            # then add the word
            new_line = add_word(new_line, word)

    # append remaining new_line
    new_line, lines = close_line(new_line, lines)

    # add padding to meet char count k
    final_lines = []
    for line in lines:
        dif = k - len(line)  # how many extra spaces we have
        if dif == 0:
            final_lines.append(line)
        else:
            space_count = len(line.split(" ")) - 1  # how many options we have
            # special case for 1 word line
            if space_count == 0:
                final_lines.append(line + (" " * dif))
            else:
                # add spaces evenly
                even_spaces = dif // space_count
                if even_spaces > 0:
                    new_space = " " * (even_spaces + 1)
                    line = line.replace(" ", new_space)
                else:
                    new_space = " "

                # add spaces from left
                from_left = dif % space_count
                if from_left > 0:
                    words = line.split(new_space)
                    for i in range(from_left):
                        words[i] = words[i] + " "
                    line = new_space.join(words)

                final_lines.append(line)

    return final_lines


print(justify_text(16, ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]))

