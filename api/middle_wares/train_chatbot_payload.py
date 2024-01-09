from functools import wraps

from api.utils.parse_requests import pares_post_request
from flask import request, make_response, jsonify


def train_chatbot_payload(next_to):
    @wraps(next_to)
    def wrapper(*args, **kwargs):
        data = pares_post_request(request=request)
        with_sitemap = data.get("with_sitemap", False)
        dataPath=data.get("dataPath", False)
        if not isinstance(with_sitemap,bool):
            return make_response(jsonify({
                "message": "with_sitemap must be bool",
                "success": False
            })), 406
        return next_to(with_sitemap,dataPath, *args, **kwargs)

    return wrapper
