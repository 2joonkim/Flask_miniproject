from views.images import images_bp
from views.questions import questions_bp
from views.answers import answers_bp
from views.choices import choices_bp
from views.users import users_bp

def register_routes(app):
    # Blueprint 등록
    app.api.register_blueprint(images_bp, url_prefix='/images')
    app.api.register_blueprint(questions_bp, url_prefix='/questions')
    app.api.register_blueprint(answers_bp, url_prefix='/answers')
    app.api.register_blueprint(choices_bp, url_prefix='/choices')
    app.api.register_blueprint(users_bp, url_prefix='/users')
