//inicio no índice 0
let arr1 = ['Lari', 20, 1.65, true]
const arr2 = [30, 12, 45, 34, 29, 34]
let arr3 = []

//percorre elementos do array
for (let i = 0; i < arr1.length; i++){
    console.log(arr1[i])
}

console.clear()

//percorre elementos do array
for (let elemento of arr1){
    console.log(elemento)
}

//percorre indice do array
for (let indice in arr1){
    console.log(indice, arr1[indice])
}

console.log(arr1.slice(0, 2))
console.log(arr1.slice(2))
console.log(arr1.slice(2, arr2.length))

//adiciona no final
arr3.push(10, 20, 30)
arr3.push(40)

//adiciona no início
arr3.unshift(0)

//remove no final e retorna o elemento removido
arr3.pop()

//remove no inicio e retorna o elemento removido
arr3.shift()

//concatena arrays
console.log(arr1.concat(arr2))
console.log(arr2.concat(arr1))

//retorna índice do primeiro elemento selecionado no array
console.log(arr1.indexOf(34))
console.log(arr2.indexOf(34))

//retorna índice do último elemento selecionado no array
console.log(arr2.lastIndexOf(34))

//verifica se o valor existe no array
console.log(arr2.includes(12))

//inverte array
console.log(arr1.reverse())