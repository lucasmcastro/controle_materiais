# -*- coding: utf8 -*-
from __future__ import with_statement

import pickle

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    with open('dados/material.dat','r') as arquivo:
        lista = pickle.load(arquivo)
    return render_template('material/index.html', lista=lista)

@app.route('/cadastro/')
def cadastro():
    return render_template('material/cadastro.html')

@app.route('/novo/', methods=['POST'])
def novo():
    dados = request.form.to_dict()
    with open('dados/material.dat','r') as arquivo:
        lista = pickle.load(arquivo)
    lista.append(dados)

    with open('dados/material.dat','w+') as arquivo:
        pickle.dump(lista,arquivo)

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
