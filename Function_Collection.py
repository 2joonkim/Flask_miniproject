#QUESTION
def get_question(question_id):
    question = Question.query.get(question_id)
return question

#ANSWER
    