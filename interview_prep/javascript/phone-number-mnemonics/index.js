function phoneNumberMnemonics (phoneNumber) {
  let starter = Array(phoneNumber.length).fill('0')
  let final = []
  helper(0, phoneNumber, starter, final)
  return final
}

function helper (idx, phoneNumber, currentMnemonic, mnemonics) {
  if (idx === phoneNumber.length) {
    mnemonics.push(currentMnemonic.join(''))
  } else {
    let nextDigit = phoneNumber[idx]
    for (let letter of DIGIT_LETTERS[nextDigit]) {
      currentMnemonic[idx] = letter
      helper(idx + 1, phoneNumber, currentMnemonic, mnemonics)
    }
  }
}

const DIGIT_LETTERS = {
  0: ['0'],
  1: ['1'],
  2: ['a', 'b', 'c'],
  3: ['d', 'e', 'f'],
  4: ['g', 'h', 'i'],
  5: ['j', 'k', 'l'],
  6: ['m', 'n', 'o'],
  7: ['p', 'q', 'r', 's'],
  8: ['t', 'u', 'v'],
  9: ['w', 'x', 'y', 'z']

}