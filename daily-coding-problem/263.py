"""
Create a basic sentence checker that takes in a stream of characters and determines whether they form valid sentences.
If a sentence is valid, the program should print it out.

We can consider a sentence valid if it conforms to the following rules:

1. The sentence must start with a capital letter, followed by a lowercase letter or a space.
2. All other characters must be lowercase letters, separators (,,;,:) or terminal marks (.,?,!,‽).
3. There must be a single space between each word.
4. The sentence must end with a terminal mark immediately following a word.
"""

import string

def sentence_checker(stream: str) -> tuple[bool, int]:
    terminals = ".?!"
    separators = ",;:"
    white_space = " "
    # 1
    if stream[0] not in string.ascii_uppercase:
        return False, 1
    # 2
    for char in stream[1:-1]:
        if not (char in string.ascii_lowercase or char in separators or char == white_space):
            return False, 2
    # 3
    for i in range(1, len(stream)):
        if stream[i] == white_space and stream[i-1] == white_space:
            return False, 3
    # 4
    if not (stream[-1] in terminals and stream[-2] != white_space):
        return False, 4
    
    return True, 0


if __name__ == "__main__":
    print(sentence_checker("Applejacks brewing company."))
    print(sentence_checker("Pablo is a stinky cat, although he is cute."))
    print(sentence_checker("Anuke sadfkjejnkbdsfje, kjashdf: : :!"))
    print(sentence_checker("J?"))
    print(sentence_checker("will fail on one."))
    print(sentence_checker("Will fail on 2."))
    print(sentence_checker("Will fail  on three."))
    print(sentence_checker("Will fail on four"))





        
    
    