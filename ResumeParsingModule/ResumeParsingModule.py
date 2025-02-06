import fitz  # PyMuPDF for PDF files
import docx  # python-docx for DOCX files

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file"""
    doc = fitz.open(pdf_path)
    text = "\n".join([page.get_text() for page in doc])
    return text

def extract_text_from_docx(docx_path):
    """Extract text from a DOCX file"""
    doc = docx.Document(docx_path)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text

def extract_text_from_txt(txt_path):
    """Extract text from a TXT file"""
    with open(txt_path, "r", encoding="utf-8") as file:
        text = file.read()
    return text

def extract_resume_text(file_path):
    """Identify the file type and extract text accordingly"""
    if file_path.endswith(".pdf"):
        return extract_text_from_pdf(file_path)
    elif file_path.endswith(".docx"):
        return extract_text_from_docx(file_path)
    elif file_path.endswith(".txt"):
        return extract_text_from_txt(file_path)
    else:
        raise ValueError("Unsupported file format. Use PDF, DOCX, or TXT.")
