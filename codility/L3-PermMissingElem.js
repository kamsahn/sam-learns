function solution(N) {
  if (A.length === 0) { return 0 }
  if (A.length === 1) { return A[0] === 1 ? 2 : 1 }
  const ans = A.sort((a, b) => a - b).find((num, index) => num !== (index + 1)) - 1
  return ans || (A.length + 1)
}
