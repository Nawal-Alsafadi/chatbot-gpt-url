from functools import wraps

from api.utils.parse_requests import pares_post_request
from flask import request, make_response, jsonify


def chat_with_emix_payload(next_to):
    @wraps(next_to)
    def wrapper(*args, **kwargs):
        data = pares_post_request(request=request)
        question = data.get("question")
        if not question:
            return make_response(jsonify({
                "message": "question is required",
                "success": False
            })), 406
        return next_to(question, *args, **kwargs)

    return wrapper
