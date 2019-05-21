// function solution(A) {
//     const store = []
//     A.forEach(num => {
//         if (!store.includes(num)) { store.push(num) }
//     })
//     return store.length
// }

function solution(A) {
    if (A.length === 0) { return 0 }
    const sortedA = A.sort((a, b) => a - b)
    const store = [sortedA[0]]
    let lastNum = sortedA[0]
    sortedA.forEach(num => {
        if (num !== lastNum) {
          store.push(num)
          lastNum = num
        }
    })
    return store.length
}
