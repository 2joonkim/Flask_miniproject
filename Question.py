from flask import Blueprint, jsonify
from app.Function_Collection import get_question

# Blueprint 생성
# "questions"라는 이름으로 Blueprint를 생성하여, 질문 관련 API를 그룹화
questions_bp = Blueprint("questions", __name__)

@questions_bp.route("/questions/<int:question_id>", methods=["GET"])
def get_question_by_id(question_id):
    """
    특정 질문 조회 API
    이 API는 클라이언트가 특정 질문의 ID를 전달하면, 해당 ID에 대한 질문 정보를 반환
    """

    # Function_Collection.py에 정의된 get_question 함수 호출
    # 질문 ID로 데이터베이스에서 질문 객체를 가져옴
    question = get_question(question_id)

    # 질문이 없을 경우, 404 응답 반환
    if not question:
        return jsonify({"error": "Question not found"}), 404

    # 질문이 있을 경우, 질문 객체의 주요 데이터를 딕셔너리로 변환하여 JSON 응답으로 반환
    return jsonify({
        "id": question.id,
        "title": question.title,
        "is_active": question.is_active,
        "sqe": question.sqe
    }), 200