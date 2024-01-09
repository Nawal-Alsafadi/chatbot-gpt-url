from flask import Blueprint

from api.controllers.chat_emix.chat_with_emix import chat_with_emix
from api.controllers.chat_emix.train_chat_emix import retain_chat_emix
from api.controllers.chat_emix.upload_file import upload_file

chat_emix_bp = Blueprint('chat_emix_bp', __name__)

chat_emix_bp.route('chat-emix', methods=['POST'])(chat_with_emix)
chat_emix_bp.route('train-chat-emix', methods=['POST'])(retain_chat_emix)
chat_emix_bp.route('upload-file', methods=['POST'])(upload_file)