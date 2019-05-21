function solution(A) {
    let store = 0
    let ans = 0
    for (let i = 0; i < A.length; i++) {
        A[i] ? ans += store : store++
        if (ans > 1000000000) { return -1 }
    }
    return ans
}
