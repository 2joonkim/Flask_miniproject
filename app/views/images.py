from flask_smorest import Blueprint
from app import db
from app.models import Image
import os
from flask import jsonify

# Blueprint 생성
images_bp = Blueprint('images', __name__, url_prefix='/images')

@images_bp.route("/images", methods=["POST"])
def add_local_image():
    base_dir = os.path.abspath(os.path.dirname(__file__))  # 현재 파일의 디렉토리 경로
    image_files = [
        'images_0.jpeg',
        'images_1.jpeg',
        'images_2.jpeg',
        'images_3.jpeg',
        'images_4.jpeg'
    ]
    
    # 각 이미지 파일에 대해 절대 경로를 생성하여 저장
    image_urls = []
    for image_file in image_files:
        local_image_path = os.path.join(base_dir, 'images', image_file)

        if not os.path.exists(local_image_path):
            return jsonify({"error": f"이미지 파일 '{image_file}'을 찾을 수 없습니다."}), 404
        
        # 이미지 정보를 데이터베이스에 저장
        new_image = Image(
            url=local_image_path,  # 파일 경로 저장
            type="main"  # 예시로 'main' 타입을 지정
        )
        db.session.add(new_image)
        db.session.commit()  # 커밋을 통해 실제 데이터베이스에 저장

        # 추가된 이미지의 id와 url을 저장하여 응답할 데이터 준비
        image_urls.append({
            'id': new_image.id,
            'url': new_image.url
        })
    
    # 모든 이미지가 저장된 후 응답
    return jsonify(image_urls), 201
