from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter


def get_chunk_indexes(documents, chunks):
    full_text = "".join([doc.page_content for doc in documents])  # Acceder al texto de cada documento
    indixes = []

    # Recorrer los chunks y obtener los índices en el texto original
    start_idx = 0
    chunk_num = 0
    for chunk in chunks:
        chunk_text = chunk.page_content if hasattr(chunk, 'page_content') else chunk
        end_idx = start_idx + len(chunk_text)
        indixes.append((chunk_num, start_idx, end_idx))
        start_idx = end_idx
        chunk_num += 1

    return indixes


def getTextFromPDF(oFiles, filepath):
    try:
        # Cargar el PDF
        loader = PyPDFLoader(oFiles.uploadsPath+filepath)
        documents = loader.load()

        # Dividir el texto en fragmentos
        splitter = CharacterTextSplitter(chunk_size=oFiles.chunkSize, chunk_overlap=0)
        chunks = splitter.split_documents(documents)

        chunkIndexes = get_chunk_indexes(documents, chunks)

        return chunks, chunkIndexes

    except Exception as e:
        print(f"[X] Error processing PDF: {e}")
        return None, None
