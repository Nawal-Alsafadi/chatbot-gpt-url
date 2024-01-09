from flask import make_response, jsonify

from api.middle_wares.train_chatbot_payload import train_chatbot_payload
from api.models.chat_model.emix_service_model.emix_service_model import EmixServiceChat
from api.models.chat_model.utils_chat_model.train_index_model import TrainIndexModel
from api.utils.paths import Paths


@train_chatbot_payload
def retain_chat_emix(with_sitemap,dataPath):
    MYpATH = Paths()
    try:
        # print("hola from retrain chatr emix")
        emix_service_chat = EmixServiceChat()
        
        emix_service_chat.add_data_and_train(with_sitemap=with_sitemap , dataPath=dataPath)
        # train_index_model = TrainIndexModel()
        # train_index_model.construct_index(directory_path=MYpATH.chatEmixMainDocs,with_sitemap=with_sitemap)
        
        return make_response(jsonify({
            "message": "Training completed successfully",
            "success": True,

        })), 200
    except Exception as e:
        print(e)
        return make_response(jsonify({
            "message": "something went wrong, we're working to solve it",
            "success": False,
        })), 500
