/*
Invert a binary tree.

For example, given the following tree:

    a
   / \
  b   c
 / \  /
d   e f
should become:

  a
 / \
 c  b
 \  / \
  f e  d
*/

class Node {
    constructor(value, left = null, right = null) {
        this.value = value;
        this.left = left;
        this.right = right;
    }
}

function invertTree(tree) {
    const tempRight = tree.right;
    tree.right = tree.left;
    tree.left = tempRight;
    
    if (tree.left && tree.right) {
        tree.left = invertTree(tree.left);
        tree.right = invertTree(tree.right);
        return tree
    }
    else if (tree.left) {
        tree.left = invertedTree(tree.left)
        return tree
    } else if (tree.right) {
        tree.right = invertTree(tree.right)
        return tree
    } else {
        return tree
    }
}

const testTree = new Node("a", new Node("b", new Node("d"), new Node ("e")), new Node("c", new Node("f")))
console.log("a", testTree.value)
console.log("b", testTree.left.value)
console.log("c", testTree.right.value)
console.log("d", testTree.left.left.value)
console.log("e", testTree.left.right.value)
console.log("f", testTree.right.left.value)
console.log("null", testTree.right.right)
const invertedTree = invertTree(testTree)
console.log("a", invertedTree.value)
console.log("c", invertedTree.left.value)
console.log("b", invertedTree.right.value)
console.log("e", invertedTree.right.left.value)
console.log("d", invertedTree.right.right.value)
console.log("null", invertedTree.left.left)
console.log("f", invertedTree.left.right.value)