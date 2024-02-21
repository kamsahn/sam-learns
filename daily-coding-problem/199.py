"""
Given a string of parentheses, find the balanced string that can be produced from it using the minimum number of insertions and deletions.
If there are multiple solutions, return any of them.

For example, given "(()", you could return "(())". Given "))()(", you could return "()()()()".
"""


def fix_parens(parens: str) -> str:
    ans = ""
    opened = []
    closed = []
    
    for i in range(len(parens)):
        if parens[i] == ")":
            if len(opened):
                del opened[-1]
            else:
                closed.append(i)
        elif parens[i] == "(":
            opened.append(i)
    
    to_delete = set(opened + closed)
    
    for i in range(len(parens)):
        if i not in to_delete:
            ans += parens[i]
    
    return ans


if __name__ == "__main__":
    print(fix_parens("(()"))
    print(fix_parens("))()("))
    print(fix_parens("())()((())()"))
    

"""kotlin
    
    fun main() {
    fun fixParens(parens: String): String {
        var ans = ""
        val opened = mutableListOf<Int>()
        val closed = mutableListOf<Int>()

        parens.forEachIndexed { i, e -> 
            if (e.toString() == ")") {
                if (opened.size > 0) {
                    opened.removeLast()
                } else {
                    closed.add(i)
                }
            } else if (e.toString() == "(") {
                opened.add(i)
            }
        }

        val toDelete = opened + closed
        toDelete.toSet<Int>()

        parens.forEachIndexed { i, e ->
            if (i !in toDelete) {
                ans += e
            }
        }

        return ans
    }

    println(fixParens("(()"))
    println(fixParens("))()("))
    println(fixParens("())()((())()"))
}

"""
            