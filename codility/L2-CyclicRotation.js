function solution(A, K) {
    let count = 0
    while (count < K) {
        A.unshift(A.pop())
        count++
    }
    return A
}
