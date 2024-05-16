"""
Write a function, throw_dice(N, faces, total), that determines how many ways it is possible to throw N dice with some number of faces each to get a specific total.

For example, throw_dice(3, 6, 7) should equal 15.
"""
class DiceThrower:
    def __init__(self, n: int, faces: int, total: int):
        self.n = n
        self.faces = faces
        self.total = total
        self.ans = 0
        self.c = 0

    def helper(self, m, rolls: int):
        self.c += 1
        if m > 0:
            for i in range(1, self.faces+1):
                if i+rolls > self.total:
                    break
                self.helper(m-1, i+rolls)

        else:
            if self.total - rolls == 0:
                self.ans += 1

    def throw_dice(self) -> int:
        self.helper(self.n, 0)
        print(">>>", self.c)
        return self.ans
    

def throw_dice(n: int, faces: int, total: int) -> int:
    ans = 0
    def helper(m: int, rolls: int) -> None:
        if m > 0:
            for i in range(1, faces+1):
                if i+rolls > total:
                    break
                helper(m-1, i+rolls)

        else:
            # found out about nonlocal to get variable scoping from outer functions
            nonlocal ans
            if total - rolls == 0:
                ans += 1

    helper(n, 0)
    return ans


if __name__ == "__main__":
    # print(DiceThrower(3, 6, 7).throw_dice())
    # print(DiceThrower(2, 6, 7).throw_dice())
    # print(DiceThrower(2, 6, 8).throw_dice())
    # print(DiceThrower(4, 4, 6).throw_dice())
    # print(DiceThrower(5, 4, 8).throw_dice())
    print(throw_dice(3, 6, 7))    
    print(throw_dice(2, 6, 7))    
    print(throw_dice(4, 4, 6))
    print(throw_dice(5, 4, 8))