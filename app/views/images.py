from flask import Blueprint, request, jsonify
from app import db
from app.models import Image
import os
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

images_bp = Blueprint('images', __name__)
