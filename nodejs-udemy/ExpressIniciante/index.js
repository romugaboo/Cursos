const express = require("express"); // Importando o express
const app = express(); // Iniciando o express

app.get("/", function (req, res) {
    res.send("<h1>Bem vinde meu primeiro site com express</h1>");
});

app.get("/blog/:artigo?", function (req, res) {

    var artigo = req.params.artigo;

    if (artigo) {
        res.send("<h2>Artigo: " + artigo + " </h2>");
    } else {
        res.send("<h3>Bem vindo ao meu blog!</h3>");
    }
})

app.get("/canal/youtube", function (req, res) {
    var canal = req.query["canal"];

    if (canal) {
        res.send(canal);
    } else {
        res.send("Nenhum canal fornecido!");
    }
})

app.get("/ola/:nome/:empresa", function (req, res) {
    // REQ => DADOS ENVIADOS PELO USUÁRIO
    // RES => RESPOSTA QUE VAI SER ENVIADA PARA O USUÁRIO
    var nome = req.params.nome;
    var empresa = req.params.empresa;
    res.send("<h1>Oi " + nome + " do " + empresa + " </h1>");
});


app.listen(4000, function (erro) {
    if (erro) {
        console.log("Ocorreu um erro!");
    } else {
        console.log("Servidor iniciado com sucesso!");
    }
})

