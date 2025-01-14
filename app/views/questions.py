from flask import Blueprint, jsonify, request
from app import db
from app.models import db, Question, Image  # 데이터베이스 모델 직접 사용
from flask_restx import Api

# Blueprint 생성
questions_bp = Blueprint("questions", __name__)  # "questions"라는 이름의 블루프린트 생성
api = Api(questions_bp)

@questions_bp.route("/questions/<int:question_id>", methods=["GET"])
def get_question_by_id(question_id):
    # 특정 질문 조회 API
    # 클라이언트가 특정 질문의 ID를 요청하면, 해당 질문 정보를 반환
    # 데이터베이스에서 질문 조회
    question = Question.query.get(question_id)

    if not question:
        return jsonify({"error": "Question not found"}), 404

    # 질문 데이터를 JSON 형태로 반환
    return jsonify({
        "id": question.id,              
        "title": question.title,         
        "is_active": question.is_active,  
        "sqe": question.sqe              
    }), 200

@questions_bp.route("/questions", methods=["POST"])
def create_new_question():
    # 질문 생성 API
    # 클라이언트로부터 데이터를 받아 새로운 질문을 생성합니다.
    # 요청 본문에서 JSON 데이터 가져오기
    data = request.get_json()

    title = data.get("title")
    image_id = data.get("image_id") 

    if not title:
        return jsonify({"error": "The 'title' field is required"}), 400

    new_question = Question(
        title=title,      
        is_active=True,   
        sqe=0            
    )
    
    # 이미지가 존재하는지 확인하고 연결
    image = Image.query.get(image_id) if image_id else None

    new_question = Question(
        title=title,
        is_active=True,
        sqe=0,
        image_id=image.id if image else None  # 이미지가 있으면 연결
    )

    # 데이터베이스 세션에 추가
    db.session.add(new_question)

    # 변경 사항을 데이터베이스에 반영 (커밋)
    db.session.commit()

    # 생성된 질문 데이터를 JSON 형태로 반환
    return jsonify({
        "id": new_question.id, 
        "title": new_question.title,
        "image": new_question.image.to_dict() if new_question.image else None
    }), 201  