function solution(A) {
    if (A.length === 2) { return Math.abs(A[0] - A[1]) }
    let sumLeft = 0
    let sumRight = A.reduce((a, b) => a + b)
    let minDiff = Number.POSITIVE_INFINITY
    for (let i = 0; i < A.length; i++) {
        if (minDiff !== 1) {
            sumLeft += A[i]
            sumRight -= A[i]
            let currDiff = Math.abs(sumLeft - sumRight)
            minDiff = Math.min(minDiff, currDiff)
        }
    }
    return minDiff
}

// function solution(A) {
//     if (A.length === 2) { return Math.abs(A[0] - A[1]) }
//     let min = null
//     A.forEach((num, index) => {
//         if (index > 0 && min !== 1) {
//             test = Math.abs(A.slice(0, index).reduce((a, b) => a + b) - A.slice(index, A.length).reduce((a, b) => a + b))
//             if (!min || test < min) {
//                 min = test
//             }
//         }
//     })
//     return min
// }
