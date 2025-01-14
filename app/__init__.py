from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restx import Api  # flask_restx로 변경
import app.models

# 데이터베이스 초기화
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class="config.Config"):
    application = Flask(__name__)

    # 애플리케이션 설정
    application.config.from_object(config_class)
    application.secret_key = "oz_form_secret"

    # 데이터베이스 초기화
    db.init_app(application)
    migrate.init_app(application, db)

    # Swagger UI 설정 (Flask-RESTX API 객체 생성)
    api = Api(application, version='1.0', title='API 테스트', description='테스트입니다')

    # Blueprint 등록
    from views.images import images_bp
    from views.questions import questions_bp
    from views.answers import answers_bp
    from views.choices import choices_bp
    from views.users import users_bp

    # Blueprints를 URL 접두어와 함께 등록
    application.register_blueprint(images_bp, url_prefix='/api/images')
    application.register_blueprint(questions_bp, url_prefix='/api/questions')
    application.register_blueprint(answers_bp, url_prefix='/api/answers')
    application.register_blueprint(choices_bp, url_prefix='/api/choices')
    application.register_blueprint(users_bp, url_prefix='/api/users')

    return application
