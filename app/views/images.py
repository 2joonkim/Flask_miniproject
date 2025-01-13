from flask import Blueprint, jsonify
from app import db
from app.models import Image  # Image 모델 임포트
import os

# 확장자 타입은 제외시켰습니다. 어차피 로컬에서 받을거라면 이미지 확장자를 이렇게 받을거다라고
# 지정할 필요가 없어요
# Blueprint 생성
images_bp = Blueprint('images', __name__)

# 로컬에 있는 이미지 파일을 사용하여 데이터베이스에 저장하는 api 입니다.
@images_bp.route("/images", methods=["POST"])
def add_local_image():
    # 로컬 디렉토리에서 이미지를 가져올 경로 설정
    local_image_path = '경로/이미지'  #로컬 이미지 파일 경로 (수정 필요)

    if not os.path.exists(local_image_path):
        return jsonify({"error": "이미지 파일을 찾을 수 없습니다."}), 404

    # 이미지 정보를 데이터베이스에 저장
    new_image = Image(
        url=local_image_path,  # 파일 경로 저장
        type="main"  # 예시로 'main' 타입을 지정
    )
    db.session.add(new_image)
    db.session.commit()