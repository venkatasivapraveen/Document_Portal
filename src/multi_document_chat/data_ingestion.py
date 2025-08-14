class DocumentIngestor:
    SUPPORTED_EXTENSIONS = {'.pdf', '.docx', '.txt', '.md'}
    def __init__(self, temp_dir:str = "data/multi_document_chat/temp", faiss_dir: str = "faiss_index", session_id: str | None = None):
        try:
            self.log = CustomLogger().get_logger(__name__)

            self.temp_dir = Path(temp_dir)
            self.temp_dir.mkdir(parents=True, exist_ok=True)
            self.faiss_dir = Path(faiss_dir)
            self.faiss_dir.mkdir(parents=True, exist_ok=True)
            self.log = CustomLogger().get_logger(__name__)
        except Exception as e:
            self.log.error("Error initializing DocumentIngestor", error=str(e))
            raise DocumentPortalException("Error initializing DocumentIngestor", sys)
        
    def ingest_files(self, uploaded_files):
        try:
            documents=[]

            for uploaded_file in uploaded_files:
                ext = Path(uploaded_file.name).suffix.lower()
                if ext not in self.SUPPORTED_EXTENSIONS:
                    self.log.warning("Unsupported file skipped", filename=uploaded_file.name)
                    continue
        