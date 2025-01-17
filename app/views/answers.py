from flask import Blueprint, jsonify, request
from app.models import Answer
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
            # entry 출력
            print(entry)  # entry를 콘솔에 출력

            # 각 entry에서 'userId'와 'choiceId'가 유효한지 확인
            if not entry.get("userId") or not entry.get("choiceId"):
                return jsonify({"error": "Missing userId or choiceId in entry"}), 400

            # 데이터베이스에 저장
            db.session.add(Answer(user_id=entry["userId"], choice_id=entry["choiceId"]))

        # 커밋
        db.session.commit()

        # 성공 응답 반환
        return jsonify({"message": "Data successfully saved!"}), 201
    except Exception as e:
        db.session.rollback()  # 트랜잭션 롤백
        return jsonify({"error": str(e)}), 500  # 예외 처리