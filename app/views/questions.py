from flask_smorest import Blueprint  # smorest의 Blueprint 사용
from app import db
from app.models import Question, Image, Choices
from flask import request, jsonify

# Blueprint 생성 (smorest Blueprint 사용)
questions_bp = Blueprint('questions', __name__, url_prefix='/questions')

@questions_bp.route("/<int:question_id>", methods=["GET"])
def get_question_by_id(question_id):
    question = Question.query.get(question_id)

    if not question:
        return jsonify({"error": "질문을 찾을 수 없습니다."}), 404

    return jsonify({
        "id": question.id,
        "title": question.title,
        "is_active": question.is_active,
        "sqe": question.sqe
    }), 200

@questions_bp.route("/create_new_question", methods=["POST"])
def create_new_question():
    data = request.get_json()

    title = data.get("title")
    image_id = data.get("image_id")
    choices_data = data.get("choices", [])  # 선택지 데이터를 받아옴 (선택지 없으면 빈 배열)

    if not title:
        return jsonify({"error": "'title'은 필수 입력 사항입니다."}), 400

    # 새 질문 생성
    new_question = Question(
        title=title,
        is_active=True,
        sqe=0
    )

    # 이미지가 존재하는지 확인하고 연결
    image = Image.query.get(image_id) if image_id else None
    if image:
        new_question.image_id = image.id

    # 데이터베이스에 새 질문 추가
    db.session.add(new_question)

    # 선택지 추가
    for choice_data in choices_data:
        choice = Choices(
            content=choice_data.get('content'),
            sqe=choice_data.get('sqe', 0),  # 선택지 순서 기본값은 0
            question_id=new_question.id
        )
        db.session.add(choice)

    # 데이터베이스에 질문과 선택지 모두 커밋
    db.session.commit()

    # 새로운 질문과 선택지를 반환
    return jsonify({
        "id": new_question.id,
        "title": new_question.title,
        "image": new_question.image.to_dict() if new_question.image else None,
        "choices": [choice.to_dict() for choice in new_question.choices]  # 새로 추가된 선택지 반환
    }), 201
