//coerção explícita
const num = 10

console.log(num, typeof num)

const numString = String(num)
console.log(numString, typeof numString)

console.log(Number('123'))
console.log(Boolean('0')) //0 é false
console.log(Boolean('1')) //diferente de 0 é true

//coerção implícita
console.log('10' + 2) //102
console.log('10' - 2) //8
console.log(10 * '2') //20
console.log(10 - 'aeiou') //NAN - Not A Number