/*
Given two non-empty binary trees s and t,
check whether tree t has exactly the same structure and node values with a subtree of s.

A subtree of s is a tree consists of a node in s and all of this node's descendants.
The tree s could also be considered as a subtree of itself.
*/

// first make a function that checks if two trees are the same
// then make a function to traverse a tree and look for a match to the starting node

class Node {
    constructor(val, left=null, right=null) {
        this.val = val
        this.left = left
        this.right = right
    }
}

function treesAreEqual(node1, node2) {
    /*
    Node 1 is our original node - will use that as our guide
    Node 2 is our node in question
    */
    if (node1.val === node2.val) {
        if (node1.left && node1.right) {
            // node 1 has right and left branches
            const leftEqual = node2.left ? treesAreEqual(node1.left, node2.left) : false
            const rightEqual = node2.right ? treesAreEqual(node1.right, node2.right) : false
            return leftEqual && rightEqual
        } else if (node1.left) {
            // node 1 has only left branches
            return node2.left ? treesAreEqual(node1.left, node2.left) : false
        } else if (node1.right) {
            // node 1 has only right branches
            return node2.right ? treesAreEqual(node1.right, node2.right) : false
        } else {
            // node 1 has no branches
            return true
        }
    }
    return false
}

// test treesAreEqual function
//const tree1 = new Node(1, new Node(2), new Node(3, new Node(4), new Node(5)))
//const tree2 = new Node(1, new Node(2), new Node(3, new Node(4), new Node(5))) // same tree as 1
//const tree3 = new Node(1, new Node(2), new Node(3, new Node(4), new Node(5, new Node(6)))) // same sub tree as 1
//const tree4 = new Node(1, new Node(2, new Node(7)), new Node(3, new Node(4), new Node(5, new Node(6)))) // same sub tree as 1
//const tree5 = new Node(1, new Node(8, new Node(7)), new Node(3, new Node(4), new Node(5, new Node(6)))) // no similar sub tree as 1
//console.log(treesAreEqual(tree1, tree2))
//console.log(treesAreEqual(tree1, tree3))
//console.log(treesAreEqual(tree1, tree4))
//console.log(treesAreEqual(tree1, tree5))

function findEqualSubTree(t, s) {
    // t is our original tree
    // s is the tree that we will search for a similar subtree
    if (treesAreEqual(t, s)) {
        return true
    } else {
        // check s branches if present
        const leftEqual = s.left ? treesAreEqual(t, s.left) : false
        const rightEqual = s.right ? treesAreEqual(t, s.right) : false
        return leftEqual || rightEqual
    }
}

// test findEqualSubTree function
const tree1 = new Node(1, new Node(2), new Node(3, new Node(4), new Node(5)))
const tree2 = new Node(1, new Node(2), new Node(3, new Node(4), new Node(5))) // same tree as 1
const tree3 = new Node(1, new Node(2), new Node(3, new Node(4), new Node(5, new Node(6)))) // starts with same sub tree as 1
const tree4 = new Node(0, new Node(1, new Node(2), new Node(3, new Node(4), new Node(5, new Node(6))))) // encases same sub tree as 1
const tree5 = new Node(1, new Node(8, new Node(7)), new Node(3, new Node(4), new Node(5, new Node(6)))) // no similar subtrees as 1
console.log(findEqualSubTree(tree1, tree2))
console.log(findEqualSubTree(tree1, tree3))
console.log(findEqualSubTree(tree1, tree4))
console.log(findEqualSubTree(tree1, tree5))






