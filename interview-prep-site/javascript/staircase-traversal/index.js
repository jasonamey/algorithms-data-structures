function staircaseTraversal (height, maxSteps) {
  let stepCounts = []
  helper(height, maxSteps, stepCounts)
  return stepCounts.length
}

function helper (height, maxSteps, numOfVariations) {
  if (height - maxSteps < 0) {
    return
  }
  else if (height - maxSteps === 0) {
    numOfVariations.push(1)
  }
  else {
    let arr = []
    for (let i = 1; i <= maxSteps; i++) {
      arr.push(i)
    }
    for (let num of arr) {
      helper(height - num, num, numOfVariations)
    }
  }
}

staircaseTraversal(4, 2)