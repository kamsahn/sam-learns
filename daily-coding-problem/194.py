"""
Suppose you are given two lists of n points, one list p1, p2, ..., pn on the line y = 0
and the other list q1, q2, ..., qn on the line y = 1.

Imagine a set of n line segments connecting each point pi to qi.
Write an algorithm to determine how many pairs of the line segments intersect.
"""

# compare each set to all other sets
# if ((p1 >= p2 and q1 <= q2) or (p1 <= p2 and q1 >= q2)) -> add pair to intersection store
# intersection store will hold pairs of lines (order will not matter)


def get_intersections(p_line: list[int], q_line: list[int]) -> int:
    intersection_count = 0
    
    for i in range(len(p_line)):
        p1 = p_line[i]
        q1 = q_line[i]
        for j in range(i+1, len(p_line)):  # will not double count
            p2 = p_line[j]
            q2 = q_line[j]
            if (p1 >= p2 and q1 <= q2) or (p1 <= p2 and q1 >= q2):
                intersection_count += 1

    return intersection_count


if __name__ == "__main__":
    p_line = [1, 2, 3, 4, 5]
    q_line = [1, 2, 3, 4, 4]
    print(get_intersections(p_line, q_line))
    p_line = [1, 2, 3, 4, 5]
    q_line = [1, 2, 3, 4, 3]
    print(get_intersections(p_line, q_line))
    p_line = [1, -1, 3, 4, 5]
    q_line = [-2, 0, 3, 5, 0]
    print(get_intersections(p_line, q_line))
    p_line = [1, -1, 3, 4, 5, 6, 7, 8, 9, 10]
    q_line = [-2, 0, 3, 5, 0, 4, 20, 7, 2, 9]
    print(get_intersections(p_line, q_line))


"""kotlin
    fun main() {
    fun getIntersections(pLine: List<Int>, qLine: List<Int>): Int {
        var intersectionCount = 0
        val length = pLine.size

        for (i in (0..length-1)) {
            val p1 = pLine[i]
            val q1 = qLine[i]
            for (j in (i+1..length-1)) {
                val p2 = pLine[j]
                val q2 = qLine[j]
                if ((p1 >= p2 && q1 <= q2) || (p1 <= p2 && q1 >= q2)) {
                    intersectionCount += 1
                }
            }
        }

        return intersectionCount
    }

    val p_line1 = listOf(1, 2, 3, 4, 5)
    val q_line1 = listOf(1, 2, 3, 4, 4)
    println(getIntersections(p_line1, q_line1))
    val p_line2 = listOf(1, 2, 3, 4, 5)
    val q_line2 = listOf(1, 2, 3, 4, 3)
    println(getIntersections(p_line2, q_line2))
    val p_line3 = listOf(1, -1, 3, 4, 5)
    val q_line3 = listOf(-2, 0, 3, 5, 0)
    println(getIntersections(p_line3, q_line3))
    val p_line4 = listOf(1, -1, 3, 4, 5, 6, 7, 8, 9, 10)
    val q_line4 = listOf(-2, 0, 3, 5, 0, 4, 20, 7, 2, 9)
    println(getIntersections(p_line4, q_line4))

}
"""