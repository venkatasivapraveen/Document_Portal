import os
from utils.model_loader import ModelLoader
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException
from model.models import *
from langchain_core.output_parsers import JsonOutputParser
from langchain.output_parsers import OutputFixingParser


class DocumentAnalyzer:
    """
    Main class for document analysis.
    Loads models, processes documents, and handles analysis logic.
    """

    def __init__(self):
        pass

    def analyze_metadata(self):
        pass