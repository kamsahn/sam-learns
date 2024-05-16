"""
The "look and say" sequence is defined as follows:
beginning with the term 1, each subsequent term visually describes the digits appearing in the previous term.
The first few terms are as follows:

1
11
21
1211
111221

As an example, the fourth term is 1211, since the third term consists of one 2 and one 1.

Given an integer N, print the Nth term of this sequence.
"""

def look_and_say(n: int, seq: list[int] = [1]) -> int:
    if len(seq) == n:
        return seq[-1]
    next_seq = ""
    temp = ""
    
    for char in str(seq[-1]):
        if temp == "" or temp[-1] == char:
            temp += char
        else:
            next_seq += str(len(temp)) + temp[-1]
            temp = char
    
    next_seq += str(len(temp)) + temp[-1]
    seq.append(int(next_seq))
    return look_and_say(n, seq)


if __name__ == "__main__":
    print(look_and_say(1))
    print(look_and_say(2))
    print(look_and_say(3))
    print(look_and_say(4))
    print(look_and_say(5))
    print(look_and_say(6))
    print(look_and_say(7))

        
    