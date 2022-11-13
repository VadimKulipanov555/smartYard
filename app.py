from flask import Flask, render_template, request
from models import Base, User
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:kuldim555@localhost:5432/smartYard"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

path = "postgresql://postgres:kuldim555@localhost:5432/smartYard"
engine = create_engine(path, echo=True)
session = Session(bind=engine)
Base.metadata.create_all(engine)


@app.route('/')
def form():  # put application's code here
    return render_template('form.html')


@app.route('/login', methods=['POST', 'GET'])
def login():

    error = {}
    not_error = {}

    if request.method == 'GET':
        return "Login via the login Form"

    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        password = request.form['password']
        email = request.form['email']
        telephone = f"+7{request.form['telephone']}"
        new_user = User(name_user=name, surname_user=surname, password_user=password, email_user=email, telephone_user=telephone)
        # Добавление новых данных
        session.add(new_user)
        # Сохранение изменений
        session.commit()
        return f"Done!!"


if __name__ == '__main__':
    app.run(debug=True)
