const a = [2, -1, 4, -2, 5, -3, -7]

function sweetAndSavory (dishes, target) {
  dishes.sort((a, b) => a - b)
  let sweetIdx = 0
  let savoryIdx = dishes.length - 1
  let savoryEnd = -1
  let targetDif = Infinity
  for (let i = 0; i < dishes.length; i++) {
    if (dishes[i] > 0) {
      savoryEnd = i
      break
    }
  }
  let bestPairs = []
  if (savoryEnd === 0 || savoryEnd === -1) return [0, 0]
  while (sweetIdx < savoryEnd && savoryIdx >= savoryEnd) {
    let test = dishes[sweetIdx] + dishes[savoryIdx]
    if (test <= target) {
      let testDif = Math.abs(target - test)
      if (testDif === 0) {
        return [dishes[sweetIdx], dishes[savoryIdx]]
      }
      else if (testDif < targetDif) {
        targetDif = testDif
        bestPairs = [dishes[sweetIdx], dishes[savoryIdx]]
      }
      sweetIdx++
    } else {
      savoryIdx--
    }
  }
  return targetDif === Infinity ? [0, 0] : bestPairs
}

