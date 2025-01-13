#question 조회
def get_question(question_id):
    question = Question.query.get(question_id)
    return question

#question 생성
def create_question(text):
    question = Question(
        text=text
    )
    db.session.add(question)
    db.session.commit()
    return question

#answer 조회
def get_answer(answer_id):
    answer = Answer.query.get(answer_id)
    return answer

#answer 생성
def create_answer(text, question_id):
    answer = Answer(
        text=text,
        question_id=question_id
    )
    db.session.add(answer)
    db.session.commit()
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

#user 조회
def get_user(user_id):
    user = User.query.get(user_id)
    return user

#user 생성
def create_user(name. age, gender, email):
    user = User(
        name=name,
        age=age,
        gender=gender,
        email=email
    )
    db.session.add(user)
    db.session.commit()
    return user
