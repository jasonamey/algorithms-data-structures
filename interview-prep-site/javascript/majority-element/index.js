// [1, 2, 3, 2, 2, 1, 2]

function majorityElement (arr) {
  let foundNum = null
  let count = 0
  for (let num of arr) {
    if (count === 0) foundNum = num
    if (foundNum === num) {
      count++
    } else {
      count--
    }
  }
  return foundNum
}


