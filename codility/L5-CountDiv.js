function solution(A, B, K) {
    if (A === B) { return A % K === 0 ? 1 : 0 }
    if (K === 1) { return B - A + 1 }
    if (K === 2) {
      if (A % 2 !== B % 2) {
        return (B - A + 1) / 2
      } else if (A % 2 === 0) {
        return (B - A + 2) / 2
      } else {
        return (B - A) / 2
      }
    }
    let count = 0
    let i = A === 0 ? 0 : Math.max(A, K)
    while (i <= B) {
        if (i % K === 0) {
        count++
        i += K
      } else {
          i++
      }
    }
    return count
}
