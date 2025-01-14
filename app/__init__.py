from flask import Flask
from flask_migrate import Migrate
from flask_smorest import Api  # smorest 임포트
from config import db
import app.models

migrate = Migrate()

def create_app():
    application = Flask(__name__)

    # config 설정을 애플리케이션에 적용
    application.config.from_object("config.Config")
    application.secret_key = application.config["SECRET_KEY"]  # 시크릿 키 설정

    # DB 초기화
    db.init_app(application)

    # Migrate 초기화
    migrate.init_app(application, db)

    # smorest API 설정
    api = Api(application)  # OPENAPI_VERSION을 config에서 자동으로 불러옴

    # 블루프린트 등록
    from app.views.users import users_bp
    from app.views.questions import questions_bp
    from app.views.choices import choices_bp
    from app.views.answers import answers_bp
    from app.views.images import images_bp

    # smorest의 API에서 블루프린트 등록
    api.register_blueprint(users_bp)
    api.register_blueprint(questions_bp)
    api.register_blueprint(choices_bp)
    api.register_blueprint(answers_bp)
    api.register_blueprint(images_bp)

    return application
