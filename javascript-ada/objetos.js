let pessoa = {
    nome: 'Lari',
    idade: 20
}

pessoa.altura = 1.77
console.log(pessoa)
console.log(pessoa.nome) //ou console.log(pessoa['nome'])

delete pessoa.altura
console.log(pessoa)

//percorrer atributos
for (let chave in pessoa){
    console.log(chave)
}