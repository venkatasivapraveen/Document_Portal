import sys
import os
from operator import itemgetter
from typing import List, Optional, Dict, Any

from langchain_core.messages import BaseMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import FAISS

from utils.model_loader import ModelLoader
from exception.custom_exception_archive import DocumentPortalException
from logger.custom_logger import CustomLogger
from prompt.prompt_library import PROMPT_REGISTRY
from model.models import PromptType

class ConversationalRAG:
    def __init__(self,session_id:str, retriever=None):

        self.log = CustomLogger().get_logger(__name__)
        

    def load_retiever_from_faiss(self):
        pass

    def _load_llm(self):
        pass

    @staticmethod
    def _format_docs(docs):
        pass

    def _build_lcel_chin(self):
        pass
