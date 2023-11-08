/*
Given a 2D board of characters and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.

For example, given the following board:

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
exists(board, "ABCCED") returns true,
exists(board, "SEE") returns true,
exists(board, "ABCB") returns false.
*/

// create a cell class that holds the value, neighbors and state
// use recursion to check each neighbor

class Cell {
    constructor(value,
                left=null,
                right=null,
                top=null,
                bottom=null,
                ready=true) {
        this.value = value;
        this.left = left;
        this.right = right;
        this.top = top;
        this.bottom = bottom;
        this.ready = ready;
    }
}

// cell helpers
function match(cell, letter) {
    if (cell && cell.ready && cell.value === letter) {
        cell.ready = false;
        return true
    }
    return false
}

function pair_horizontal(leftCell, rightCell) {
    leftCell.right = rightCell
    rightCell.left = leftCell
}

function pair_vertical(topCell, bottomCell) {
    topCell.bottom = bottomCell
    bottomCell.top = topCell
}

function exists(board, word) {
    function existsHelper(board, word, i) {
        board.ready = false;
        if (word.length === i+1) {
            return true
        }
        if (match(board.left, word[i+1])) {
            return existsHelper(board.left, word, i+1)
        }
        if (match(board.right, word[i+1])) {
            return existsHelper(board.right, word, i+1)
        }
        if (match(board.top, word[i+1])) {
            return existsHelper(board.top, word, i+1)
        }
        if (match(board.bottom, word[i+1])) {
            return existsHelper(board.bottom, word, i+1)
        }
        return false
    }
    return match(board, word[0]) ? existsHelper(board, word, 0) : false
}

// create the board
/*
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
*/
const c00 = new Cell('A');
const c01 = new Cell('B');
const c02 = new Cell('C');
const c03 = new Cell('E');
const c10 = new Cell('S');
const c11 = new Cell('F');
const c12 = new Cell('C');
const c13 = new Cell('S');
const c20 = new Cell('A');
const c21 = new Cell('D');
const c22 = new Cell('E');
const c23 = new Cell('E');

pair_horizontal(c00, c01);
pair_horizontal(c01, c02);
pair_horizontal(c02, c03);
pair_horizontal(c10, c11);
pair_horizontal(c11, c12);
pair_horizontal(c12, c13);
pair_horizontal(c20, c21);
pair_horizontal(c21, c22);
pair_horizontal(c22, c23);

pair_vertical(c00, c10);
pair_vertical(c10, c20);
pair_vertical(c01, c11);
pair_vertical(c11, c21);
pair_vertical(c02, c12);
pair_vertical(c12, c22);
pair_vertical(c03, c13);
pair_vertical(c13, c23);

// treat top corner node as the "board"
// needs to happen in a vaccum (board state must be reset)
console.log("ABF expected true:", exists(c00, "ABF")) // starts from corner
//console.log("ABS expected false:", exists(c00, "ABS"))
//console.log("ABCCED expected true:", exists(c00, "ABCCED")) // goes backward
//console.log("SEE expected true:", exists(c00, "SEE")) // starts from anywhere
//console.log("ABCB expected false:", exists(c00, "ABCB")) // does not reuse
