use escola_cursos;

drop table alunos;

drop table notas;

create table alunos (
	id_aluno int not null auto_increment,
    nome varchar(100) not null,
    data_nascimento date not null,
    endereco varchar(255) not null,
    cidade varchar(100) not  null,
    estado varchar(2) not null,
    cpf varchar(11) not null,
    primary key(id_aluno)
);

create table notas (
	id_nota int auto_increment not null,
    descricao_atividade varchar(20) not null,
    vlr_nota decimal(5, 2) not null,
    primary key (id_nota));

insert into alunos
values(default, "Lucien", "2004-08-05", "Rua dos Sapos", "Natal", "RN", "12312312312");

update alunos
set nome = "Lucien Kauã"
where id_aluno = 1;

update alunos
set data_nascimento = "2004-08-02"
where id_aluno = 1;

delete from alunos
where id_aluno = 1;

alter table notas
drop column id_alunos_cursos;
