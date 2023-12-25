class LinkedList {
  constructor (value) {
    this.value = value;
    this.next = null;
  }
  printList () {
    let tmp = this
    let str = ""
    while (tmp.next != null) {
      str += tmp.value + " -> "
      tmp = tmp.next
    }
    console.log(str + tmp.value)

  }
}
function sumOfLinkedLists (linkedListOne, linkedListTwo) {
  l1 = linkedListOne
  l2 = linkedListTwo
  total = 0
  digit = 0
  tempTotal = 0
  exp = 0
  carry = 0
  while (l1 !== undefined && l2 !== undefined) {
    tempTotal = l1.value + l2.value + carry
    digit = tempTotal % 10
    if (tempTotal > 9) {
      carry = 1
    } else {
      carry = 0
    }
    total += Math.pow(10, exp++) * digit
    l1 = l1.next
    l2 = l2.next
  }

  node = l1 === undefined ? l2 : l2 === undefined ? undefined : l2
  while (node !== undefined) {
    tempTotal = node.value + carry
    digit = tempTotal % 10
    if (tempTotal > 9) {
      carry = 1
    } else {
      carry = 0
    }
    total += Math.pow(10, exp++) * digit
    node = node.next
  }
  digits = []
  while (total != 0) {
    digits.push(new LinkedList(total % 10, null))
    total = Math.floor(total / 10)
  }
  for (let i = 0; i < digits.length - 1; i++) {
    digits[i].next = digits[i + 1]
  }
  return digits[0];
}


SIZE = 4

let nodes1 = []
let nodes2 = []
for (let i = 1; i < SIZE; i++) {
  // nodes1.push(new LinkedList(Math.floor(Math.random() * 9), null))
  nodes1.push(new LinkedList(i, null))

  nodes2.push(new LinkedList(i, null))
}



for (let i = 0; i < SIZE - 1; i++) {
  nodes1[i].next = nodes1[i + 1]
  nodes2[i].next = nodes2[i + 1]
}

nodes1[0].printList()
nodes2[0].printList()

sumOfLinkedLists(nodes1[0], nodes2[0])