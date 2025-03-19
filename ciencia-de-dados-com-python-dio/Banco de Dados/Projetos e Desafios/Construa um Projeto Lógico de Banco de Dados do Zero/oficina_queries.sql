USE oficina;

-- RECUPERAÇÃO DE TODOS OS CARROS DE UM CLIENTE ESPECIFICO
SELECT Carro.modelo, Carro.ano
FROM Carro
WHERE Carro.idCliente = 1;

-- RECUPERACAO DOS SERVICOS REALIZADOS EM UM CARRO COM VALOR TOTAL
SELECT Servico.descricao, Servico.preco
FROM CarroServico
JOIN Servico ON CarroServico.idServico = Servico.idServico
WHERE CarroServico.idCarro = 1; -- Substitua 1 pelo ID do carro desejado

-- CALCULAR O VALOR TOTAL, ADD GROUP BY
SELECT CarroServico.idCarro, SUM(Servico.preco) AS ValorTotal
FROM CarroServico
JOIN Servico ON CarroServico.idServico = Servico.idServico
GROUP BY CarroServico.idCarro;

-- RECUPERACAO DOS CARROS QUE REALIZARAM UM SERVICO ESPECIFICO
SELECT Carro.modelo, Carro.ano
FROM Carro
JOIN CarroServico ON Carro.idCarro = CarroServico.idCarro
WHERE CarroServico.idServico = 1; -- Substitua 1 pelo ID do serviço desejado

-- RECUPERACAO DOS CLIENTES QUE GASTARAM MAIS DE X EM SERVCICOS
SELECT Cliente.nome, SUM(Servico.preco) AS TotalGasto
FROM Cliente
JOIN Carro ON Cliente.idCliente = Carro.idCliente
JOIN CarroServico ON Carro.idCarro = CarroServico.idCarro
JOIN Servico ON CarroServico.idServico = Servico.idServico
GROUP BY Cliente.idCliente
HAVING TotalGasto > 100;