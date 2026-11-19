import faiss
import numpy as np
from groq import Groq
from pypdf import PDFReader
from sentence_transformers import SentenceTransformer

#load pdfs
def load_pdf (pdf_path):
  def load_pdf (pdf_path):
  reader = PDFReader(str(pdf_path))
  mypages = [ i.extract_text() or "" for i in raeder.pages]
  full_text = "\n".join(mypages).strip()
  if not full_text:
    raise ValueError("No readable Text Found")
  return full_text

  #chunking
  def create_chunks(full_text, chunksize = 500, overlap = 100):
    chunks = []
    start = 0
    while start<len(full_text):
      end = start + chunksize
      chunk = full_text[start:end]
      if chunk.strip():
        chunks.append(chunk)
        start = chunksize - overlap
        return chunks

#Embedding:
def build_vectors (chunks, model_name = "all-MiniLM-L6-V2"):
  embd_model = SentenceTransformer(model_name)
  embd_vectors = embed_model.encode(chunks, convert_to_numpy = True)
  faiss.normalize_L2(embed_vectors)
  index = faiss.IndexFlatIP(embed_vectors.shape[1])
  index.add(embed_vectors)
  return index, embed_model
  
  #Call loadpdf, chunk, embedding
def load_base (pdf_path= "01_College_Information.pdf"):
  full_text = load_pdf(pdf_path)
  chunks = create_chunks(full_text)
  embed_model, index = build_vector(chunks)
  return embed_model, chunks, index
