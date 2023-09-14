from flask import Flask, request, jsonify
import requests
import time

app = Flask(__name__)

# Lista para armazenar URLs registradas pelo e-commerce
webhook_urls = []


@app.route('/register', methods=['POST'])
def register():
    data = request.json
    if 'url' in data:
        webhook_urls.append(data['url'])
        return jsonify({'status': 'registered'}), 200
    return jsonify({'status': 'invalid data'}), 400


@app.route('/initiate-payment', methods=['POST'])
def initiate_payment():
    # Processar venda aqui
    data = request.json
    print(
        f"Processando venda para item: {data['item']} pelo valor de: ${data['amount']}")

    # Simulação: aguardar 5 segundos para processar a venda
    time.sleep(5)

    # Notificar e-commerce sobre a confirmação de pagamento
    for url in webhook_urls:
        requests.post(url, json={'message': 'Pagamento Confirmado'})

    return jsonify({'status': 'Payment Processed'}), 200


if __name__ == '__main__':
    app.run(port=7000, debug=True)
