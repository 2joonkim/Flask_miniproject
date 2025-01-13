from flask import Flask, request, jsonify
from app.models import User
from app import db

app = Flask(__name__)

# 유저 생성 API
@app.route('/create_user', methods=['POST'])
def create_user():
    # 요청에서 JSON 데이터를 받음
    data = request.get_json()
    
    # JSON 데이터에서 유저의 정보 추출
    name = data.get('name')  # 이름
    age = data.get('age')    # 나이
    gender = data.get('gender')  # 성별
    email = data.get('email')  # 이메일
    
    # 새로운 유저 객체 생성
    new_user = User(
        name=name,
        age=age,
        gender=gender,
        email=email
    )
    
    # 유저를 데이터베이스 세션에 추가
    db.session.add(new_user)
    # 데이터베이스에 변경 사항 커밋
    db.session.commit()
    
    # 유저 생성 완료 메시지 반환
    return jsonify({'message': '유저 생성이 완료되었습니다.'}), 201


# 유저 조회 API
@app.route('/get_user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    # URL 경로에서 전달된 user_id를 이용해 유저를 데이터베이스에서 조회
    user = User.query.get(user_id)
    
    # 유저가 존재하지 않으면 404 오류를 반환
    if user is None:
        return jsonify({'error': '유저를 찾을 수 없습니다.'}), 404
    
    # 유저 정보가 존재하면 JSON 형태로 반환
    return jsonify({
        'id': user.id,      # 유저의 ID
        'name': user.name,  # 유저의 이름
        'age': user.age,    # 유저의 나이
        'gender': user.gender,  # 유저의 성별
        'email': user.email  # 유저의 이메일
    }), 200