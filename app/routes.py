from views.images import images_bp
from views.questions import questions_bp
from views.answers import answers_bp
from views.choices import choices_bp
from views.users import users_bp

def register_routes(app):
    # Blueprint 등록
    app.register_blueprint(images_bp, url_prefix='/api/images')
    app.register_blueprint(questions_bp, url_prefix='/api/questions')
    app.register_blueprint(answers_bp, url_prefix='/api/answers')
    app.register_blueprint(choices_bp, url_prefix='/api/choices')
    app.register_blueprint(users_bp, url_prefix='/api/users')
