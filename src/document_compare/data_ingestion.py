import sys
from pathlib import Path
import fitz  # PyMuPDF
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException


class DocumentComparator:
    def __init__(self,base_dir):
        self.log = CustomLogger().get_logger(__name__)
        self.base_dir = Path(base_dir)
        self.base_dir.make_dirs(parents=True, exist_ok=True)




    def delete_existing_files(sself, file_paths):
        """
        Delete existing files at specified paths.
        """
        try:
            pass
        except Exception as e:
            self.log.error(f"Error deleting existing files: {e}")
            raise DocumentPortalException("Error deleting existing files", sys)

    def save_uploaded_files(self):
        """
        Save uploaded files to the server.
        """
        try:
            self.delete_existing_files()
            self.log.info("Existing files deleted successfully.")

            ref_path=""
            act_path=""
            
        except Exception as e:
            self.log.error(f"Error saving uploaded files: {e}")
            raise DocumentPortalException("Error saving uploaded files", sys)

    def read_pdf(self):
        """
        Read the content of a PDF file.
        """
        try:
            with fitz.open(pdf_path) as doc:
                if doc.is_encrypted:
                    raise ValueError(f"PDF is encrypted: {pdf_path.name}")
                all_text = []
                for page_num in range(doc.page_count):
                    page=doc.load_page(page_num)
                    text = page.get_text()
                    if text.strip():
                        all_text.append(f"\n --- page {page_num + 1} --- \n{text}")
                self.log.info(f"PDF read successfully: {pdf_path.name}, pages: {len(all_text)}")
                return "\n".join(all_text)                

        except Exception as e:
            self.log.error(f"Error reading PDF: {e}")
            raise DocumentPortalException("Error reading PDF", sys)
    