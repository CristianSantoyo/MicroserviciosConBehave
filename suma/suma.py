"""
Created on Mon Apr  6 15:07:08 2020

@author: santoyo-yo Cristan Patiño
"""
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors=CORS(app)

@app.route('/api/suma', methods=['POST'])
def suma():    
    n1 = int(request.args.get('n1'))
    n2 = int(request.args.get('n2'))
    result = sumar(n1,n2)
    return str(result)

def sumar(a, b):
    return a+b


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='3030')