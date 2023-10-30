/*
Given a binary tree, return all paths from the root to leaves.

For example, given the tree:

   1
  / \
 2   3
    / \
   4   5
Return [[1, 2], [1, 3, 4], [1, 3, 5]].
*/

// solve using a class and recursion

class Node {
    constructor(value, left=null, right=null) {
        this.value = value;
        this.left = left;
        this.right = right;
    }
}

// add each value to an existing path list
// return list of lists

function getAllPaths(root) {
    const pathStore = []
    function getAllPathsHelper(node, path) {
        path.push(node.value)
        if (!node.left && !node.right) {
            pathStore.push(path)
        } else {
            if (node.left) {
                getAllPathsHelper(node.left, [...path])
            }
            if (node.right) {
                getAllPathsHelper(node.right, [...path])
            }
        }
    }
    getAllPathsHelper(root, [])
    return pathStore
}

// test node:
const tree = new Node(1, new Node(2), new Node(3, new Node(4), new Node(5)))
// my test node
/*
      1
     / \
    2   3
   / \ / \
  4  5 6  7
 /\   /  / \
8 9  10 11 12
expected: [[1,2,4,8],[1,2,4,9],[1,2,5],[1,3,6,10],[1,3,7,11],[1,3,7,12]]
*/
const myTree = new Node(1, new Node(2, new Node(4, new Node(8), new Node(9)), new Node(5)), new Node(3, new Node(6, new Node(10)), new Node(7, new Node(11), new Node(12))))

console.log(getAllPaths(tree))
console.log(getAllPaths(myTree))