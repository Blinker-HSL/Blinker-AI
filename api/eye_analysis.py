import os
from flask import request, jsonify
from werkzeug.utils import secure_filename
from utils.image_processor import process_image

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def analyze():
    files = request.files.getlist("images")
    image_paths = []
    for idx, file in enumerate(files):
        filename = secure_filename(f"{idx:03d}_{file.filename}")
        path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(path)
        image_paths.append(path)

    blink_count = 0
    eyes_closed = False
    for img_path in image_paths:
        ear = process_image(img_path)
        if ear is None:
            continue
        if ear < 0.21 and not eyes_closed:
            eyes_closed = True
        elif ear >= 0.21 and eyes_closed:
            blink_count += 1
            eyes_closed = False

    return jsonify({
        "blink_count": blink_count,
        "image_count": len(image_paths)
    })