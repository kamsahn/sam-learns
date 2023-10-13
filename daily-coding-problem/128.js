/*
The Tower of Hanoi is a puzzle game with three rods and n disks, each a different size.

All the disks start off on the first rod in a stack. They are ordered by size, with the largest disk on the bottom and the smallest one at the top.

The goal of this puzzle is to move all the disks from the first rod to the last rod while following these rules:

You can only move one disk at a time.
A move consists of taking the uppermost disk from one of the stacks and placing it on top of another stack.
You cannot place a larger disk on top of a smaller disk.
Write a function that prints out all the steps necessary to complete the Tower of Hanoi. You should assume that the rods are numbered, with the first rod being 1, the second (auxiliary) rod being 2, and the last (goal) rod being 3.

For example, with n = 3, we can do this in 7 moves:

Move 1 to 3
Move 1 to 2
Move 3 to 2
Move 1 to 3
Move 2 to 1
Move 2 to 3
Move 1 to 3
*/

/*
write class for disk
- size
- move
write class for rod
- disk order
*/

class Rod {
  constructor(num, disks) {
    this._num = num
    this.disks = disks ? disks : []
  }

  get num() {
    return this._num
  }

  get top() {
    return this.disks.length > 0 ? this.disks[0] : new Disk(1000) // arbitrary large disk
  }

  remove() {
    return this.disks.shift()
  }

  add(disk) {
    this.disks.unshift(disk)
  }
}

class Disk {
  constructor(size) {
    this._size = size
  }

  get size() {
    return this._size
  }

  move(startRod, endRod) {
    if (startRod.top === this) {
      if (endRod.top.size > this.size) {
        endRod.add(startRod.remove())
        console.log(`Move ${startRod.num} to ${endRod.num}`)
      }
    }
  }
}

const d1 = new Disk(1)
const d2 = new Disk(2)
const d3 = new Disk(3)

const r1 = new Rod(1, [d1, d2, d3])
const r2 = new Rod(2)
const r3 = new Rod(3)

d1.move(r1, r2)

// solution will look like:
// n=1 (move) 1
// n=2 (move) 1,2,1
// n=3 (move) 1,2,1,3,1,2,1
// n=4 (move) 1,2,1,3,1,2,1,4,1,2,1,3,1,2,1

