from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

GATEWAY_URL = 'http://127.0.0.1:7000'
REGISTER_URL = f'{GATEWAY_URL}/register'
INITIATE_PAYMENT_URL = f'{GATEWAY_URL}/initiate-payment'

webhook_url = 'http://127.0.0.1:6000/payment-status'


@app.route('/payment-status', methods=['POST'])
def payment_status():
    data = request.json
    print(f"Recebido do Gateway de Pagamento: {data['message']}")
    return jsonify({'status': 'Received'}), 200


@app.route('/start-payment', methods=['GET'])
def start_payment():
    initiate_payment()
    return "Iniciando pagamento...", 200


def register_webhook():
    response = requests.post(REGISTER_URL, json={'url': webhook_url})
    print(response.json())


def initiate_payment():
    sale_details = {
        'item': 'Livro Python',
        'amount': 50.00
    }
    response = requests.post(INITIATE_PAYMENT_URL, json=sale_details)
    print(response.json())


if __name__ == '__main__':
    # O registro do webhook é feito apenas uma vez quando o sistema é inicializado
    register_webhook()
    app.run(port=6000, debug=True)
