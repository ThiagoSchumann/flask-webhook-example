from flask import Flask, request, jsonify
import requests
import time
import threading  # Importe a biblioteca threading

app = Flask(__name__)
webhook_urls = []


@app.route('/register', methods=['POST'])
def register():
    data = request.json
    if 'url' in data:
        webhook_urls.append(data['url'])
        return jsonify({'status': 'registered'}), 200
    return jsonify({'status': 'invalid data'}), 400


def notify_webhooks():  # Função separada para notificar webhooks
    time.sleep(5)
    for url in webhook_urls:
        requests.post(url, json={'message': 'Pagamento Confirmado'})


@app.route('/initiate-payment', methods=['POST'])
def initiate_payment():
    data = request.json
    print(
        f"Processando venda para item: {data['item']} pelo valor de: ${data['amount']}")

    # Inicie a função notify_webhooks em uma thread separada
    thread = threading.Thread(target=notify_webhooks)
    thread.start()

    return jsonify({'status': 'Pagamento enviado para processamento'}), 200


if __name__ == '__main__':
    app.run(port=7000, debug=True)
