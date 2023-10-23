/*
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
Assume that each node in the tree also has a pointer to its parent.

According to the definition of LCA on Wikipedia:
“The lowest common ancestor is defined between two nodes v and w as the lowest node in T
that has both v and w as descendants (where we allow a node to be a descendant of itself).”
*/

// low being furthest from the root
// define a node class with a parent pointer
// write method to descend the tree while saving all ancestors with level
// find matching ancestors and choose highest level

class Node {
    constructor(value, left = null, right = null, parent = null) {
        this.value = value
        this.left = left
        this.right = right
        this.parent = parent
    }
    
    setParent(parent) {
        this.parent = parent
    }

    setChildren(left = null, right = null) {
        if (left) {
            this.left = left
            left.setParent(this)
        }
        if (right) {
            this.right = right
            right.setParent(this)
        }
    }
}

function getAncestors(node) {
    const storage = []
    function getAncestorsHelper(node) {
        storage.push(node)
        if (node.parent) {
            getAncestorsHelper(node.parent)
        }
    }
    getAncestorsHelper(node)
    return storage
}

function getLikeAncestors(ancestors1, ancestors2) {
    const similarValues = []
    ancestors1.forEach(node1 => {
        ancestors2.forEach(node2 => {
            if (node1 === node2) {
                similarValues.push(node1)
            }
        })
    })
    return similarValues
}

function getLCA(ancestors) {
    return ancestors.shift().value
}

function main(v, w) {
    const vAncestors = getAncestors(v)
    const wAncestors = getAncestors(w)
    const similarAncestors = getLikeAncestors(vAncestors, wAncestors)
    return getLCA(similarAncestors)
}

// Testing
// node creation
const node0 = new Node(0)
const node1 = new Node(1)
const node2 = new Node(2)
const node3 = new Node(3)
const node4 = new Node(4)
const node5 = new Node(5)
const node6 = new Node(6)
const node7 = new Node(7)
const node8 = new Node(8)
// node association
node0.setChildren(node1, node4)
node1.setChildren(node2, node3)
node4.setChildren(node5)
node5.setChildren(node6, node7)
node7.setChildren(node8)

console.log(main(node2, node3))
console.log(main(node5, node6))
console.log(main(node7, node8))
console.log(main(node2, node6))

