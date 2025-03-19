//sem parâmetros
function saudacao() {
    console.log('oiii!')
}

saudacao()

//com parâmetros
function saudacaoPersonalizada(nome, curso = 'JavaScript') {
    console.log(`oi, ${nome}!!1! Você está treinando ${curso}!`) 
}

saudacaoPersonalizada('lari')
saudacaoPersonalizada('lari', 'VS Code')

//com retorno

function soma(num1, num2) {
    return num1 + num2
}

console.log(soma(10, 20)/2)