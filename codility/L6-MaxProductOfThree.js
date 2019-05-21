function solution(A) {
    const sorted = A.sort((a, b) => a - b)
    const threeHigh = sorted[sorted.length - 3] * sorted[sorted.length - 2] * sorted[sorted.length - 1]
    const lowLowHigh = sorted[0] * sorted[1] * sorted[sorted.length - 1]
    return Math.max(threeHigh, lowLowHigh)
}
