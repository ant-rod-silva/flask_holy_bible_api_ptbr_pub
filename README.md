# Flask Bible API
An Sacred Bible API made in Flask
This is a work-in-progress app.

#### Pre-requisites
- Python 3
- Pip
- Flask

#### To run this example:

##### Clone the repository:

```
git clone https://github.com/ant-rod-silva/flask_holy_bible_api_ptbr_pub.git
cd flask-crud
```

##### Create and activate a virtual environment:

```
virtualenv env
source env/bin/activate
```

##### Install requirements:

```
pip install -r requirements.txt
```

##### Run the application:

```
python app.py
```

#### HOW TO USE

##### ver os tipos de testamento (devolve: Antigo Testamento e Novo Testamento) e seus respectivos dados

```
http://127.0.0.1:5000/api/testamento/
```

##### ver o tipo de testamento id = 1 (devolve: Antigo Testamento)

```
http://127.0.0.1:5000/api/testamento/1
http://127.0.0.1:5000/api/testamento/?id=1
```

##### ver os livros cadastrados (devolve: Gênesis, Êxodo, ..., Apocalipse) e seus respectivos dados

```
http://127.0.0.1:5000/api/livros
```

##### ver o livro id = 1 (devolve: Gênesis) e seus respectivos dados

```
http://127.0.0.1:5000/api/livros/1
http://127.0.0.1:5000/api/livros/?id=1
```

##### retorna todos os versículos de todos os capítulos do livro id = 1 (Gênesis)

```
http://127.0.0.1:5000/api/livro/1
http://127.0.0.1:5000/api/livro/?id=1
```

##### retorna todos os versículos do capítulo 2 do livro id = 1 (Gênesis)

```
http://127.0.0.1:5000/api/livro/1/2
```

##### retorna o versículo 4 do capítulo 3 do livro id = 1 (Gênesis)

```
http://127.0.0.1:5000/api/livro/1/3/4
```

#### CONTRIBUTING

If you want to contribute to a project and make it better, your help is very welcome. 
Contributing is also a great way to learn more about social coding on Github, new technologies and and their ecosystems and how to make constructive, helpful bug reports, feature requests and the noblest of all contributions: a good, clean pull request.
How to make a clean pull request

- Create a personal fork of the project on Github.
- Clone the fork on your local machine. Your remote repo on Github is called [origin].
- Add the original repository as a remote called [upstream].
- If you created your fork a while ago be sure to pull [upstream] changes into your local repository.
- Create a new branch to work.
- Implement/fix your feature, comment your code.
- Follow the code style of the project, including indentation.
- Write and run tests as needed.
- Push your branch to your fork on Github, the remote origin.
- From your fork open a pull request in the correct branch. Target the project's develop branch if there is one, else go for master!
- Once the pull request is approved and merged, you can pull the changes from upstream to your local repo and delete your extra branch(es).

And last but not least: Always write your commit messages in the present tense. Your commit message should describe what the commit, when applied, does to the code – not what you did to the code.
