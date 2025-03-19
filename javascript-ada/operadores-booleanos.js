//iguais diferentes em js
const num = 10
console.log(num == 10) //true
console.log(num == '10') //true
console.log(num === '10') //false

console.log(num != 10) //false
console.log(num != '10') //false
console.log(num !== '10') //true

console.clear() //limpa console

let idade = 20
let tenhoCNH = false

const possoDirigir = idade >= 18 && tenhoCNH === true

console.log('Posso dirigir?', possoDirigir)

console.log('Posso dirigir rs?', !possoDirigir)