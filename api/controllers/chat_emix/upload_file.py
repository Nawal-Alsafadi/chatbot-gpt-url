from api.middle_wares.upload_file_payload import upload_file_payload
import os
from api.utils.paths import Paths
from flask import request, make_response, jsonify


@upload_file_payload
def upload_file(file):
    try:
        file.save(os.path.join(Paths().chatEmixMainDocs, file.filename))
        return make_response(jsonify({
            "message": "File uploaded successfully.",
            "success": True,
        })), 202
    except Exception as e:
        print(e)
        return make_response(jsonify({
            "message": "something went wrong, we're working to solve it",
            "success": False,
        })), 500
