# -*- coding: utf-8 -*-
#!flask/bin/python

# pip install flask

import flask
from flask import Flask, request, json, Response
from jsonTestamento import tb_testamento
from jsonLivro import tb_livro
from jsonGenesis import tb_texto_genesis

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def index():
    return '''
       Flask Bible API v. 0.1<br/>
       by Antonio Rodrigo<br/>
       Almeida Corrigida e Fiel<br/>
       Última atualização: 18/09/2018
    '''

# http://127.0.0.1:5000/api/testamento/1
@app.route('/api/testamento/<testamento_id>', methods=['GET'])
def api_testamento_id(testamento_id):
    response = None
    json_str = ''
    testamento_id = int(testamento_id)
    if testamento_id <= 0:
        return "id invalido"
    for testamento in tb_testamento:
        if testamento['id'] == testamento_id:
            json_str = json.dumps(
                testamento,
                ensure_ascii=False,
                indent=4,
                sort_keys=False
            )
            response = Response(json_str, content_type="application/json; charset=utf-8" )
    if not response:
        return "nao encontrado"
    return response

# http://127.0.0.1:5000/api/testamento/
# http://127.0.0.1:5000/api/testamento/?id=1
@app.route('/api/testamento/', methods=['GET'])
def api_testamento():
    response = None
    if not 'id' in request.args:
        json_str = json.dumps(
            tb_testamento,
            ensure_ascii=False,
            indent=4,
            sort_keys=False
        )
        response = Response(json_str, content_type="application/json; charset=utf-8" )
    else:
        id = int(request.args['id'])
        return api_testamento_id(id)
    if not response:
        return "nao encontrado"
    return response

# http://127.0.0.1:5000/api/livros/1
@app.route('/api/livros/<livro_id>', methods=['GET'])
def api_livros_id(livro_id):
    response = None
    json_str = ''
    livro_id = int(livro_id)
    if livro_id <= 0:
        return "id invalido"
    for livro in tb_livro:
        if livro['id'] == livro_id:
            json_str = json.dumps(
                livro,
                ensure_ascii=False,
                indent=4,
                sort_keys=False
            )
            response = Response(json_str, content_type="application/json; charset=utf-8" )
    if not response:
        return "nao encontrado"
    return response

# http://127.0.0.1:5000/api/livros/
# http://127.0.0.1:5000/api/livros/?id=1
@app.route('/api/livros/', methods=['GET'])
def api_livros():
    response = None
    if not 'id' in request.args:
        json_str = json.dumps(
            tb_livro,
            ensure_ascii=False,
            indent=4,
            sort_keys=False
        )
        response = Response(json_str, content_type="application/json; charset=utf-8" )
    else:
        id = int(request.args['id'])
        return api_livros_id(id)
    if not response:
        return "nao encontrado"
    return response

# http://127.0.0.1:5000/api/livro/1
@app.route('/api/livro/<livro_id>', methods=['GET'])
def api_livro_id(livro_id):
    response = None
    livro_tbl = None
    livro_id = int(livro_id)
    if livro_id == 1:
        livro_tbl = tb_texto_genesis
    json_str = json.dumps(
        livro_tbl,
        ensure_ascii=False,
        indent=4,
        sort_keys=False
    )
    response = Response(json_str, content_type="application/json; charset=utf-8" )
    return response

# http://127.0.0.1:5000/api/livro/1/1
@app.route('/api/livro/<livro_id>/<capitulo>', methods=['GET'])
def api_livro_id_capitulo(livro_id,capitulo):
    response = None
    livro_tbl = None
    livro_id = int(livro_id)
    capitulo = int(capitulo)
    results = []
    if livro_id == 1:
        livro_tbl = tb_texto_genesis
    for livro in livro_tbl:
        if livro['capitulo'] == capitulo:
            results.append(livro)

    json_str = json.dumps(
        results,
        ensure_ascii=False,
        indent=4,
        sort_keys=False
    )
    response = Response(json_str, content_type="application/json; charset=utf-8" )
    return response


if __name__ == '__main__':
    app.run(debug=True)

