from flask import Blueprint, jsonify, request
from app.models import Answer, User, Choices
from config import db

# Blueprint 생성
answers_bp = Blueprint("answers", __name__, url_prefix="/submit")

# 다중 응답 저장
@answers_bp.route("", methods=["POST"])
def submit_answers():
    data = request.get_json()  # 요청 데이터를 JSON으로 파싱
    
    if not isinstance(data, list):  # 요청 데이터가 배열인지 확인
        return jsonify({"error": "요청 바디는 배열 형식이어야 합니다."}), 400

    results = []  # 저장 결과를 저장할 리스트

    for entry in data:
        user_id = entry.get("userId")
        choice_id = entry.get("choiceId")

        if not user_id or not choice_id:
            return jsonify({"error": "userId와 choiceId는 필수입니다."}), 400

        # 사용자와 선택지 확인
        user = User.query.get(user_id)
        choice = Choices.query.get(choice_id)

        if not user:
            return jsonify({"error": f"유효하지 않은 사용자 ID: {user_id}"}), 400
        if not choice:
            return jsonify({"error": f"유효하지 않은 선택지 ID: {choice_id}"}), 400

        # 새 응답 생성
        new_answer = Answer(user_id=user_id, choice_id=choice_id)
        db.session.add(new_answer)
        results.append({"userId": user_id, "choiceId": choice_id})  # 저장된 데이터를 결과에 추가

    # 변경 사항 커밋
    db.session.commit()

    return jsonify({"message": "답변 저장 완료", "saved": results}), 201