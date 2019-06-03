// If we were to set up a Tic-Tac-Toe game, we would want to know whether the board's current state is solved, wouldn't we? Our goal is to create a function that will check that for us!
//
// Assume that the board comes in the form of a 3x3 array, where the value is 0 if a spot is empty, 1 if it is an "X", or 2 if it is an "O", like so:
//
// [[0, 0, 1],
//  [0, 1, 2],
//  [2, 1, 0]]
// We want our function to return:
//
// -1 if the board is not yet finished (there are empty spots),
// 1 if "X" won,
// 2 if "O" won,
// 0 if it's a cat's game (i.e. a draw).
// You may assume that the board passed in is valid in the context of a game of Tic-Tac-Toe.

function isSolved(board) {
  const flat = [].concat.apply([], board)
  if (flat[0] && flat[0] === flat[1] && flat[0] === flat[2]) { return flat[0] }
  if (flat[3] && flat[3] === flat[4] && flat[3] === flat[5]) { return flat[3] }
  if (flat[6] && flat[6] === flat[7] && flat[6] === flat[8]) { return flat[6] }
  if (flat[0] && flat[0] === flat[3] && flat[0] === flat[6]) { return flat[0] }
  if (flat[1] && flat[1] === flat[4] && flat[1] === flat[7]) { return flat[1] }
  if (flat[2] && flat[2] === flat[5] && flat[2] === flat[8]) { return flat[2] }
  if (flat[0] && flat[0] === flat[4] && flat[0] === flat[8]) { return flat[0] }
  if (flat[2] && flat[2] === flat[4] && flat[2] === flat[6]) { return flat[2] }
  if (flat.some(space => space < 1)) { return -1 }
  return 0
}
