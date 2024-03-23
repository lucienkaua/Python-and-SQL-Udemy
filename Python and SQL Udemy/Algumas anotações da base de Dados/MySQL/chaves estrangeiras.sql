drop table notas;
drop table alunos_cursos;

# Cardinalidade vários para vários gera uma tabela que herda as duas chaves primárias de cada tabela da relação
# Essas chaves primárias que são recebidas de outra tabela são chamadas de Foreign Keys, ou Chaves estrangeiras
create table alunos_cursos (
	id_aluno_curso int auto_increment not null,
    id_aluno int not null,
    id_curso int not null,
    primary key(id_aluno_curso));
    
#Criação das chaves estrangeiras da tabela alunos_cursos
ALTER TABLE alunos_cursos
ADD INDEX fk_id_aluno_idx (id_aluno ASC) VISIBLE,
ADD INDEX fk_id_curso_idx (id_curso ASC) VISIBLE;
;

ALTER TABLE alunos_cursos
ADD CONSTRAINT fk_id_aluno
  FOREIGN KEY (id_aluno)
  REFERENCES alunos (id_aluno)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT fk_id_curso
  FOREIGN KEY (id_curso)
  REFERENCES cursos (id_curso)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;
  
# Criando a tabela notas
create table notas (
	id_nota int auto_increment not null,
    descricao_atividade varchar(20) not null,
    vlr_nota decimal(5, 2) not null,
    primary key (id_nota));

# Criando chave estrangeira da tabela notas
ALTER TABLE NOTAS
ADD COLUMN id_aluno_curso int not null;

ALTER TABLE notas
ADD INDEX fk_id_aluno_curso_idx (id_aluno_curso ASC) VISIBLE;
;
ALTER TABLE notas
ADD CONSTRAINT fk_id_aluno_curso
  FOREIGN KEY (id_aluno_curso)
  REFERENCES alunos_cursos (id_aluno_curso)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;
