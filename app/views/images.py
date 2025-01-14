from flask import Blueprint, jsonify, request
from app.models import Image
from config import db

images_bp = Blueprint("images", __name__, url_prefix="/images")

# 이미지 목록 조회
@images_bp.route("/", methods=["GET"])
def get_images():
    images = Image.query.all()
    return jsonify([img.to_dict() for img in images]), 200

# 이미지 업로드
@images_bp.route("/", methods=["POST"])
def upload_image():
    data = request.get_json()
    url = data.get("url")
    type = data.get("type")

    if not url or not type:
        return jsonify({"error": "필수 데이터가 부족합니다."}), 400

    new_image = Image(url=url, type=type)
    db.session.add(new_image)
    db.session.commit()

    return jsonify(new_image.to_dict()), 201