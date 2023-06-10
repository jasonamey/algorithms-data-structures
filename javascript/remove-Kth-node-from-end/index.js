class LinkedList {
  constructor (value) {
    this.value = value;
    this.next = null;
  }
}

function removeKthNodeFromEnd (head, k) {
  let count = 1
  let front = head
  let back = head
  while (count <= k) {
    back = back.next
    count++
  }
  if (back === null) {
    head.value = head.next.value
    head.next = head.next.next
  } else {
    while (back.next !== null) {
      back = back.next
      front = front.next
    }
    let tmp = front.next
    front.next = front.next.next
    tmp.next = null
  }
}