from flask_smorest import Blueprint  # smorest의 Blueprint 사용
from app import db
from app.models import Question, Choices
from flask import request, jsonify

# Blueprint 생성 (smorest Blueprint 사용)
choices_bp = Blueprint('choices', __name__, url_prefix='/choices')

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
