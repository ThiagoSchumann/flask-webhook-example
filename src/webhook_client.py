# Importações
import requests

# Dados a serem enviados
data = {"evento": "pagamento_confirmado", "venda": "123"}

# Envio da requisição
response = requests.post('http://localhost:5000/webhook', json=data)

# Exibição da resposta
print(f"Server response: {response.text}")
