function solution(X, A) {
    if (X > A.length) { return -1 }
    const store = {}
    let done = false
    let notFound = false
    let count = 0
    while (!done && !notFound) {
        A[count] <= X && !store[A[count]] ? store[A[count]] = true : count++
        if (Object.keys(store).length === X) { done = true }
        if (count + 1 === A.length && !done) { notFound = true }
    }
    return done && !notFound ? count : -1
}
