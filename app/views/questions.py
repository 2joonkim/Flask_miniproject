from flask import Blueprint, jsonify, request
from app.models import Question, Image
from config import db

# Blueprint 생성
questions_bp = Blueprint("questions", __name__, url_prefix="/questions")

# 질문 목록 조회
@questions_bp.route("/get", methods=["GET"])
def get_questions():
    questions = Question.query.all()
    return jsonify([q.to_dict() for q in questions]), 200

# 질문 생성
@questions_bp.route("/", methods=["POST"])
def create_question():
    data = request.get_json()
    title = data.get("title")
    image_id = data.get("image_id")
    sqe = data.get("sqe", 0)

    if not title or not image_id:
        return jsonify({"error": "필수 데이터가 부족합니다."}), 400

    # 이미지 확인
    image = Image.query.get(image_id)
    if not image:
        return jsonify({"error": "유효하지 않은 이미지 ID입니다."}), 400

    new_question = Question(title=title, image_id=image_id, sqe=sqe)
    db.session.add(new_question)
    db.session.commit()

    return jsonify(new_question.to_dict()), 201