from flask_smorest import Blueprint  # smorest의 Blueprint 사용
from app import db
from app.models import Image
import os
from flask import jsonify

# Blueprint 생성 (smorest Blueprint 사용)
images_bp = Blueprint('images', __name__, url_prefix='/images')

@images_bp.route("/images", methods=["POST"])
def add_local_image():
    # 로컬 디렉토리에서 이미지를 가져올 경로 설정
    local_image_path = '경로/이미지'  # 로컬 이미지 파일 경로 (수정 필요)

    if not os.path.exists(local_image_path):
        return jsonify({"error": "이미지 파일을 찾을 수 없습니다."}), 404

    # 이미지 정보를 데이터베이스에 저장
    new_image = Image(
        url=local_image_path,  # 파일 경로 저장
        type="main"  # 예시로 'main' 타입을 지정
    )
    db.session.add(new_image)
    db.session.commit()

    return jsonify(new_image.to_dict()), 201
