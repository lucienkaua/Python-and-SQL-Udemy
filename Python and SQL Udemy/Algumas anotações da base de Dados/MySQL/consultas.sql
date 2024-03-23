# select * from alunos
# Consulta comum
select nome, cidade, id_aluno from alunos
where cidade = "Macau"
	order by nome;

# Ordenado por e decrescente
select nome, cidade, id_aluno from alunos
where estado = "RN"
	order by cidade desc;

# Operadores lógicos
select nome, cidade, id_aluno from alunos
where estado = "RN" and cidade = "Macau"
	order by cidade;

select nome, cidade, id_aluno from alunos
where estado = "RN" or cidade = "Macau"
	order by cidade;

# Operadores relacionais
select * from alunos
where data_nascimento >= "1999-02-11"
	order by id_aluno;

select * from alunos
where nome <> "João"