function powerset (array) {
  const sets = [[]]
  for (let num of array) {
    let len = sets.length
    for (let i = 0; i < len; i++) {
      let newSet = [...sets[i], num]
      sets.push(newSet)
    }
  }
  return sets;
}
powerset([1, 2, 3])
