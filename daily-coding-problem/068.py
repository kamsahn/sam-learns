"""
On our special chessboard, two bishops attack each other if they share the same diagonal.
This includes bishops that have another bishop located between them, i.e. bishops can attack through pieces.

You are given N bishops, represented as (row, column) tuples on a M by M chessboard.
Write a function to count the number of pairs of bishops that attack each other.
The ordering of the pair doesn't matter: (1, 2) is considered the same as (2, 1).

For example, given M = 5 and the list of bishops:

(0, 0)
(1, 2)
(2, 2)
(4, 0)
The board would look like this:

[b 0 0 0 0]
[0 0 b 0 0]
[0 0 b 0 0]
[0 0 0 0 0]
[b 0 0 0 0]
You should return 2, since bishops 1 and 3 attack each other, as well as bishops 3 and 4.
"""

# exhaustive approach: given any point, check all diagonal points within the bounds, include any collisions

def check_diagonal(point: tuple[int], M: int, N: list[tuple[int]]) -> list:
    ans = []
    
    # down right
    temp_point = point[0], point[1]
    while 0 <= temp_point[0] < M and 0 <= temp_point[1] < M:
        temp_point = temp_point[0]+1, temp_point[1]+1
        if temp_point in N:
            ans.append((point, temp_point))
    
    # down left
    temp_point = point[0], point[1]
    while 0 <= temp_point[0] < M and 0 <= temp_point[1] < M:
        temp_point = temp_point[0]+1, temp_point[1]-1
        if temp_point in N:
            ans.append((point, temp_point))
    
    # up right
    temp_point = point[0], point[1]
    while 0 <= temp_point[0] < M and 0 <= temp_point[1] < M:
        temp_point = temp_point[0]-1, temp_point[1]+1
        if temp_point in N:
            ans.append((point, temp_point))

    # up left
    temp_point = point[0], point[1]
    while 0 <= temp_point[0] < M and 0 <= temp_point[1] < M:
        temp_point = temp_point[0]-1, temp_point[1]-1
        if temp_point in N:
            ans.append((point, temp_point))
    
    return ans
            
            

def bishops(M: int, N: list[tuple[int]]) -> int:
    ans = 0
    for n in N:
        list_of_pairs = check_diagonal(n, M, N)
        ans += len(list_of_pairs)
    
    # ans should be double the answer since we are counting each pair twice
    return ans // 2 if ans != 0 else ans
    


if __name__ == "__main__":
    """
    [b 0 0 0 0]
    [0 0 b 0 0]
    [0 0 b 0 0]
    [0 0 0 0 0]
    [b 0 0 0 0]
    """
    print(bishops(5, [(0, 0), (1, 2), (2, 2), (4, 0)]))
    
    """
    [b 0 0 0 0]
    [0 0 b 0 0]
    [0 0 0 b 0]
    [0 0 0 0 0]
    [b 0 0 0 0]
    """
    print(bishops(5, [(0, 0), (1, 2), (2, 3), (4, 0)]))
    
    """
    [b 0 0 0 0]
    [0 0 b 0 0]
    [0 0 0 0 b]
    [0 0 0 0 0]
    [b 0 0 0 0]
    """
    print(bishops(5, [(0, 0), (1, 2), (2, 4), (4, 0)]))
    
    """
    [b 0 0 0 0]
    [0 b 0 0 0]
    [0 0 b 0 0]
    [0 0 0 b 0]
    [0 0 0 0 b]
    """
    print(bishops(5, [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]))


    """
    [b 0 0 0 b]
    [0 0 0 0 0]
    [0 0 b 0 0]
    [0 0 0 0 0]
    [b 0 0 0 b]
    """
    print(bishops(5, [(0, 0), (0, 4), (2, 2), (4, 0), (4, 4)]))
        
