/*
This problem was asked by Microsoft.

Let's represent an integer in a linked list format by having each node represent a digit in the number. The nodes make up the number in reversed order.

For example, the following linked list:

1 -> 2 -> 3 -> 4 -> 5
is the number 54321.

Given two linked lists in this format, return their sum in the same linked list format.

For example, given

9 -> 9
5 -> 2
return 124 (99 + 25) as:

4 -> 2 -> 1
*/

/*
Inital notes:

1. numbers are organized in 0, 10, 100, etc. place. Can just add them together in those places, recursively carrying remainders from higher place additions

2. can read numbers out to numbers, add, write numbers back to list
*/

class LinkedNode {
  constructor(val, next = null) {
    this.val = val;
    this.next = next;
  }
}

// 1. read list to numbers, add, read number to list

function listToNumber (linkedList) {
  let reversedString = "";
  let currentNode = linkedList;
  while (currentNode) {
    reversedString += currentNode.val;
    currentNode = currentNode.next;
  }
  return parseInt(reversedString.split("").reverse().join(""))
}

function numberToList (num) {
  const reverseList = num.toString().split("").reverse();
  let linkedList;
  let endNode;
  reverseList.forEach(e => {
    const newNode = new LinkedNode(parseInt(e));
    if (linkedList) {
      endNode.next = newNode;
      endNode = endNode.next;
    } else {
      linkedList = newNode;
      endNode = newNode;
    }
  })
  return linkedList
}

function addLists (list1, list2) {
  const sum = listToNumber(list1) + listToNumber(list2);
  return numberToList(sum)
}


function run () {
  const linkedList1 = new LinkedNode(9, new LinkedNode(9))
  const linkedList2 = new LinkedNode(5, new LinkedNode(2))
  const sumList = addLists(linkedList1, linkedList2)
  console.log(sumList)

}

run()