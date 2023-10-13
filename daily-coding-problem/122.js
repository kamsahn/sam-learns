/*
You are given a 2-d matrix where each cell represents number of coins in that cell. 
Assuming we start at matrix[0][0], and can only move right or down, 
find the maximum number of coins you can collect by the bottom right corner.

For example, in this matrix

0 3 1 1
2 0 0 4
1 5 3 1

The most we can collect is 0 + 2 + 1 + 5 + 3 + 1 = 12 coins.
*/

// Use recursion 
// Base case returns total count
// at every junction, return max of each option
// "right" or "down" just means increasing x or y index

function get_max_coins(matrix) {
  const m_length = matrix.length;
  const m_width = matrix[0].length;
  function get_max_coins_helper(x, y, max) {
      // if reached the end of the matrix, return max
      // base case for recursion
      if (x+1 === m_length && y+1 === m_width) {
        return max + matrix[x][y]
      }

      // acount for max length and width
      if (x >= m_length || y >= m_width) {
        return 0
      }

      // add new position
      max += matrix[x][y]
      // get max case for right or down
      return Math.max(
        get_max_coins_helper(x+1, y, max),
        get_max_coins_helper(x, y+1, max)
      )
  }

  return get_max_coins_helper(0, 0, 0)
}

console.log(get_max_coins([[0, 3, 1, 1], [2, 0, 0, 4], [1, 5, 3, 1]]))