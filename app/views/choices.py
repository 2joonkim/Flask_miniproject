from flask import Blueprint, jsonify, request
from app.models import Choices, Question
from config import db

choices_bp = Blueprint("choices", __name__, url_prefix="/choices")

# 선택지 목록 조회
@choices_bp.route("/", methods=["GET"])
def get_choices():
    choices = Choices.query.all()
    return jsonify([choice.to_dict() for choice in choices]), 200

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