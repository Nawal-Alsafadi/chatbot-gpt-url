from langchain.memory import ConversationBufferMemory
from api.utils.first_init import FirstInit

from api.utils.paths import Paths
from llama_index.llms import OpenAI
from llama_index import StorageContext, load_index_from_storage, LLMPredictor, PromptHelper, ServiceContext

from api.models.chat_model.utils_chat_model.processor import Processor

from api.models.chat_model.utils_chat_model.train_index_model import TrainIndexModel


class EmixServiceChat:
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
        self.paths = Paths()

        self.process = Processor()
        self.index = None
        self.query_engine = None
        self.chat_engine = None
        self.evaluator = None
        self.memory = ConversationBufferMemory(memory_key="chat_history")

        self.initialize_bot()

    def initialize_bot(self):
        try : 
            self.index = self.load_index()
            self.query_engine = self.load_query_engine()
            self.chat_engine = self.load_chat_engine()
  
        except Exception as e:
            print(f"An error occurred during bot initialization: {e}")
        # Add more details about the exception for debugging
            import traceback
            traceback.print_exc()


    # chat by agent function
    def chat_by_chat_engine(self, input_text):

        response = self.chat_engine.chat(input_text)
        return response

    # chat by query function
    def chat_by_query(self, input_text):
        response = self.query_engine.query(input_text, )
        response = response.response
        return response

    # The function responsible for the automated chat (query engin, chat engin)
    def chatbot_indexing_model(self, input_text):
        response = self.chat_by_chat_engine(input_text)
        print(f"response : {response}")
        reprocess_response = self.process.reproccess_response_index(response)
        return reprocess_response

    # reload index
    def load_index(self):

        print("*** load emix index ***")
        # define LLM


        # define service context & storage_context
        service_context = ServiceContext.from_defaults(llm = OpenAI())
########################### here !!
        storage_context = StorageContext.from_defaults(
            persist_dir=self.paths.chatEmixMainIndex)
        # load  index
        index = load_index_from_storage(storage_context=storage_context, service_context=service_context)

        return index

    # reload query_engine from local
    def load_query_engine(self):
        query_engine = self.index.as_query_engine(response_mode='compact', )
        return query_engine

    # reload agent_chain from local
    def load_chat_engine(self):
        chat_engine = self.index.as_chat_engine(chat_mode="condense_question", verbose=False)
        return chat_engine

    # main fun to add new data and retrain model
    def add_data_and_train(self,with_sitemap:bool, dataPath):
        train_index_model = TrainIndexModel()
        ###### D:/docs1 , TestPath = "D:/docs1"
        train_index_model.construct_index(directory_path=dataPath,with_sitemap=with_sitemap)
        self.initialize_bot()
