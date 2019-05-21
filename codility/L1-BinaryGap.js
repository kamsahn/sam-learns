function solution(N) {
  // convert decimal number into a binary and then split each character into an array
  // not that each element of the array is a string
  const binArr = N.toString(2).split('')
  let maxGap = 0
  let storedIndex = null
  binArr.forEach((elem, index) => {
    // checks if there is a stored '1' to complete a binary gap
    // checks if the current element is '1'
    // checks if the diff between two stored indices is greater than the existing max gap
    if (storedIndex >= 0 && elem === '1' && (index - storedIndex) > maxGap) {
      // if all criteria are met, create a new maximum
      maxGap = index - storedIndex
    }
    // take the index of a '1' and store it for above use
    if (elem === '1') {
      storedIndex = index
    }
  })
  // after all elements have been checked, return the max gap - 1
  // binary gap is essentially counting the zeros in between the ones
  // and the current maxGap holds a '1' in that count
  return (maxGap - 1)
}
