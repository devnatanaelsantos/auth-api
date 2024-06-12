# Flask Auth API
API de autenticação com Flask, Flask-Login, SQLAlchemy, MySQL, gerenciamento de perfil de usuário e criptografia de senha com bcrypt.

Funcionalidades:
- Cadastrar usuário com criptografia de senha. 
- Realizar login e logout.
- Buscar todos usuários cadastrados. 
- Atualizar senha. 
- Deletar usuários.

 ## Tecnologias Utilizadas
- Flask
- Flask-Login
- bcrypt
- SQLAlchemy
- MySQL

 ## Executando a aplicação
1. Certifique-se de ter o Python e o Docker instalados.

2. Clone este repositório:
````bash
git clone https://github.com/devnatanaelsantos/flask-auth-api.git
````

3. Instale as dependências:
````bash
pip install -r requirements.txt
````

4. Antes de iniciar o contêiner altere o caminho antes de `:/var/lib/mysql` no arquivo docker-compose.yml para uma pasta local.

5. Inicie o contêiner Docker:
````bash
docker-compose up -d
````

6. Utilize a extensão MySQL do VS Code ou outro cliente MySQL para conectar-se ao banco de dados.

7. No terminal, execute os comandos abaixo para criar as tabelas do banco de dados:
````bash
flask shell
db.create_all()
db.session.commit()
exit()
````

8. Inicie a aplicação:
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
    "username": "User",
    "password": "123"
}
````
Retorno esperado:
````json
{
    "message": "Usuário cadastrado com sucesso"
}
````
### Login

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

**Oberservação:** Apenas usuários com o perfil de ``admin`` têm permissão para consultar todos usuários cadastrados, atualizar senhas e excluir cadastros de outros usuários. Para modificar o perfil de um usuário, acesse o registro correspondente no banco de dados e altere o valor do campo ``role``, que por padrão está definido como ``user``, para ``admin``.

### Buscar todos usuários cadastrados

Método: GET

URL: http://127.0.0.1:5000/user/{id}

Retorno esperado:
````json
{
    "username": "User"
}
````
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
    "message": "Usuário 2 deletado com sucesso"
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



