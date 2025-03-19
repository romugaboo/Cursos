const input = require('readline-sync')

const numSorteado = 5
let num = Number(input.question('Advinhe um numero: '))

while(num !== numSorteado){
    console.log('Você errou, tente novamente!')
    num = Number(input.question('Advinhe um numero: '))
}

console.log('Você acertou, parabéns!')