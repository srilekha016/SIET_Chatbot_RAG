import faiss
import numpy as np
from groq import Groq
from pypdf import PDFReader
from sentence_transformers import SentenceTransformer

#load pdfs
def load_pdf (pdf_path):
  reader = PDFReader(str(pdf_path))
  mypages = [ i.extract_text() or "" for i in reader.pages]
  full_text = 
  if i !=-1:
    background=""
    for 
