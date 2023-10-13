"""
Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
"""

truthy_input = "([])[]({})"
falsey_input_1 = "([)]"
falset_input_2 = "((()"

def is_balanced(bracket_string):
    # create a string store for unclosed bracket
    unclosed = ""
    for i in bracket_string:
        # store an open bracket
        if i in ["(", "[", "{"]:
            unclosed += i

        # check if bracket is going to close
        else:
            if unclosed == "":
                # cannot close if nothing is there
                return False
            elif i == ")" and unclosed[-1] == "(" or \
                i == "]" and unclosed[-1] == "[" or \
                i == "}" and unclosed[-1] == "{":
                # close a bracket and remove from unclosed
                unclosed = unclosed[:-1]
    return True if unclosed == "" else False

print(is_balanced(truthy_input), "should be True")
print(is_balanced(falsey_input_1), "should be False")
print(is_balanced(falset_input_2), "should be False")
print(is_balanced("(({{{[]}}}))"), "should be True")
print(is_balanced("}(((({{}}))))"), "should be False")
print(is_balanced("[(((({{}}))))"), "should be False")
print(is_balanced("["), "should be False")
print(is_balanced("]"), "should be False")
print(is_balanced("{{{{{{}}}}}}["), "should be False")
print(is_balanced("{{{{{{}}}}}}]"), "should be False")
print(is_balanced("{{{()}}}{}[[()]]{}"), "should be True")

