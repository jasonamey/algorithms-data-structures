function getMinIdx (idx, arr) {
  let minIdx = 2 * idx + 1
  if (2 * idx + 2 < arr.length) {
    minIdx = arr[minIdx] < arr[2 * idx + 2] ? minIdx : 2 * idx + 2
  }
  return minIdx
}

function getParentIdx (idx) {

  return Math.floor((idx - 1) / 2)
}

function shiftUp (idx, arr) {
  let curIdx = idx
  let parentIdx = getParentIdx(idx)
  while (parentIdx >= 0 && arr[curIdx] < arr[parentIdx]) {
    swap(curIdx, parentIdx, arr)
    curIdx = parentIdx
    parentIdx = getParentIdx(curIdx)
  }

}

function shiftDown (arr) {
  let curIdx = 0;
  let minIdx = getMinIdx(curIdx, arr)
  while ((curIdx * 2 + 1) < arr.length && (arr[curIdx] > arr[minIdx])) {
    swap(curIdx, minIdx, arr)
    curIdx = minIdx
    minIdx = getMinIdx(curIdx, arr)
  }
}

function swap (i, j, arr) {
  let temp = arr[i]
  arr[i] = arr[j]
  arr[j] = temp
}

let arr = [23, 65, 1, 3, 2, 78, 3, 9, 65]
shiftUp(arr.length - 1, arr)
for (let i = arr.length - 1; i >= 0; i--) {
  shiftUp(i, arr)
  // console.log(arr)
}
swap(0, arr.length - 1, arr)
arr.pop()
shiftDown(arr)
console.log(arr)

