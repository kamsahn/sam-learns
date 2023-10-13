/*
Given a set of closed intervals, 
find the smallest set of numbers that covers all the intervals. 
If there are multiple smallest sets, return any of them.

For example, given the intervals 
[0, 3], [2, 6], [3, 4], [6, 9], 
one set of numbers that covers all these intervals is {3, 6}.
*/

/*
Will need to look through each set at least once
Add each number of each interval to an active set
Whatever does NOT get added is part of the answer set
If nothing added to answer set, return active set (no similar spans)
*/

function smallestSet(intervals) {
  const activeSet = new Set()
  const answerSet = new Set()

  intervals.forEach(interval => {
    interval.forEach(elem => {
      if (activeSet.has(elem)) {
        answerSet.add(elem)
      } else {
        activeSet.add(elem)
      }
    })
  })
  return answerSet.size > 0 ? answerSet : activeSet
}

console.log(smallestSet([[0, 3], [2, 6], [3, 4], [6, 9], [9, 10], [0, 1], [0, 9], [8, 9]]))
console.log(smallestSet([[0, 3]]))
console.log(smallestSet([[0, 3], [2, 6]]))
console.log(smallestSet([[0, 3], [2, 6], [3, 4]]))
console.log(smallestSet([[0, 3], [2, 6], [3, 4], [6, 7]]))
console.log(smallestSet([[0, 3], [2, 6], [3, 4], [6, 9]]))
console.log(smallestSet([[0, 3], [2, 6], [3, 4], [6, 100]]))
console.log(smallestSet([[0, 4], [1, 2], [5, 6]]))