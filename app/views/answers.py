from flask import Blueprint, request, jsonify
from app.models import Answer, User, Choices
from config import db

answers_bp = Blueprint("answers", __name__, url_prefix="/submit")

@answers_bp.route("/", methods=["POST"])
def submit_answers():
    data = request.get_json()

    # 데이터 유효성 검사
    if not data:
        return jsonify({"error": "No data provided"}), 400

    try:
        for entry in data:
            # user_id와 choice_id를 확인
            user_id = entry.get("userId")
            choice_id = entry.get("choiceId")

            if not user_id or not choice_id:
                return jsonify({"error": "Missing userId or choiceId in entry"}), 400

            # 유효한 user_id인지 확인
            user = User.query.get(user_id)
            if not user:
                return jsonify({"error": "Invalid userId"}), 400

            # 유효한 choice_id인지 확인
            choice = Choices.query.get(choice_id)
            if not choice:
                return jsonify({"error": "Invalid choiceId"}), 400

            # Answer 모델에 저장
            new_answer = Answer(user_id=user_id, choice_id=choice_id)
            db.session.add(new_answer)

        # 데이터베이스에 저장
        db.session.commit()

        return jsonify({"message": "Data successfully saved!"}), 201

    except Exception as e:
        db.session.rollback()  # 예외 발생 시 롤백
        return jsonify({"error": str(e)}), 500  # 예외 처리