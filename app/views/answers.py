from flask import Blueprint, jsonify, request
from app.models import Answer, User, Choices
from config import db

# Blueprint 생성
answers_bp = Blueprint("answers", __name__, url_prefix="/answers")

# 응답 목록 조회
@answers_bp.route("/", methods=["GET"])
def get_answers():
    answers = Answer.query.all()
    return jsonify([ans.to_dict() for ans in answers]), 200

# 응답 생성
@answers_bp.route("/", methods=["POST"])
def submit_answer():
    data = request.get_json()
    user_id = data.get("user_id")
    choice_id = data.get("choice_id")

    if not user_id or not choice_id:
        return jsonify({"error": "필수 데이터가 부족합니다."}), 400

    # 사용자와 선택지 확인
    user = User.query.get(user_id)
    choice = Choices.query.get(choice_id)

    if not user:
        return jsonify({"error": "유효하지 않은 사용자 ID입니다."}), 400
    if not choice:
        return jsonify({"error": "유효하지 않은 선택지 ID입니다."}), 400

    new_answer = Answer(user_id=user_id, choice_id=choice_id)
    db.session.add(new_answer)
    db.session.commit()

    return jsonify(new_answer.to_dict()), 201