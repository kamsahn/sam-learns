"""
You are given an string representing the initial conditions of some dominoes. Each element can take one of three values:

L, meaning the domino has just been pushed to the left,
R, meaning the domino has just been pushed to the right, or
., meaning the domino is standing still.

Determine the orientation of each tile when the dominoes stop falling. 
Note that if a domino receives a force from the left and right side simultaneously, it will remain upright.

For example, given the string .L.R....L, you should return LL.RRRLLL.

Given the string ..R...L.L, you should return ..RR.LLLL.
"""

# iterate from left
# if L is found, all dominoes preceding will be L
# if R is found, iterate until a L is found, then split that sub array
# restart the process after the "closing L" is found

def dominoes(domino_string: str) -> str:
    ans = ""
    opening_r = None
    last_index_edited = 0
    for i in range(len(domino_string)):
        if opening_r is None:
            if domino_string[i] == "L":
                ans += "L"*(i - last_index_edited + 1)
                last_index_edited = i
            elif domino_string[i] == "R":
                ans += "."*(i - 1 - last_index_edited)
                opening_r = i
                last_index_edited = i
        else:
            if domino_string[i] == "L":
                mid_length = i - opening_r + 1
                ans += "R"*(mid_length // 2)
                if mid_length % 2 != 0:
                    ans += "."
                ans += "L"*(mid_length // 2)
                opening_r = None
                last_index_edited = i
        
        # print(i, ans, domino_string[i])
    
    if opening_r is not None:
        ans += "R"*(len(domino_string) - opening_r)
    
    return ans


if __name__ == "__main__":
    print("input: .L.R....L, output:", dominoes(".L.R....L"))    
    print("input: ..R...L.L, output:", dominoes("..R...L.L"))