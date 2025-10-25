"""
Avaliação – Python + SQLite
Tema: CRUD em 'alunos'

O que o script deve fazer:
1) Criar 'escola.db'
2) Criar tabela 'alunos' -> Seguindo o diagrama
3) Inserir registros na tabela alunos
4) Listar todos
5) Buscar por id
6) Atualizar registros
7) Deletar registros

"""

import sqlite3

# passo 1 conetc/create the DB
conn = sqlite3.connect('escola.db') 
cursor = conn.cursor()

# passo 2 - criar tabela
cursor.execute('''CREATE TABLE IF NOT EXISTS alunos(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               idade INTEGER,
               email TEXT
               )''')
print('TABELA CRIADA COM SUCESSO')

# PASSO 3 inserir dados
# cursor.execute('INSERT INTO alunos(nome,idade,email) VALUES(?,?,?)',
#                ('Thiago',17,'thiagoviannavitalsilva@gmail.com'))
# cursor.execute('INSERT INTO alunos(nome,idade,email) VALUES(?,?,?)',
#                ('Mario',18,'mariogameshehehehaa@gmail.com'))
# cursor.execute('INSERT INTO alunos(nome,idade,email) VALUES(?,?,?)',
#                ('Nicolly',17,'lyly_sufocado@gmail.com'))
# cursor.execute('INSERT INTO alunos(nome,idade,email) VALUES(?,?,?)',
#                ('Pedro',30,'rolabola123@gmail.com'))

conn.commit()
print('FEITO :)')

# passo 4 -listar todos
print('Lista de alunos cadastrados')
cursor.execute('SELECT * FROM alunos')

for linha in cursor.fetchall():
    print(linha)
print()

# PASSO 5 atualizar um registro

cursor.execute('UPDATE alunos SET email = ? WHERE id = ?',('lyly_sufocadora@gmail.com',3))
conn.commit()

print('atualizacao 1')
cursor.execute('SELECT * FROM alunos')
for linha in cursor.fetchall():
    print(linha)
print()

# PASSO 6 deletar um registro

cursor.execute('DELETE FROM alunos WHERE id = ? ', (4,))
conn.commit()

print('depois do DELETE ')
cursor.execute('SELECT * FROM alunos')
for linha in cursor.fetchall():
    print(linha)
print()

# fechar a conn
conn.close()
