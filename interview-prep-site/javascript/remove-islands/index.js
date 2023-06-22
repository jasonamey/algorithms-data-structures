function removeIslands (matrix) {
  stack = []
  let m = matrix
  let xLen = m[0].length
  let yLen = m.length
  for (let i = 0; i < yLen; i++) {
    if (m[i][0] === 1) {
      stack.push([i, 0])
    }
    if (m[i][xLen - 1] === 1) {
      stack.push([i, xLen - 1])
    }
  }
  for (let i = 1; i < xLen - 1; i++) {
    if (m[0][i] === 1) {
      stack.push([0, i])
    }
    if (m[yLen - 1][i] === 1) {
      stack.push([yLen - 1, i])
    }
  }
  for (let point of stack) {
    let newStack = []
    newStack.push(point)
    while (newStack.length > 0) {
      const checkPoint = newStack.shift()
      const y = checkPoint[0]
      const x = checkPoint[1]
      if (inMiddle(y + 1, x, m) && m[y + 1][x] == 1) {
        m[y + 1][x] = 2
        newStack.push([y + 1, x])
      }
      if (inMiddle(y - 1, x, m) && m[y - 1][x] == 1) {
        m[y - 1][x] = 2
        newStack.push([y - 1, x])
      }
      if (inMiddle(y, x + 1, m) && m[y][x + 1] == 1) {
        m[y][x + 1] = 2
        newStack.push([y, x + 1])
      }
      if (inMiddle(y, x - 1, m) && m[y][x - 1] == 1) {
        m[y][x - 1] = 2
        newStack.push([y, x - 1])
      }
    }

  }
  for (let i = 1; i < m.length - 1; i++) {
    for (let j = 1; j < m[0].length - 1; j++) {
      if (m[i][j] == 2) {
        m[i][j] = 1
      } else {
        m[i][j] = 0
      }
    }
  }
  return m;
}

function inMiddle (y, x, m) {
  let t = (y > 0 && x > 0 && y < m.length - 1 && x < m[0].length - 1)
  return t
}

let m = [
  [1, 1, 1, 1, 1],
  [1, 0, 0, 0, 1],
  [1, 0, 1, 0, 1],
  [1, 0, 0, 0, 1],
  [1, 0, 1, 0, 1],
  [1, 0, 1, 0, 1],
  [1, 0, 1, 1, 1],
  [1, 0, 1, 0, 1]
]

removeIslands(m)
