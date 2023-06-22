function minimumPassesOfMatrix (matrix) {
  const m = matrix
  let count = 0;
  let stack = []
  const yLen = m.length
  const xLen = m[0].length
  for (let i = 0; i < yLen; i++) {
    for (let j = 0; j < xLen; j++) {
      if (m[i][j] > 0) {
        stack.push([i, j])
      }
    }
  }
  while (stack.length > 0) {
    const pointsStack = [...stack]
    stack = []
    while (pointsStack.length > 0) {
      const point = pointsStack.shift()
      const y = point[0]
      const x = point[1]
      checkForNegativeNumbers(y, x, stack, m, m.length, m[0].length)
    }
    if (stack.length > 0) {
      count++;
    }
  }
  const allPositive = checkIfAllPositive(m)
  return allPositive ? count : -1
}

function checkForNegativeNumbers (y, x, st, m, yLen, xLen,) {
  if (y > 0 && m[y - 1][x] < 0) {
    m[y - 1][x] *= -1
    st.push([y - 1, x])
  }

  if ((y < yLen - 1) && m[y + 1][x] < 0) {
    m[y + 1][x] *= -1
    st.push([y + 1, x])
  }
  if (x > 0 && m[y][x - 1] < 0) {
    m[y][x - 1] *= -1
    st.push([y, x - 1])
  }
  if ((x < xLen - 1) && m[y][x + 1] < 0) {
    m[y][x + 1] *= -1
    st.push([y, x + 1])
  }
}

const m = [
  [0, -1, -3, 2, 0],
  [1, -2, -5, -1, -3],
  [3, 0, 0, -4, -1]
]

function checkIfAllPositive (m) {
  for (let i = 0; i < m.length; i++) {
    for (let j = 0; j < m[0].length; j++) {
      if (m[i][j] < 0) {
        return false;
      }
    }
  }
  return true;
}

function printMatrix (m) {
  for (let arr of m) {
    console.log(arr)
  }
  console.log("------")
}

minimumPassesOfMatrix(m)