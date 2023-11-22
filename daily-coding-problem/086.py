"""
Given a string of parentheses,
write a function to compute the minimum number of parentheses to be removed to make the string valid
(i.e. each open parenthesis is eventually closed).

For example, given the string "()())()", you should return 1.
Given the string ")(", you should return 2, since we must remove all of them.
"""

# read the string
# for every open parens, add to the open count
# for every close parens, sub from the open count if there are any, else add to closed count
# return remaining sum of counts


def min_parentheses(parentheses: str) -> int:
    open_count = 0
    close_count = 0
    
    for p in parentheses:
        if p == "(":
            open_count += 1
        else:
            if open_count:
                open_count -= 1
            else:
                close_count += 1
    
    return open_count + close_count


if __name__ == "__main__":
    print("expected 1:", min_parentheses("()())()"))
    print("expected 2:", min_parentheses(")("))
    print("expected 3:", min_parentheses(")()()())(()"))
    print("expected 4:", min_parentheses(")()(((())(()"))
    print("expected 3:", min_parentheses("((("))
    print("expected 3:", min_parentheses(")))"))
    print("expected 4:", min_parentheses(")))("))
    print("expected 2:", min_parentheses(")())"))
