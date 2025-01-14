from flask import Blueprint, request, jsonify
from app import db
from app.models import Question, Choices
from flask_restx import Api

#블루프린트 설정
choices_bp = Blueprint('choices', __name__)

@choices_bp.route('/questions/<int:question_id>/choices', methods=['POST'])
def create_choice(question_id):
    data = request.get_json()

    # 질문을 찾기 + 질문이 없다면 404 오류 노출
    question = Question.query.get_or_404(question_id)

    # 선택지 생성
    choice = Choices(
        content=data['content'],
        sqe=data['sqe'],
        question_id=question.id
    )

    # 데이터베이스 추가
    db.session.add(choice)
    db.session.commit()

    return jsonify(choice.to_dict()), 201