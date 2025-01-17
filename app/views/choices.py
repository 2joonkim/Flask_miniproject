from flask import Blueprint, jsonify, request
from app.models import Choices, Question
from config import db

# Blueprint 생성
choices_bp = Blueprint("choices", __name__, url_prefix="/choices")

# 특정 질문의 선택지 목록 조회
@choices_bp.route("/<int:question_id>", methods=["GET"])
def get_choices_by_question(question_id):
    # 해당 질문의 선택지 가져오기
    choices = Choices.query.filter_by(question_id=question_id).all()

    # 질문 유효성 검증
    if not choices:
        question = Question.query.get(question_id)
        if not question:
            return jsonify({"error": "유효하지 않은 질문 ID입니다."}), 404

    # 선택지 리스트 반환
    return jsonify({
        "choices": [
            {
                "id": choice.id,
                "content": choice.content,
                "is_active": choice.is_active
            } for choice in choices
        ]
    }), 200

# 선택지 생성
@choices_bp.route("/", methods=["POST"])
def create_choice():
    data = request.get_json()
    content = data.get("content")
    question_id = data.get("question_id")
    sqe = data.get("sqe", 0)

    if not content or not question_id:
        return jsonify({"error": "필수 데이터가 부족합니다."}), 400

    # 질문 확인
    question = Question.query.get(question_id)
    if not question:
        return jsonify({"error": "유효하지 않은 질문 ID입니다."}), 400

    new_choice = Choices(content=content, question_id=question_id, sqe=sqe)
    db.session.add(new_choice)
    db.session.commit()

    return jsonify(new_choice.to_dict()), 201

# 선택지 삭제
@choices_bp.route("/<int:question_id>", methods=["DELETE"])
def delete_choices_by_question(question_id):
    # 해당 질문 ID의 모든 선택지 삭제
    choices = Choices.query.filter_by(question_id=question_id).all()
    
    if not choices:
        return jsonify({"error": "해당 질문에 선택지가 없습니다."}), 404

    for choice in choices:
        db.session.delete(choice)

    db.session.commit()
    return jsonify({"message": f"질문 ID {question_id}의 모든 선택지가 삭제되었습니다."}), 200
