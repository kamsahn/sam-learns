"""
A step word is formed by taking a given word, adding a letter, and anagramming the result.
For example, starting with the word "APPLE", you can add an "A" and anagram to get "APPEAL".

Given a dictionary of words and an input word, create a function that returns all valid step words.
"""


def step_words(inp: str, word_dictionary: list[str]) -> list[str]:
    ans = []
    alphabet = list(map(chr, range(97, 123)))
    for letter in alphabet:
        temp = "".join(sorted(inp + letter))
        for word in word_dictionary:
            if temp == "".join(sorted(word)):
                ans.append(word)
    
    return ans

if __name__ == "__main__":
    word_dictionary = ["apple", "appeal", "be", "bee", "beer", "bet", "bets", "spot", "stop", "tops", "tons"]
    inp = "apple"
    print(step_words(inp, word_dictionary))    
    inp = "be"
    print(step_words(inp, word_dictionary))
    inp = "top"
    print(step_words(inp, word_dictionary))    
    inp = "tso"
    print(step_words(inp, word_dictionary))