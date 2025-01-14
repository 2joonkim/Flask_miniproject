from flask_smorest import Blueprint  # smorest의 Blueprint 사용
from app import db
from app.models import Answer, Question, User
from flask import request, jsonify

# Blueprint 생성 (smorest Blueprint 사용)
answers_bp = Blueprint('answers', __name__, url_prefix='/api/answers')

@answers_bp.route('/questions/<int:question_id>/answers', methods=['POST'])
def create_answer(question_id):
    data = request.get_json()

    # 질문을 찾기 + 질문이 없다면 404 오류 노출
    question = Question.query.get_or_404(question_id)

    # 유저 ID와 답변 내용 받기
    user_id = data.get('user_id')
    content = data.get('content')

    # 유저가 없거나 내용이 없으면 오류 반환
    if not user_id or not content:
        return jsonify({"error": "유저 ID와 내용은 필수입니다."}), 400

    # 답변 생성
    answer = Answer(
        content=content,
        user_id=user_id,
        question_id=question.id
    )

    # 데이터베이스에 답변 추가
    db.session.add(answer)
    db.session.commit()

    return jsonify(answer.to_dict()), 201
