let primeiroNum = 20
let segundoNum = 2

//operadores
const soma = primeiroNum + segundoNum
const subtracao = primeiroNum - segundoNum
const multiplicacao = primeiroNum * segundoNum
const divisao = primeiroNum / segundoNum
const exponenciacao = primeiroNum ** segundoNum
const modulo = primeiroNum % segundoNum

console.log('Soma =', soma)
console.log('Subtração =', subtracao)
console.log('Multiplicação =', multiplicacao)
console.log('Divisão =', divisao)
console.log('Exponenciação =', exponenciacao)
console.log('Módulo =', modulo)

//precedência
console.log(3 + 7 * 3) //24
console.log((3 + 7) * 3) //30

//biblioteca nativa Math
console.log(Math.PI)
console.log(Math.sqrt(16))
