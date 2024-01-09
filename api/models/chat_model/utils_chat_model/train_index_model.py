import os
from llama_index import SimpleDirectoryReader, LLMPredictor, PromptHelper, ServiceContext, GPTVectorStoreIndex, \
    StorageContext, VectorStoreIndex
from langchain.llms import OpenAI
import openai
from api.utils.first_init import FirstInit
from api.utils.paths import Paths
from api.models.chat_model.utils_chat_model.processor import Processor


class TrainIndexModel:
    def __init__(self):
        self.paths = Paths()

        self.process = Processor()

        self.nameData = ""
        self.newData = ""

        print("End init Train Index Model !!!")

    def sitemap_docs(self):
        from langchain.document_loaders.sitemap import SitemapLoader
        from llama_index.schema import Document
        sitemap_loader = SitemapLoader(web_path="https://gpt-index.readthedocs.io/sitemap.xml",
                                       filter_urls=["https://gpt-index.readthedocs.io/en/latest/"])

        pages = sitemap_loader.load()
        documents = []
        for page in pages:
            document = Document(
                text=page.page_content,
                metadata=page.metadata
            )

            documents.append(document)
        return documents

    def construct_index(self, directory_path, with_sitemap: bool):
        # define service context & storage_context
        


        service_context = ServiceContext.from_defaults(llm=OpenAI())

        storage_context = StorageContext.from_defaults()
        documents = SimpleDirectoryReader(directory_path).load_data()
        print(f"sitemap {with_sitemap}")
        if with_sitemap:
            sitemap_documents = self.sitemap_docs()
            documents.extend(sitemap_documents)
        ##########################

        index = GPTVectorStoreIndex.from_documents(documents, service_context=service_context,
                                                   storage_context=storage_context)
        # save new index to indexing folder
        index.storage_context.persist(persist_dir=f'{self.paths.chatEmixIndexing}/indexAndTime')
        # replace index file with new index
        index.storage_context.persist(persist_dir=self.paths.chatEmixMainIndex)

    # The function responsible for add new data to the json file in "docs folder"
    def add_data_file(self, new_data):
        # split new data and add to self
        print('add_data_file')
        new_name_data, new_new_data = self.process.split_new_data_for_retrain(new_data)
        self.nameData = new_name_data
        self.newData = new_new_data
        # create new folder new data in docs
        os.mkdir(f"{self.paths.chatEmixDocs}/{self.nameData}")
        # save new data to docs folder
        self.process.save_to_json_file(self.nameData, self.newData,
                                       f"{self.paths.chatEmixDocs}/{self.nameData}/")

    # The function responsible for inserting index with  new data"
    def insert_new_data(self, path_new_data, index):
        # load new data
        new_documents = SimpleDirectoryReader(path_new_data).load_data()
        # insert new data to index
        for doc in new_documents:
            index.insert(document=doc)

        return index

    # save new index file to
    def save_new_index(self, index):
        # save new index to indexing folder
        index.storage_context.persist(persist_dir=f'{self.paths.chatEmixIndexing}/{self.nameData}')
        # replace index file with new index
        index.storage_context.persist(persist_dir=self.paths.chatEmixMainIndex)

        # The function responsible for add data to the index file And train Index model

    def add_data_and_train(self):
        #self.construct_index(self.paths.chatEmixMainDocs)
        print("\nEnd of add data And train index Model")

