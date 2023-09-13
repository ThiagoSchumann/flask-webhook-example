## Flask Webhook Example

Este repositório fornece uma demonstração simples de como implementar e usar webhooks usando Python e Flask. Ele foi criado para fins educacionais e demonstrativos.

### Pré-requisitos

- Python 3.x
- Pip (gerenciador de pacotes do Python)

### Como Clonar e Rodar o Projeto

1. Clone o repositório:
   ```
   git clone https://github.com/ThiagoSchumann/flask-webhook-example.git
   ```

2. Navegue até o diretório do projeto:
   ```
   cd flask-webhook-example
   ```

3. (Opcional) Crie um ambiente virtual:
   ```
   python3 -m venv myenv
   source myenv/bin/activate  # No Windows use: myenv\Scripts\activate
   ```

4. Instale as dependências:
   ```
   pip install Flask requests
   ```

5. Rode o servidor (Receptor do Webhook):
   ```
   python webhook_server.py
   ```

6. Em um novo terminal ou janela, rode o cliente (Emissor do Webhook):
   ```
   python webhook_client.py
   ```

7. Observe a saída no terminal do servidor para ver os dados enviados pelo cliente.

### Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
