-- CRIAÇÃO DE DATABASE
CREATE DATABASE oficina;
USE oficina;

-- CRIAÇÃO DE TABELAS
CREATE TABLE Cliente (
    idCliente INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    telefone VARCHAR(15)
);

CREATE TABLE Carro (
    idCarro INT AUTO_INCREMENT PRIMARY KEY,
    idCliente INT,
    modelo VARCHAR(50),
    ano INT,
    FOREIGN KEY (idCliente) REFERENCES Cliente(idCliente)
);

CREATE TABLE Servico (
    idServico INT AUTO_INCREMENT PRIMARY KEY,
    descricao VARCHAR(200),
    preco DECIMAL(10, 2)
);

CREATE TABLE CarroServico (
    idCarro INT,
    idServico INT,
    PRIMARY KEY (idCarro, idServico),
    FOREIGN KEY (idCarro) REFERENCES Carro(idCarro),
    FOREIGN KEY (idServico) REFERENCES Servico(idServico)
);