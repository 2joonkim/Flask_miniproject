from flask import Blueprint, jsonify, request
from app.models import Answer, User, Choices
from config import db

# Blueprint 생성
answers_bp = Blueprint("answers", __name__, url_prefix="/submit")

# 사용자 답변 저장 API
@answers_bp.route("/", methods=["POST"])
def submit_answers():
    try:
        data = request.get_json()

        # 요청 데이터 형식 확인
        if not isinstance(data, list):
            return jsonify({"error": "요청 바디는 배열 형식이어야 합니다."}), 400

        saved_user_id = None  # 첫 번째 사용자 ID 저장

        for entry in data:
            user_id = entry.get("userId")
            choice_id = entry.get("choiceId")

            # 필수 데이터 확인
            if not user_id or not choice_id:
                return jsonify({"error": "userId와 choiceId는 필수입니다."}), 400

            # 유효성 검증
            user = User.query.get(user_id)
            choice = Choices.query.get(choice_id)

            if not user:
                return jsonify({"error": f"유효하지 않은 사용자 ID: {user_id}"}), 400
            if not choice:
                return jsonify({"error": f"유효하지 않은 선택지 ID: {choice_id}"}), 400

            # 답변 저장
            new_answer = Answer(user_id=user_id, choice_id=choice_id)
            db.session.add(new_answer)

            # 첫 번째 user_id 저장
            if saved_user_id is None:
                saved_user_id = user_id

        # 데이터베이스 커밋
        db.session.commit()

        # 성공 응답
        return jsonify({"message": f"User: {saved_user_id}'s answers Success Create"}), 201

    except Exception as e:
        # 예외 처리
        db.session.rollback()
        return jsonify({"error": f"서버 오류 발생: {str(e)}"}), 500