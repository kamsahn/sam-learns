function solution(A) {
    if (A.length === 1) { return A[0] === 1 ? 2 : 1 }
    const sorted = A.sort((a, b) => a - b)
    if (sorted[A.length - 1] < 0) { return 1 }
    const store = []
    for (let i = 0; i < sorted.length; i++) {
        if (sorted[i] > 0 && !store.includes(sorted[i])) {
            store.push(sorted[i])
            if (store.length !== sorted[i]) {
                return store.length
            }
        }
    }
    return A.length + 1
}
