# Flask Bible API
An Sacred Bible API made in Flask
This is a work-in-progress app.

#### Pré-requisitos
- Python 3
- Pip
- NodeJS
- Flask

#### Para executar
- python app.py

#### ver os tipos de testamento (devolve: Antigo Testamento e Novo Testamento) e seus respectivos dados

```
http://127.0.0.1:5000/api/testamento/
```

#### ver o tipo de testamento id = 1 (devolve: Antigo Testamento)

```
http://127.0.0.1:5000/api/testamento/1
http://127.0.0.1:5000/api/testamento/?id=1
```

#### ver os livros cadastrados (devolve: Gênesis, Êxodo, ..., Apocalipse) e seus respectivos dados

```
http://127.0.0.1:5000/api/livros
```

#### ver o livro id = 1 (devolve: Gênesis) e seus respectivos dados

```
http://127.0.0.1:5000/api/livros/1
http://127.0.0.1:5000/api/livros/?id=1
```

#### retorna todos os versículos de todos os capítulos do livro id = 1 (Gênesis)

```
http://127.0.0.1:5000/api/livro/1
http://127.0.0.1:5000/api/livro/?id=1
```

#### retorna todos os versículos do capítulo 2 do livro id = 1 (Gênesis)

```
http://127.0.0.1:5000/api/livro/1/2
```

#### retorna o versículo 4 do capítulo 3 do livro id = 1 (Gênesis)

```
http://127.0.0.1:5000/api/livro/1/3/4
```
