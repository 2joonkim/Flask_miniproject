from flask_smorest import Blueprint  # smorest의 Blueprint 사용
from app import db
from app.models import User
from flask import request, jsonify

# Blueprint 생성 (smorest의 Blueprint 사용)
users_bp = Blueprint('users', __name__, url_prefix='/users')

# 유저 생성 API
@users_bp.route('/create_user', methods=['POST'])
def create_user():
    data = request.get_json()
    
    name = data.get('name')
    age = data.get('age')
    gender = data.get('gender')
    email = data.get('email')
    
    new_user = User(
        name=name,
        age=age,
        gender=gender,
        email=email
    )
    
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message': '유저 생성이 완료되었습니다.'}), 201

# 유저 조회 API
@users_bp.route('/get_user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    
    if user is None:
        return jsonify({'error': '유저를 찾을 수 없습니다.'}), 404
    
    return jsonify({
        'id': user.id,
        'name': user.name,
        'age': user.age,
        'gender': user.gender,
        'email': user.email
    }), 200
