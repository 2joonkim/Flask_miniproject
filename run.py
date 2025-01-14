from app import create_app
from flask_restx import Api

application = create_app()

if __name__ == "__main__":
    application.run(debug=True)
