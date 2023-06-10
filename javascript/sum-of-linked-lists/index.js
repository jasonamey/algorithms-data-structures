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
  let l1 = linkedListOne
  let l2 = linkedListTwo
  let total = 0, carry = 0, digit = 0, digitTotal = 0, exp = 0;
  while (l1 !== null && l2 !== null) {
    console.log(l1.value)
    digitTotal = l1.value + l2.value + carry
    digit = digitTotal % 10
    total += digit * Math.pow(10, exp++)
    carry = digit > 9 ? 1 : 0
    l1 = l1.next
    l2 = l2.next
  }

  if (l1 !== null) {
    while (l1 !== null) {
      digitTotal = l1.value + carry
      digit = digitTotal % 10
      total += digit * Math.pow(10, exp++)
      carry = digit > 9 ? 1 : 0
      l1 = l1.next
    }
  } else {
    while (l2 !== null) {
      digitTotal = l2.value + carry
      digit = digitTotal % 10
      total += digit * Math.pow(10, exp++)
      carry = digit > 9 ? 1 : 0
      l2 = l2.next
    }
  }
  if (carry === 1) {
    total += Math.pow(10, exp)
  }
  console.log(total)
  return linkedListOne;
}


SIZE = 10
// const list1 = new LinkedList(1, null)
let nodes1 = []
let nodes2 = []
for (let i = 1; i < SIZE; i++) {
  nodes1.push(new LinkedList(Math.floor(1 + Math.random() * 9), null))
  nodes2.push(new LinkedList(i, null))
}

for (let i = 0; i < SIZE - 1; i++) {
  nodes1[i].next = nodes1[i + 1]
  nodes2[i].next = nodes2[i + 1]
}

nodes1[0].printList()

// nodes2[0].printList()
// console.log(nodes1[0])
sumOfLinkedLists(nodes1[0], nodes2[0])