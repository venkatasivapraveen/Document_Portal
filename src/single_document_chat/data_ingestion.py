import uuid
from pathlib import Path
import sys
from datetime import datetime, timezone
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from logger.custom_logger import CustomLogger
from exception.custom_exception_archive import DocumentPortalException
from utils.model_loader import ModelLoader

class SingleDocIngestor:
    def __init__(self,data_dir: "data/single_document_chat", faiss_dir: str = "faiss_index"):
        try:
            self.log = CustomLogger().get_logger(__name__)
            self.data_dir = Path(data_dir)
            self.data_dir.mkdir(parents=true, exist_ok=True)

            self.faiss_dir = Path(faiss_dir)
            self.faiss_dir.mkdir(parents=true, exist_ok=True)


            self.model_loader = ModelLoader()
            self.log.info("SingleDocIngestor initialized", temp_path=str(self.data_dir), faiss_path=str(self.faiss_dir))
        except Exception as e:
            self.log.error("Error initializing SingleDocIngestor", error=str(e))
            raise DocumentPortalException("Error initializing SingleDocIngestor", sys)
        

    def ingestfiles(self):
        try:
            documents = []

            for uploaded_file in uploaded_files:
                unique_filename = f"session_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:8]}.pdf"
                temp_path=self.data_dir / unique_filename

                with open(temp_path, "wb") as f_outs:
                    f_outs.write(uploaded_file.read())
                self.log.info("PDF saved for ingestion", filename=uploaded_file.name)
                loader = PyPDFLoader(str(temp_path))
                docs = loader.load()
                documents.extend(docs)
            self.log.info("PDF files loaded", count=len(documents))
            return self._create_retriever(documents)

        except Exception as e:
            self.log.error("Error ingesting files", error=str(e))
            raise DocumentPortalException("Error ingesting files", sys) 
        

    def _create_retriever(self,documents):
        try:
            splitter = RecursiveCharacterTextSplitter(chunck_size=1000, chunk_overlap=300)
            chunks = splitter = splitter_documents(documents)
            self.log.info("Documents split into chunks", count=len(chunks))

            embeddings = self.model_loader.load_embeddings()
            vectorstore = FAISS.from_documents(documents=chunks, embedding=embeddings)

            vectorstore.save_local(str(self.faiss_dir))
            self.log.info("FAISS index created and saved", faiss_path=str(sself.faiss_dir))
            retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k":5})
            self.log.info("retriever created successfully", retriever_type=str(type(retriever)))
            return retriever
            

        except Exception as e:
            self.log.error("Error creating retriever", error=str(e))
            raise DocumentPortalException("Error creating retriever", sys)
