from flask import Flask, request, jsonify, render_template
import os
import requests
import teste
import time


app = Flask(__name__)

# Defina o caminho para salvar os arquivos PDF
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/upload', methods=['POST'])
def upload_pdf():
    if 'pdf' not in request.files:
        return jsonify({'message': 'Nenhum arquivo PDF encontrado.'}), 400

    file = request.files['pdf']

    if file.filename == '':
        return jsonify({'message': 'Nenhum arquivo selecionado.'}), 400

    if file and file.filename.endswith('.pdf'):
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        
        
        teste.S3envio(filepath, 'A01/VagasTI/', file.filename)
        time.sleep(10)
                
        #resultado = requests.get("http://34.237.203.148:5000/run/01")
        #res_json = resultado.json()
        #print(res_json)
        #return 
    

        #return jsonify({'message': f'Arquivo {file.filename} enviado com sucesso!'}), 200

        #return render_template('scores.html', scores=res_json['scores'])

        #print(res_json)
        #return jsonify({'message': f'Arquivo {file.filename} enviado com sucesso!'}), 200
    else:
        return jsonify({'message': 'Apenas arquivos PDF são permitidos.'}), 400

if __name__ == '__main__':
    app.run(debug=True,port=5001)
