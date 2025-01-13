from flask import Flask, request, jsonify

# 기존 구조로 /question/질문 아이디 넘버/choices 모델 사용 새로운 선택지 생성 (post)
# 선택지 생성의 함수가 없기 때문에 create_choice로 아래 새로 함수를 만들었습니다 쓰다보니 안 내용입니다!
# 질문의 선택지 생성 [choices] 
@app.route('/questions/<int:question_id>/choices', methods=['POST'])
def create_choice(question_id):
    data = request.get_json()

    # 질문을 찾기 + 질문이 없다면 404 오류 노출
    question = Question.query.get_or_404(question_id)

    # 선택지 생성 / model.py 참조
    # sqe는 순서나 다른 관련정보를 나타내는 값입니다. ex. 질문1 / 질문2 등
    choice = Choices(
        content=data['content'],
        sqe=data['sqe'],
        question_id=question.id
    )
    # 데이터베이스 추가
    db.session.add(choice)
    db.session.commit()

    return jsonify(choice.to_dict()), 201


# 기존 구조로 /answer/ 에 선택한 선택지 및 선택을 한 사용자 정보 저장입니다.(post)
# 정답 데이터에 저장 [answers]
@app.route('/answers', methods=['POST'])
def save_answer():
    data = request.get_json()

    # 사용자와 선택지가 맞는지 확인 아니면 404 에러 표시
    user = User.query.get_or_404(data['user_id'])
    choice = Choices.query.get_or_404(data['choice_id'])
    
    # 중복 값 방지인데 여기서는 저도 질문이 좀 필요해서 이거는 조교님께 여쭤보겠습니다.
    # filter_by() 와 filter()를 사용할때 의 차이점이 잘 명확하게 이해가 안가요
    # gpt한테 물어보니 filter() 는 더 복잡한 조건일 때 쓴다는데 저는 가독성면에서 filter()이 더 좋아보여서
    # 이 부분은 물어보고 답변드리겠습니다.
    existing_answer = Answer.query.filter_by(user_id=data['user_id'], choice_id=data['choice_id']).first()
    if existing_answer:
        return jsonify({"message": "You have already answered this question"}), 400

    # 새로운 답변 객체 생성
    # user_id / choice_id는 사용자가 선택한 값
    answer = Answer(
        user_id=user.id,
        choice_id=choice.id
    )

    db.session.add(answer)
    db.session.commit()

    return jsonify(answer.to_dict()), 201

