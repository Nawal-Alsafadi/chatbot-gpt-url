from llama_index import Document

from api.middle_wares.chat_with_emix_data import chat_with_emix_payload
from api.models.chat_model.emix_service_model.emix_service_model import EmixServiceChat
from flask import make_response, jsonify


@chat_with_emix_payload
def chat_with_emix(question: str):
    try:
        emix_service_chat = EmixServiceChat()
        
        result = emix_service_chat.chatbot_indexing_model(question)



        return make_response(jsonify({
            "message": "Response completed successfully.",
            "success": True,
            "result": result
        })), 200
    except Exception as e:
        print(f"error in chat_with_emix {e}")
        return make_response(jsonify({
            "message": "A problem occurred during the chat process ,{}. ".format(str(e)),
            "success": False,
        })), 500
