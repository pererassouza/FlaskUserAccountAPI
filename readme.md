# Flask User Account API

Este é um projeto de uma API para gerenciamento de usuários e contas utilizando Flask e SQLAlchemy.

- **models/**: Contém os modelos de dados (`User` e `Account`) definidos com SQLAlchemy.
- **routes/**: Contém os arquivos que definem as rotas da API (`default.py` neste caso).
- **instance/**: Diretório onde o arquivo do banco de dados SQLite (`taskmanager.db`) é criado.
- **\_\_init\_\_.py**: Inicializa a aplicação Flask e o banco de dados SQLAlchemy.
- **run.py**: Ponto de entrada da aplicação Flask.

## Funcionalidades Implementadas

### 1. Modelos de Dados

#### User

- **id**: Chave primária do usuário.
- **name**: Nome do usuário (máximo de 40 caracteres).
- **email**: E-mail do usuário (máximo de 60 caracteres).
- **accounts**: Relacionamento um para muitos com a tabela `Account`.

#### Account

- **id**: Chave primária da conta.
- **number_of_followers**: Número de seguidores da conta.
- **account_name**: Nome da conta (máximo de 15 caracteres).
- **user_id**: Chave estrangeira que referencia o `id` do usuário na tabela `User`.

### 2. Rotas da API

#### GET `/users`

- **Descrição**: Retorna uma lista de todos os usuários cadastrados.
- **Método HTTP**: GET
- **Resposta**: JSON com lista de usuários, cada um contendo `id`, `name` e `email`.

#### POST `/users`

- **Descrição**: Cria um novo usuário e uma conta associada a esse usuário.
- **Método HTTP**: POST
- **Dados esperados**: JSON contendo `name`, `email`, `number_of_followers` e `account_name`.
- **Resposta**: JSON com mensagem de sucesso e código de status 201.

### 3. Executando a Aplicação

Para executar a aplicação, siga os passos abaixo:

1. **Ambiente Virtual** (recomendado):
   ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate

2. **Dependências** (obrigatório)
    ```bash
        pip install -r requirements.txt

3. **Banco de Dados**
    Crie e reinicialize o Banco de Dados
    ```bash
        flask db upgrade

4. **Executar**
    ```bash
        python run.py

5. **Teste da API**
    Acesse `http://localhost:5000/users` para visualizar todos os usuários.
    Use um cliente HTTP (como Postman ou cURL) para enviar requisições POST para `http://localhost:5000/users` e criar novos usuários.
