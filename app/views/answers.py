from flask import Blueprint, jsonify, request
from app.models import Answer, User, Choices
from config import db

# Blueprint 생성
answers_bp = Blueprint("answers", __name__, url_prefix="/submit")

# 응답 목록 조회
@answers_bp.route("/", methods=["GET"])
def get_answers():
    answers = Answer.query.all()
    # 요구된 형식으로 응답 데이터 변환
    result = [{"userId": ans.user_id, "choiceId": ans.choice_id} for ans in answers]
    return jsonify(result), 200

# 응답 생성
@answers_bp.route("", methods=["POST"])
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

    # 새 응답 생성
    new_answer = Answer(user_id=user_id, choice_id=choice_id)
    db.session.add(new_answer)
    db.session.commit()

    # 요청된 user_id로 메시지 응답
    return jsonify({
        "message": f"User: {user_id}'s answers Success Create"
    }), 201