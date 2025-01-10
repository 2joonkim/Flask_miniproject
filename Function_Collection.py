#QUESTION
def get_question(question_id):
    question = Question.query.get(question_id)
    return question

#ANSWER
def get_answer(answer_id):
    answer = Answer.query.get(answer_id)
    return answer

#image 조회
def get_image(image_id):
    image = Image.query.get(image_id)
    return image

#image 생성
def create_image(url, type, question_id):
    image = Image(
        url=url,
        type=type,
        question_id=question_id
    )
    db.session.add(image)
    db.session.commit()
    return image