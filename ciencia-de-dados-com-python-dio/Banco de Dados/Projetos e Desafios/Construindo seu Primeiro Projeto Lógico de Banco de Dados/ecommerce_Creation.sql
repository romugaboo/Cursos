-- criar banco de dados de e-commerce
create database ecommerce;
use ecommerce;
-- drop database ecommerce;
-- criar tabela cliente

create table client(
	idClient int auto_increment primary key,
    Fname varchar(10),
    Minit char(3),
    Lname varchar(20),
    CPF char(11) not null,
    Address varchar(30),
    constraint unique_cpf_client unique (CPF)
);
desc client;

-- criar tabela produto

create table product(
	idProduct int auto_increment primary key,
    Pname varchar(10),
    classification_kids bool default false,
	category enum('Eletrônico','Vestimenta','Brinquedos','Alimentos','Móveis') not null,
    score float default 0,
    size varchar(10)
);
desc product;

-- criar tabela pagamento

create table payment(
	idPayment int auto_increment,
    idPaymentClient int,
    typePayment enum('Boleto','Débito','Crédito','Pix'),
    limitAvailable float,
    primary key(idPayment, idPaymentClient),
    constraint fk_payment_client foreign key(idPaymentClient) references client(idClient)
);
desc payment;

-- criar tabela pedido

create table order_(
	idOrder int auto_increment primary key,
    idOrderClient int,
    idOrderPayment int,
    orderStatus enum('Cancelado','Confirmado','Em processamento') default 'Em processamento',
    orderDescription varchar(255),
    sendValue float default 10,
    paymentCash bool default false,
    constraint fk_order_client foreign key(idOrderClient) references client(idClient)
		on update cascade,
	constraint fk_order_payment foreign key(idOrderPayment) references payment(idPayment)
);
desc order_;

-- criar tabela estoque

create table storage(
	idStorage int auto_increment primary key,
    storageLocation varchar(255)
);
desc storage;

-- criar tabela fornecedor

create table supplier(
	idSupplier int auto_increment primary key,
    socialName varchar(255) not null,
    CNPJ char(15) not null,
    contact varchar(11) not null,
    constraint unique_supplier_cnpj unique(CNPJ)
);
desc supplier;

-- criar tabela vendedor

create table seller(
	idSeller int auto_increment primary key,
	socialName varchar(255) not null,
    abstName varchar(25),
    CNPJ char(15),
    CPF char(9),
    location varchar(255),
    contact varchar(11) not null,
	constraint unique_seller_cnpj unique(CNPJ),
    constraint unique_seller_cpf unique(CPF)
);
desc seller;

-- criar tabela vendedor de produtos

create table productSeller(
	idPsSeller int,
    idPsProduct int,
    prodQuantity int default 1,
	primary key(idPsSeller, idPsProduct),
    constraint fk_product_seller foreign key (idPsSeller) references seller(idSeller),
	constraint fk_productSeller_product foreign key (idPsProduct) references product(idProduct)
);
desc productSeller;

-- criar tabela pedido de produto

create table productOrder(
	idPoProduct int,
    idPoOrder int,
    poQuantity int default 1,
    poStatus enum('Disponível', 'Sem estoque') default 'Disponível',
	primary key(idPOProduct, idPOOrder),
    constraint fk_productOrder_order foreign key (idPoOrder) references order_(idOrder),
	constraint fk_productOrder_product foreign key (idPoProduct) references product(idProduct)
);
desc productOrder;

-- criar tabela produto do estoque

create table storageProduct(
	idSpProduct int,
    idSpStorage int,
	quantity int default 0,
	primary key(idSpProduct, idSpStorage),
    constraint fk_storageProduct_product foreign key (idSpProduct) references product(idProduct),
	constraint fk_storageProduct_storage foreign key (idSpStorage) references storage(idStorage)
);
desc storageLocation;

-- criar tabela local do estoque

create table productSupplier(
	idPsSupplier int,
    idPsProduct int,
    quantity int not null,
	primary key(idPsSupplier, idPsProduct),
	constraint fk_productSupplier_supplier foreign key (idPsSupplier) references supplier(idSupplier),
    constraint fk_productSupplier_product foreign key (idPsProduct) references product(idProduct)
);
desc productSupplier;