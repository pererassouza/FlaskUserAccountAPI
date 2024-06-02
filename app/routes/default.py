from app import app, db
from app.models import User, Account
from flask import jsonify, request


@app.route('/users', methods=["GET", "POST"])
def get_account():
    if request.method == 'POST':
        response = request.json

        name = response['name']
        email = response['email']
        number_of_followers = response['number_of_followers']
        account_name = response['account_name']

        new_data = User(
            name=name,
            email=email
        )

        db.session.add(new_data)
        db.session.commit()

        new_account = Account(
            number_of_followers=number_of_followers,
            account_name=account_name,
            user_id=new_data.id
        )
        db.session.add(new_account)
        db.session.commit()

        return jsonify({'message': 'Conta criada com sucesso'}), 201

    data = User.query.all()
    return jsonify([{
        'id': usr.id,
        'name': usr.name,
        'email': usr.email,
    } for usr in data])
