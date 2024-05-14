# Flask Auth API
API de autenticação em Flask com MySQL via Docker, gerênciamento de perfil de usuário e criptografia de senha.

 ## Tecnologias Utilizadas
- Flask
- Flask-Login
- Flask-SQLAlchemy
- MySQL
- Docker
- bcrypt

 ## Como executar a aplicação
1. Certifique-se de ter o Python e o Docker instalados corretamente em sua máquina.

2. Clone este repositório:
````bash
git clone https://github.com/devnatanaelsantos/flask-auth-api.git
````

3. Instale as dependências:
````bash
pip install -r requirements.txt
````

5. Antes de iniciar o contêiner altere o caminho antes de `:/var/lib/mysql` no arquivo docker-compose.yml para uma pasta local.

4. Inicie o contêiner Docker
````bash
    docker-compose up -d
````

5. Utilize a extensão MySQL do VS Code ou outro cliente MySQL para conectar-se ao banco de dados.

6. No terminal, execute os comandos abaixo para criar as tabelas do banco de dados.
````bash
    flask shell
    db.create_all()
    db.session.commit()
    exit()
````

7. Inicie a aplicação:
````bash
    python app.py
````

## Endpoints
### Criar usuário
Método: POST

URL: http://127.0.0.1:5000/user

Corpo da Requisição (JSON):

````json
{
    "username": "Natanael",
    "password": "123"
}
````
Retorno esperado:
````json
{
    "message": "Usuário cadastrado com sucesso"
}
````
### Autenticar usuário

Método: POST

URL: http://127.0.0.1:5000/login

Corpo da Requisição (JSON):

````json
{
    "username": "User",
    "password": "123"
}
````
Retorno esperado:
````json
{
    "message": "Autenticação realizada com sucesso"
}
````

### Buscar usuário por ID

Método: GET

URL: http://127.0.0.1:5000/user/{id}

Retorno esperado:
````json
{
    "username": "Natanael"
}
````

Oberservação: Somente usuário com perfil admin podem atualizar a senha e deletar outros usuários, para alterar o perfil de um usuário acesse o registro do usuário no banco de dados e altere o valor do campo 'role' para admin'.

### Atualizar senha

Método: PUT

URL: http://127.0.0.1:5000/user/{id}

Corpo da Requisição (JSON):

````json
{
    "password": "456"
}
````
Retorno esperado:
````json
{
    "message": "Usuário 1 atualizado com sucesso"
}
````
### Deletar usuário

Método: DELETE

URL: http://127.0.0.1:5000/user/{id}

Retorno esperado:
````json
{
    "message": "Usuário 9 deletado com sucesso"
}
````
### Logout
Método: GET

URL: http://127.0.0.1:5000/logout

Retorno esperado:
````json
{
    "message": "Logout realizado com sucesso"
}
````



