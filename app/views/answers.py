from flask import Blueprint, request, jsonify
from app import db
from app.models import User, Choices, Question  # Question 모델 임포트

# Blueprint 생성
answers_bp = Blueprint('answers', __name__)

@answers_bp.route('/questions/<int:question_id>/choices', methods=['POST'])
def create_choice(question_id):
    data = request.get_json()

    # 질문을 찾기 + 질문이 없다면 404 오류 노출
    question = Question.query.get_or_404(question_id)

    # 선택지 생성
    # sqe는 순서나 다른 관련정보를 나타내는 값입니다. ex. 질문1 / 질문2 등
    choice = Choices(
        content=data['content'], #만약 없을 시 500 서버 에러
        sqe=data['sqe'],
        question_id=question.id
    )

    # 데이터베이스 추가
    db.session.add(choice)
    db.session.commit()

    return jsonify(choice.to_dict()), 201