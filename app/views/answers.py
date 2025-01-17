from flask import Blueprint, jsonify, request
from app.models import Answer
from config import db

answers_bp = Blueprint("answers", __name__, url_prefix="/submit")

@answers_bp.route("/", methods=["POST"])
def submit_answers():
    # 요청 데이터 가져오기
    data = request.get_json()

    # 데이터 저장 (검증 없이)
    for entry in data:
        db.session.add(Answer(user_id=entry["userId"], choice_id=entry["choiceId"]))

    # 커밋
    db.session.commit()

    # 응답 반환
    return jsonify({"message": "Data successfully saved!"}), 201