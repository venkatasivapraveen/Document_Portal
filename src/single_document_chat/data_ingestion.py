import uuid
from pathlib import Path
import sys
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException
from utils.model_loader import ModelLoader

class SingleDocIngestor:
    def __init__(self):
        try:
            self.log = CustomLogger().get_logger(__name__)
        except Exception as e:
            self.log.error("Error initializing SingleDocIngestor", error=str(e))
            raise DocumentPortalException("Error initializing SingleDocIngestor", sys)
        

    def ingestfiles(self):
        try:
            pass
        except Exception as e:
            self.log.error("Error ingesting files", error=str(e))
            raise DocumentPortalException("Error ingesting files", sys) 
        

    def _create_retriever(self):
        try:
            pass
        except Exception as e:
            self.log.error("Error creating retriever", error=str(e))
            raise DocumentPortalException("Error creating retriever", sys)
