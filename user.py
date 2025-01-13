from flask import Flask, request, jsonify
from app.models import User
from app import db

app = Flask(__name__)

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    new_user = User(
        username=data['username'],
        email=data['email'],
        password=data['password']  
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': '유저 생성이 완료 되었습니다.'}), 201
