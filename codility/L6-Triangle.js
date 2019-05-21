function solution(A) {
    const sorted = A.sort((a, b) => a - b).filter(num => num > 0)
    if (sorted.length < 3) { return 0 }
    for (let i = 0; i < sorted.length; i++) {
        if (sorted[i] + sorted[i+1] > sorted[i+2]) { return 1 }
        }
    return 0
}
