function solution(A) {
    let maxProf = Number.NEGATIVE_INFINITY
    for (let i = 0; i < A.length - 1; i++) {
        A.slice(i+1, A.length).forEach(val => {
            if (val - A[i] > maxProf) { maxProf = val - A[i] }
        })
    }
    return maxProf
}
