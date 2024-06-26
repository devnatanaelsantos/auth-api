from flask import Flask, request, jsonify
from models.user import User
from database import db
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
import bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:admin123@127.0.0.1:3307/data-base"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view= 'login'

db.init_app(app)

@login_manager.user_loader
def load_user(user_id):
     return User.query.get(user_id)

# Recupera e valida as credênciais de acesso do usuário
@app.route('/login/', methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username and password:
        #Busca no banco de dados o primeiro usuário que seja igual a username
        user = User.query.filter_by(username=username).first()

        if current_user.is_authenticated:
             return jsonify({"message": "O usuário já autenticado"})

        if user and bcrypt.checkpw(str.encode(password), str.encode(user.password)):
                # realiza a autenticação do usuário
                login_user(user)
                # valida se o usuário está autênticado
                print(current_user.is_authenticated)
                return jsonify({"message": "Autenticação realizada com sucesso"})

    return jsonify({"message": "Credênciais inválidas"}), 400

@app.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logout realizado com sucesso"})

@app.route('/user', methods=['POST'])
def create_user():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username and password:
        hashed_password = bcrypt.hashpw(str.encode(password), bcrypt.gensalt())
        user = User(username=username, password=hashed_password, role='user')
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": "Usuário cadastrado com sucesso"})
    
    return jsonify({"message": "Dados inválidos"}), 400

@app.route('/users', methods=['GET'])
@login_required
def get_users():

     if current_user.role != 'admin':
          return jsonify ({"message": "Operação não permitida"}), 403

     users = User.query.all()
     users_list = []

     for user in users:
          users_list.append({
               "id": user.id,
               "username": user.username,
               "role": user.role
          })
     
     output = {
          "usuários": users_list,
          "total_usuários": len(users_list)
     }

     return jsonify(output)

@app.route('/user/<int:id_user>', methods=['PUT'])
@login_required
def update_password(id_user):
     data = request.json
     password = data.get("password")
     user = User.query.get(id_user)

     if id_user != current_user.id and current_user.role == "user":
          return jsonify({"message": "Operação não permitida"}), 403

     if user and data.get("password"):
          hashed_password = bcrypt.hashpw(str.encode(password), bcrypt.gensalt())
          user.password = hashed_password
          db.session.commit()

          return jsonify ({"message": f"Usuário {id_user} atualizado com sucesso"})
     
     return jsonify({"message": "Usuário não encontrado"}), 404

@app.route('/user/<int:id_user>', methods=['DELETE'])
@login_required
def delete_user(id_user):
     user = User.query.get(id_user)

     if current_user.role != 'admin':
          return jsonify ({"message": "Operação não permitida"}), 403

     if id_user == current_user.id:
          return jsonify({"message": "Deleção não permitida"}), 403

     if user:
          db.session.delete(user)
          db.session.commit()

          return jsonify ({"message": f"Usuário {id_user} deletado com sucesso"})
     
     return jsonify({"message": "Usuário não encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)
 

