from flask import Blueprint, jsonify, request
from app.models import Answer, User, Choices, Question
from config import db

# Blueprint 생성
answers_bp = Blueprint("answers", __name__, url_prefix="/submit")

# 사용자 답변 생성
@answers_bp.route("", methods=["POST"])
def submit_answers():
    data = request.get_json()

    if not isinstance(data, list):
        return jsonify({"error": "요청 바디는 배열 형식이어야 합니다."}), 400

    saved_user_id = None  # 첫 번째 사용자 ID 저장
    for entry in data:
        user_id = entry.get("userId")
        choice_id = entry.get("choiceId")

        # 필수 데이터 확인
        if not user_id or not choice_id:
            return jsonify({"error": "userId와 choiceId는 필수입니다."}), 400

        # 사용자 및 선택지 확인
        user = User.query.get(user_id)
        choice = Choices.query.get(choice_id)

        if not user:
            return jsonify({"error": f"유효하지 않은 사용자 ID: {user_id}"}), 400
        if not choice:
            return jsonify({"error": f"유효하지 않은 선택지 ID: {choice_id}"}), 400

        # 질문과 선택지 연관 확인
        question = Question.query.get(choice.question_id)
        if not question:
            return jsonify({"error": f"선택지 ID {choice_id}에 연결된 질문이 없습니다."}), 400

        # 답변 생성
        new_answer = Answer(user_id=user_id, choice_id=choice_id)
        db.session.add(new_answer)

        # 첫 번째 사용자 ID 저장
        if saved_user_id is None:
            saved_user_id = user_id

    # 커밋
    db.session.commit()

    # 요청된 user_id로 메시지 응답
    return jsonify({
        "message": f"User: {saved_user_id}'s answers Success Create"
    }), 201