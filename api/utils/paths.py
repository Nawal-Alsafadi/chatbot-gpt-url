import os
from pathlib import Path


class Paths:
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self._initialized = True
        
        


    # Data
        
        current_working_directory = Path.cwd()
        self.dataPath = os.path.join(current_working_directory, 'api/data')
        # Data
        # self.dataPath = './data'
        # # Chat Bot Model
        self._chatBot = f'{self.dataPath}/chatbot_services'
        # # Vendor Chat Model
        # self._chatEmixService = f'{self._chatBot}/emix_service'
        # self.chatEmixDocs = f'{self._chatEmixService}/docs'
        # self.chatEmixIndexing = f'{self._chatEmixService}/indexing'
        # self.chatEmixMainIndex = f'{self._chatEmixService}/index'
        # self.chatEmixMainDocs = f'{self.chatEmixDocs}/docs1'
        
        
        self._chatEmixService = os.path.join(self._chatBot, 'emix_service')
        self.chatEmixDocs = os.path.join(self._chatEmixService, 'docs')
        self.chatEmixIndexing = os.path.join(self._chatEmixService, 'indexing')
        self.chatEmixMainIndex = os.path.join(self._chatEmixService, 'index')
        self.chatEmixMainDocs = os.path.join(self.chatEmixDocs, 'docs1')
        


# # print output to the console
# paths_instance = Paths()
# # Print out the paths
# current_working_directory = Path.cwd()
# print(f"project_folder: {current_working_directory}")
# print(f"dataPath: {paths_instance.dataPath}")
# print(f"_chatBot: {paths_instance._chatBot}")
# print(f"_chatEmixService: {paths_instance._chatEmixService}")
# print(f"chatEmixDocs: {paths_instance.chatEmixDocs}")
# print(f"chatEmixIndexing: {paths_instance.chatEmixIndexing}")
# print(f"chatEmixMainIndex: {paths_instance.chatEmixMainIndex}")
# print(f"chatEmixMainDocs: {paths_instance.chatEmixMainDocs}")