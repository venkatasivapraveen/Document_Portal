import sys
import os
from dotenv import load_dotenv
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_community.vectorstores import FAISS
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain.chains import create_history_aware_reetriever, create_retrievel_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from utils.model_loader import ModelLoader
from exception.custom_exception import DocumentPortalException
from logger.custom_logger import CustomLogger
from prompt.prompt_library import PROMPT_REGISTRY
from model.models import PromptType


class ConverstionalRag:
    def __init__(self,session_id: str, retriever) -> None:
        try:
            self.log = CustomLogger().get_logger(__name__)
        except Exception as e:
            self.log.error("Error initializing ConversationalRag", error=str(e))
            raise DocumentPortalException("Error initializing ConversationalRag", sys)
        

    def _load_llm(self):
        try:
            llm = ModelLoader().load_model()
            return llm
        except Exception as e:
            self.log.error("Error loading LLM", error=str(e))
            raise DocumentPortalException("Error loading LLM", sys)
        

    def _get_session_history(self, session_id: str) -> BaseChatMessageHistory:
        try:
            session_history = ChatMessageHistory(session_id)
            return session_history
        except Exception as e:
            self.log.error("Error getting session history", error=str(e))
            raise DocumentPortalException("Error getting session history", sys)
        

    def _load_retriever_from_faiss(self):
        try:
            pass

        except Exception as e:
            self.log.error("Error loading retriever from FAISS", error=str(e))
            raise DocumentPortalException("Error loading retriever from FAISS", sys)
        

    def invoke(self):
        try:
            pass
        except Exception as e:
            self.log.error("Error invoking ConversationalRag", error=str(e))
            raise DocumentPortalException("Error invoking ConversationalRag", sys)
