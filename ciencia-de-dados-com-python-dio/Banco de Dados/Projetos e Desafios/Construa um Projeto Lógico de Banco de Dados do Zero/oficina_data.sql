USE oficina;

-- INSERIR DADOS DOS CLIENTES
INSERT INTO Cliente (nome, telefone) VALUES ('Pedro', '1234567890');
INSERT INTO Cliente (nome, telefone) VALUES ('Mateus', '9876543210');

-- INSERIR DADOS DOS CARROS
INSERT INTO Carro (idCliente, modelo, ano) VALUES (1, 'HB20', 1980);
INSERT INTO Carro (idCliente, modelo, ano) VALUES (2, 'Fit', 2020);

-- INSERIR DADOS DOS SERVIÇOS
INSERT INTO Servico (descricao, preco) VALUES ('Troca de óleo', 50.00);
INSERT INTO Servico (descricao, preco) VALUES ('Cambagem', 80.00);