# Importações
from flask import Flask, request, jsonify

# Criação da Instância da Aplicação
app = Flask(__name__)

# Rota para o Webhook


@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        data = request.json
        print(f"Recebi os dados: {data}")
        return jsonify({'status': 'OK'}), 200
    else:
        return jsonify({'status': 'Invalid Method'}), 400


# Execução da Aplicação
if __name__ == '__main__':
    app.run(port=5000, debug=True)
