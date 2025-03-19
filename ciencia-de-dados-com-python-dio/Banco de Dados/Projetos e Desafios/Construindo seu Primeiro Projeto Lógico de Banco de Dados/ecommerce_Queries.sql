use ecommerce;

-- 1 Quantos pedidos foram feitos por cada cliente?
SELECT CONCAT(c.Fname, ' ', c.Lname) AS Cliente, COUNT(*) AS qtd_pedidos FROM client c
	JOIN order_ p ON c.idClient = p.idOrderClient GROUP BY c.idClient;

-- 2 Algum vendedor também é fornecedor?
select * from supplier su, seller se where su.CNPJ = se.CNPJ;