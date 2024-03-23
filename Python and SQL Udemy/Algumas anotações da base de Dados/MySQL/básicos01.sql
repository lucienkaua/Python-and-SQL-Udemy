# Exclusão de tabelas ------------------------------------------------------------------------------------------------
drop schema udemy;
drop schema escola_cursos;

# Criação de tabelas --------------------------------------------------------------------------------------------------
create schema escola_cursos;

# Criação de tabelas -------------------------------------------------------------------------------------------------
use escola_cursos;
create table alunos(
	id_aluno int not null auto_increment,
	primary key (id_aluno));

create table cursos(
	id_curso int not null auto_increment,
	primary key (id_curso));
    
create table notas(
	id_nota int not null auto_increment,
	primary key (id_nota));

# Alteração de tabelas -----------------------------------------------------------------------------------------------
alter table alunos
	add column nome varchar(100) not null after id_aluno,
	add column data_nascimento date not null after nome,
	add column endereco varchar(255) not null after data_nascimento,
    add column cidade varchar(25) not null after endereco,
	add column estado varchar(2) not null after cidade,
    add column cpf varchar(11) not null after estado;

alter table cursos
	add column nome varchar(100) not null after id_curso;

alter table notas
	 add column descricao_atividade varchar(100) not null after id_nota,
     add column vlr_nota decimal(5, 2) not null after descricao_atividade; # 5 = digitos, 2 = casas decimais
