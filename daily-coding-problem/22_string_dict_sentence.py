"""
Good morning! Here's your coding interview problem for today.
This problem was asked by Microsoft.

Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list.
If there is more than one possible reconstruction, return any of them.
If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
"""

# iterate over each word
# if the first letter matches the next unmatched letter in the string
# check if the whole word matches the next n letters, where n is the number of letters in the word
# if so, append
# move next unmatched letter n spaces
# return list when all letters are matched
# return None if there are unmatched letters left

def string_dict_to_list(word_list, sentence):
    sentence_list = []
    unmatched_i = 0

    def loop_through_list(word_list, sentence, unmatched_i, sentence_list):
        for word in word_list:
            print(word)
            word_matches = True
            i = 0
            while word_matches and i < len(word):
                if word[i] != sentence[unmatched_i]:
                    word_matches = False
                else:
                    i += 1
                    unmatched_i += 1

                if i == len(word):
                    sentence_list.append(word)
                    
        return sentence_list, unmatched_i

    while len(word_list):
        new_sentence_list, new_unmatched_i = loop_through_list(word_list, sentence, unmatched_i, sentence_list)
        print(new_sentence_list)
        if new_unmatched_i == unmatched_i:
            return None
        elif ''.join(new_sentence_list) == sentence:
            return new_sentence_list
        else:
            if len(word_list) == 0:
                return None
            else:
                word_list.remove(new_sentence_list[-1])
        sentence_list, unmatched_i = new_sentence_list, new_unmatched_i



# word_list = ['quick', 'brown', 'the', 'fox']
# sentence = "thequickbrownfox"
# print(string_dict_to_list(word_list, sentence))
#
# word_list = ['bed', 'bath', 'bedbath', 'and', 'beyond']
# sentence = "bedbathandbeyond"
# print(string_dict_to_list(word_list, sentence))

word_list = ['bath', 'bedbath', 'bed', 'and', 'beyond']
sentence = "bedbathandbeyond"
print(string_dict_to_list(word_list, sentence))

word_list = ['quick', 'the', 'fox']
sentence = "thequickbrownfox"
print(string_dict_to_list(word_list, sentence))

word_list = ['quick', 'brown', 'the']
sentence = "thequickbrownfox"
print(string_dict_to_list(word_list, sentence))


