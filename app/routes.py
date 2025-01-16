from views.images import images_bp
from views.questions import questions_bp
from views.answers import answers_bp
from views.choices import choices_bp
from views.users import users_bp
from views.stats_routes import stats_routes
from views.connect import connect_bp


def register_routes(app):
    """
    애플리케이션에 모든 Blueprint를 등록하는 함수.
    """
    # Blueprint 등록
    app.register_blueprint(images_bp, url_prefix='/images')
    app.register_blueprint(questions_bp, url_prefix='/questions')
    app.register_blueprint(answers_bp, url_prefix='/answers')
    app.register_blueprint(choices_bp, url_prefix='/choices')
    app.register_blueprint(users_bp, url_prefix='/users')
    app.register_blueprint(stats_routes, url_prefix='/stat_routes')
    app.register_blueprint(connect_bp)
