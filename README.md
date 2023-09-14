# Flask Webhook Example

Este repositório fornece uma demonstração simples de como implementar e usar webhooks usando Python e Flask em um cenário de e-commerce e gateway de pagamento. Ele foi criado para fins educacionais e demonstrativos.

## Pré-requisitos

- Python 3.x
- Pip (gerenciador de pacotes do Python)

## Como Clonar e Rodar o Projeto

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/ThiagoSchumann/flask-webhook-example.git
   ```

2. **Navegue até o diretório do projeto**:

   ```bash
   cd flask-webhook-example
   ```

3. **(Opcional) Crie um ambiente virtual**:

   ```bash
   python3 -m venv myenv
   source myenv/bin/activate  # No Windows use: myenv\Scripts\activate
   ```

4. **Instale as dependências**:

   ```bash
   pip install Flask requests
   ```

5. **Rode o gateway de pagamento (processador)**:

   ```bash
   python3 gateway.py # No Windows use python
   ```

6. **Em um novo terminal ou janela, rode o lado do e-commerce (consumidor e registrador)**:

   ```bash
   python3 e-commerce.py # No Windows use python
   ```

7. **Observe a saída no terminal do e-commerce para ver as notificações enviadas pelo gateway de pagamento**.

8. **Inicie uma transação de pagamento** acessando `http://127.0.0.1:6000/start-payment`.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
