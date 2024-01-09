from functools import wraps

from api.utils.parse_requests import pares_post_request
from flask import request, make_response, jsonify

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'json'}


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def upload_file_payload(next_to):
    @wraps(next_to)
    def wrapper(*args, **kwargs):
        file = request.files.get("file")
        if not file:
            return make_response(jsonify({
                "message": "file is required",
                "success": False
            })), 406
        if not allowed_file(file.filename):
            extensions = " | ".join(ALLOWED_EXTENSIONS)
            return make_response(jsonify({
                "message": f"Extension not allowed, Allowed extentions: ({extensions})",
                "success": False
            })), 406
        return next_to(file, *args, **kwargs)

    return wrapper
