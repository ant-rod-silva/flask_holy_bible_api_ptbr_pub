# -*- coding: utf-8 -*-
#!flask/bin/python

# pip install flask

"""
Non-existent route or resource: HTTP/1.1 404 Not Found
"""

import flask
from flask import Flask, request, json, Response, abort
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


def get_tb_livro(id):
    livro_tbl = None
    if id == 1:
        livro_tbl = tb_texto_genesis
    return livro_tbl


# http://127.0.0.1:5000/api/testamento/1
@app.route('/api/testamento/<testamento_id>', methods=['GET'])
def api_testamento_id(testamento_id):
    response = None
    json_str = ''
    testamento_id = int(testamento_id)
    if testamento_id <= 0:
        abort(404)
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
        abort(404)
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
        id = str(request.args['id']).replace('/','')
        id = int(id)
        return api_testamento_id(id)
    if not response:
        abort(404)
    return response


# http://127.0.0.1:5000/api/livros/1
@app.route('/api/livros/<livro_id>', methods=['GET'])
def api_livros_id(livro_id):
    response = None
    json_str = ''
    livro_id = int(livro_id)
    if livro_id <= 0:
        abort(404)
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
        abort(404)
    return response


# http://127.0.0.1:5000/api/livros/
# http://127.0.0.1:5000/api/livros/?id=1
@app.route('/api/livros', methods=['GET'], strict_slashes=False)
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
        id = str(request.args['id']).replace('/','')
        id = int(id)
        return api_livros_id(id)
    if not response:
        abort(404)
    return response


# http://127.0.0.1:5000/api/livro/1
@app.route('/api/livro/<int:livro_id>', methods=['GET'], strict_slashes=False)
def api_livro_id(livro_id):
    response = None
    livro_tbl = None
    if livro_id <= 0 or livro_id > 66:
        abort(404)
    livro_tbl = get_tb_livro(livro_id)
    json_str = json.dumps(
        livro_tbl,
        ensure_ascii=False,
        indent=4,
        sort_keys=False
    )
    response = Response(json_str, content_type="application/json; charset=utf-8" )
    return response


# http://127.0.0.1:5000/api/livro/1/1
# http://127.0.0.1:5000/api/livro/1/1/
@app.route('/api/livro/<int:livro_id>/<int:capitulo>', methods=['GET'], strict_slashes=False)
def api_livro_id_capitulo(livro_id,capitulo):
    response = None
    livro_tbl = None
    results = []
    livro_tbl = get_tb_livro(livro_id)
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


# http://127.0.0.1:5000/api/livro/1/2/3
# http://127.0.0.1:5000/api/livro/1/2/3/
@app.route('/api/livro/<int:livro_id>/<int:capitulo>/<int:versiculo>', methods=['GET'], strict_slashes=False)
def api_livro_id_capitulo_versiculo(livro_id,capitulo,versiculo):
    response = None
    livro_tbl = None
    results = []
    livro_tbl = get_tb_livro(livro_id)
    for livro in livro_tbl:
        if livro['capitulo'] == capitulo:
            if livro['versiculo'] == versiculo:
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

