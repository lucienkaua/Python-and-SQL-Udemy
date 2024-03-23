# Joins - alimentando a base de dados ---------------------------------------------------------------------------------------------------------------------------------

# Adicionando valores na tabela pai - alunos
insert into alunos
values
(default, "Lucien Kauã", "2004-08-05", "Rua Caicó", "Macau", "RN", "12312312312"),
(default, "Raynara Silva", "2003-06-05", "Rua das Margaridas", "Serra do Mel", "RN", "12312312311"),
(default, "Jefferson Costa", "2005-11-21", "Rua dos Canindés", "Natal", "RN", "12382312311"),
(default, "Ulisses Danyel", "2031-09-27", "Machado De Assis", "Santremoz", "PB", "12382372311"),
(default, "José Alfredo", "1995-05-12", "João Tancredo", "São José Mipibú", "RN", "12382372444"),
(default, "Luana Félix", "2005-05-12", "Felipe Amorim", "Guamaré", "RN", "19982372414");

select * from alunos;

# Adicionando valores na tabela pai - Cursos
insert into cursos
values
(default, "Codeigniter"),
(default, "Python"),
(default, "MySQL");

select * from cursos;

# Adicionando valores na tabela filho - alunos_cursos
insert into alunos_cursos
values
(default, 1, 1),
(default, 1, 2),
(default, 2, 1),
(default, 2, 3),
(default, 3, 1),
(default, 3, 2),
(default, 4, 1),
(default, 5, 1);

insert into alunos_cursos
values
(default, 1, 3);

select * from alunos_cursos;

# Inserindo valores na tabela pai - notas
insert into notas
values
(default, 1, "Prova 1", 28.0),
(default, 3, "Prova 1", 25.0),
(default, 5,  "Prova 1", 28.0),
(default, 2,  "Exercicio 1", 10.0),
(default, 6,  "Exercicio 1", 12.0),
(default, 1,  "Prova 2", 22.0),
(default, 2,  "Prova 2", 20.0);

insert into notas
values
(default, 4, "Prova 1", 10.0);

insert into notas
values
(default, 1, "Prova 1", 40.0),
(default, 1, "Prova 2", 40.0),
(default, 1, "Exercicio 1", 20.0);

select * from notas;

# Iniciando os joins -------------------------------------------------------------------------------------------------------------------------------------------

use escola_cursos;

SELECT * FROM alunos_cursos;
SELECT * FROM cursos;

# Mostra o Nome e ID do Curso
SELECT A.nome, AC.id_curso
FROM alunos A, alunos_cursos AC
WHERE A.id_aluno = AC.id_aluno;

# Mostra o nome e curso (esse eu consegui fazer sozinho!!!)
SELECT A.nome, C.nome
FROM alunos A, cursos C, alunos_cursos AC
WHERE A.id_aluno = C.id_curso and C.id_curso = AC.id_curso;

SELECT A.nome, C.nome, N.vlr_nota
FROM alunos A, cursos C, alunos_cursos AC, notas N
WHERE A.id_aluno = C.id_curso and C.id_curso = AC.id_curso and N.id_nota = AC.id_aluno;

# Outra maneira de fazer o join, aqui dá pra entender as ligações de uma maneira melhor...
SELECT A.nome AS "Nome do aluno", C.nome AS "Nome do curso", N.vlr_nota AS "Valor da nota"
FROM alunos A
INNER JOIN alunos_cursos AC ON A.id_aluno = AC.id_aluno
INNER JOIN cursos C ON AC.id_curso = C.id_curso
INNER JOIN notas N ON AC.id_aluno = N.id_aluno_curso
ORDER BY A.nome;

Select * from alunos_cursos;
Select * from notas;
Select * from cursos;