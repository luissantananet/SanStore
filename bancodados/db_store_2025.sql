#criar banco
#ENGINE = InnoDBInnoDB;
create database storedb;
USE storedb;

create table tbllogin(
	idlogin int not null auto_increment,
    nome VARCHAR(100) not null,
    login VARCHAR(50) not null,
    senha VARCHAR(50) not null,
    primary key(idlogin)
);
create table tblmarkup(
	idkup int not null auto_increment,
    df decimal(5,2),
    dv decimal(5,2),
    lp decimal(5,2),
	markup decimal(5,2),
    primary key(idkup)
);
-- --------------------------------------------------------
--  Criando cadastro de Pessoa
-- --------------------------------------------------------
CREATE TABLE tblpessoa (
    idpessoa INT not null AUTO_INCREMENT,
    idpessoatipo INT NOT NULL,
    cep VARCHAR(8) NOT NULL,
    endereco VARCHAR(100) NOT NULL,
    bairro VARCHAR(50) NOT NULL,
    cidade VARCHAR(50) NOT NULL,
    uf VARCHAR(2) NOT NULL,
    telefone VARCHAR(10),
    celular VARCHAR(11),
    email VARCHAR(50),
    PRIMARY KEY (idpessoa, idpessoatipo)
);

CREATE TABLE tblpessoatipo (
    idpessoatipo INT not null AUTO_INCREMENT,
    descricao VARCHAR(20),
	PRIMARY KEY(idpessoatipo)
);

CREATE TABLE tblpessoafisica (
    idpessoafisica INT not null AUTO_INCREMENT,
    cpf VARCHAR(11),
    rg VARCHAR(20),
    nomecompleto VARCHAR(100),
    PRIMARY KEY (idpessoafisica)
);

CREATE TABLE tblpessoajuridica (
    idpessoajuridica INT not null AUTO_INCREMENT,
    cnpj VARCHAR(14),
    incricaoestadual VARCHAR(20),
    razaosocial VARCHAR(100),
    nomefantasia VARCHAR(50),
    PRIMARY KEY(idpessoajuridica)
);#default charset = utf8;
ALTER TABLE tblpessoa ADD CONSTRAINT FK_tblpessoa_ptipo
    FOREIGN KEY (idpessoatipo) REFERENCES tblpessoatipo (idpessoatipo);
ALTER TABLE tblpessoafisica ADD CONSTRAINT FK_tblfisic_pessoa
    FOREIGN KEY (idpessoafisica) REFERENCES tblpessoa (idpessoa);
ALTER TABLE tblpessoajuridica ADD CONSTRAINT FK_tbljurid_pessoa
    FOREIGN KEY (idpessoajuridica) REFERENCES tblpessoa (idpessoa);

-- --------------------------------------------------------
--  Criando cadastro de produto
-- --------------------------------------------------------
create table tblproduto(
	idproduto int not null AUTO_INCREMENT,
    descricao varchar(100) not null,
    idcategoria int not null,
    primary key(idproduto, idcategoria)
);#default charset = uft8;

create TABLE tblcategoria(
	idcategoria int not null AUTO_INCREMENT,
    descricao varchar(50) not null,
    PRIMARY key (idcategoria)
);

create table tblprecoproduto(
	idproduto int not null primary key,
    precocompra decimal(5,2) not null,
    precovenda decimal(5,2) not null
);

ALTER TABLE tblprecoproduto ADD CONSTRAINT FK_tblpreco_prod
    FOREIGN KEY (idproduto) REFERENCES tblproduto (idproduto);
ALTER TABLE tblproduto ADD CONSTRAINT fk_tblproduto_categ
	FOREIGN KEY (idcategoria) REFERENCES tblcategoria(idcategoria);
    
-- --------------------------------------------------------
--  Criando estrutura do estoque
-- --------------------------------------------------------

create table tblestoque(
	idestoque int not null auto_increment,
    quantidade varchar(5),
    primary key(idestoque)
);
ALTER TABLE tblestoque ADD CONSTRAINT FK_tblprod_estoq
	FOREIGN KEY(idestoque) REFERENCES tblproduto(idproduto);

-- --------------------------------------------------------
--  Inserido dados na tabelas
-- --------------------------------------------------------
insert into tblpessoatipo(descricao) values('Fisico');
insert into tblpessoatipo(descricao) values('Juridico');
insert into tbllogin(nome, login, senha) values('Administrador','adm','adm');