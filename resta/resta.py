
"""
Created on Mon Apr  6 15:07:08 2020

@author: santoyo-yo Cristan Patiño
"""
from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app)

@app.route('/api/resta', methods=['POST'])
def resta():
    n1 = int(request.args.get('n1'))
    n2 = int(request.args.get('n2'))
    result = n1-n2
    
    return str(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='4040')