"""
Good morning! Here's your coding interview problem for today.
This problem was asked by Twitter.

Implement an autocomplete system.
That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.
For example, given the query string `de` and the set of strings [dog, deer, deal], return [deer, deal].
Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
"""

pos_strings = ['dog', 'deer', 'deal']

def autocomplete_list(s):
    """
    O[n] (n is words in list) each time
    """
    return [word for word in pos_strings if word.startswith(s)]

print(autocomplete_list('de'))

#

class Autocompleter():
    """
    Autocompleter takes a list of possible words and creates a dictionary store for all possible sub-string searches
    Autocompleter.autocomplete can then be called to return a list of words that matches the given sub-string query
    """
    def __init__(self, possible_strings):
        self.possible_strings = possible_strings
        self.store = self.construct_dict()

    def construct_dict(self):
        """
        Takes list of possible strings and sorts them into the autocomplete dictionary
        O[n*m] (n is words in list, m is letters in words) 1 time
        """
        pos_strings_dict = {}
        for word in self.possible_strings:
            sub_word = ""
            for let in word:
                sub_word += let
                if not pos_strings_dict.get(sub_word):
                    pos_strings_dict[sub_word] = {word}
                else:
                    pos_strings_dict[sub_word].add(word)

        return pos_strings_dict

    def autocomplete(self, s):
        return list(self.store.get(s, ["Couln't find a match..."]))


ac = Autocompleter(pos_strings)
print(ac.autocomplete('de'))
print(ac.autocomplete('d'))
print(ac.autocomplete('dea'))
print(ac.autocomplete('di'))

