from flask_smorest import Blueprint  # smorest의 Blueprint 사용
from app import db
from app.models import Question, Image
from flask import request, jsonify

# Blueprint 생성 (smorest Blueprint 사용)
questions_bp = Blueprint('questions', __name__, url_prefix='/questions')

@questions_bp.route("/questions/<int:question_id>", methods=["GET"])
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

@questions_bp.route("/questions", methods=["POST"])
def create_new_question():
    data = request.get_json()

    title = data.get("title")
    image_id = data.get("image_id")

    if not title:
        return jsonify({"error": "'title'은 필수 입력 사항입니다."}), 400

    new_question = Question(
        title=title,
        is_active=True,
        sqe=0
    )

    # 이미지가 존재하는지 확인하고 연결
    image = Image.query.get(image_id) if image_id else None
    if image:
        new_question.image_id = image.id

    db.session.add(new_question)
    db.session.commit()

    return jsonify({
        "id": new_question.id,
        "title": new_question.title,
        "image": new_question.image.to_dict() if new_question.image else None
    }), 201
