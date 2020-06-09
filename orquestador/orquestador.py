
"""
Created on Mon Apr  6 15:07:08 2020

@author: santoyo-yo Cristan Patiño
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import json

app = Flask(__name__)
cors = CORS(app)

@app.route('/api/operacion', methods=['POST'])
def operacion():    
    operacion = request.get_json()['operacion']
    n1 = int(request.get_json()['n1'])
    n2 = int(request.get_json()['n2'])
    r = 0
    if(operacion == "suma"):
        url = "http://localhost:3030/api/suma"        
    elif(operacion == "resta"):
        url = "http://localhost:4040/api/resta"        
    elif(operacion == "multiplicacion"):
        url = "http://localhost:5050/api/multiplicacion" 
    elif(operacion == "division"):
        url = "http://localhost:6060/api/division"
    
    data = {'n1': n1, 'n2': n2}           
    r = requests.post(url, params=data)
    return str(r.text)

    

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='2020')