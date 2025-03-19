use ecommerce;

-- Inserindo registros na tabela client
INSERT INTO client (Fname, Minit, Lname, CPF, Address) VALUES ('Larissa', 'C.', 'Ramos', '11111111111', 'SP');
INSERT INTO client (Fname, Minit, Lname, CPF, Address) VALUES ('Georffren', 'N.', 'Xavier','21456789960', 'RJ');
INSERT INTO client (Fname, Minit, Lname, CPF, Address) VALUES ('Alan', 'F.', 'Ferreira', '67258963205', 'MS');

-- Inserindo registros na tabela supplier
INSERT INTO supplier (SocialName, CNPJ, Contact) VALUES ('Nihontech', '123654985632569', '119849849');
INSERT INTO supplier (SocialName, CNPJ, Contact) VALUES ('Techbyte', '123321123321122', '21988787878');

-- Inserindo registros na tabela product
INSERT INTO product (Pname, classification_kids, category, size, score) VALUES ('Fraldas', '1', 'Vestimenta', 'P', '5');
INSERT INTO product (Pname, classification_kids, category, size, score) VALUES ('Monitor', '0', 'Eletrônico', '19', '4');
INSERT INTO product (Pname, classification_kids, category, size, score) VALUES ('Sofá', '0', 'Móveis', '3LUG', '3');
INSERT INTO product (Pname, classification_kids, category, size, score) VALUES ('Arroz', '0', 'Alimentos', '1 Saco', '4');

-- Inserindo registros na tabela productSupplier
INSERT INTO productSupplier (idPsSupplier, idPsProduct, quantity) VALUES ('1', '1', '100');
INSERT INTO productSupplier (idPsSupplier, idPsProduct, quantity) VALUES ('2', '2', '50');
INSERT INTO productSupplier (idPsSupplier, idPsProduct, quantity) VALUES ('1', '3', '200');
INSERT INTO productSupplier (idPsSupplier, idPsProduct, quantity) VALUES ('1', '4', '2000');

-- Inserindo registros na tabela storage
INSERT INTO storage (storageLocation) VALUES ('Rio de Janeiro - RJ');
INSERT INTO storage (storageLocation) VALUES ('São Paulo - SP');
INSERT INTO storage (storageLocation) VALUES ('Salvador - BA');
INSERT INTO storage (storageLocation) VALUES ('Curitiba - PR');
INSERT INTO storage (storageLocation) VALUES ('Campinas - SP');

-- Inserindo registros na tabela storageLocation
INSERT INTO storageProduct (idSpProduct, idSpStorage, quantity) VALUES ('1','1', '100');
INSERT INTO storageProduct (idSpProduct, idSpStorage, quantity) VALUES ('2','2', '50');
INSERT INTO storageProduct (idSpProduct, idSpStorage, quantity) VALUES ('3','3', '200');
INSERT INTO storageProduct (idSpProduct, idSpStorage, quantity) VALUES ('4','4', '2000');

-- Inserindo registros na tabela seller
INSERT INTO seller (socialName, abstName, CNPJ, CPF, location, contact) VALUES ('Tech eletronics',NULL,'963258741369852',NULL,'Rio de Janeiro','21963258763');
INSERT INTO seller (socialName, abstName, CNPJ, CPF, location, contact) VALUES ('Boticário',NULL,'753159852951753',NULL,'São Paulo','11985265453');
INSERT INTO seller (socialName, abstName, CNPJ, CPF, location, contact) VALUES ('JCNOK',NULL,NULL,'88899966','Mato Grosso','67952654232');
INSERT INTO seller (socialName, abstName, CNPJ, CPF, location, contact) VALUES ('Bar do zé',NULL,NULL,'925875362','São Paulo','11965412548');
INSERT INTO seller (socialName, abstName, CNPJ, CPF, location, contact) VALUES ('Boutique',NULL,'358952789654111',NULL,'Minas Gerais','31963524122');

-- Inserindo registros na tabela Produtos_Terceiros
INSERT INTO productSeller (idPsSeller, idPsProduct, prodQuantity) VALUES ('1', '2', '10');
INSERT INTO productSeller (idPsSeller, idPsProduct, prodQuantity) VALUES ('2', '3', '5');
INSERT INTO productSeller (idPsSeller, idPsProduct, prodQuantity) VALUES ('3', '4', '15');
INSERT INTO productSeller (idPsSeller, idPsProduct, prodQuantity) VALUES ('4', '1', '50');