function solution(A) {
    const sorted = A.sort((a, b) => a - b)
    let notDone = true
    let count = 0
    while (notDone && count < sorted.length) {
        sorted[count] !== (count + 1) ? notDone = false : count++
    }
    return notDone ? 1 : 0
}
