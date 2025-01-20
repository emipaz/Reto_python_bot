from langchain_community.document_loaders.text import TextLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import CSVLoader
import os

# leemos la carpeta Documentos
docs = []
for documento in os.listdir("data"):
    path = os.path.join("data", documento )
    print("cargando :",path)
    if str.endswith(path, ".md") or str.endswith(path, ".txt"):
        documentos = TextLoader(path,encoding="utf-8").load()
    elif str.endswith(path, ".pdf"):
        documentos = PyPDFLoader(path).load()
    elif str.endswith(path, ".csv"):
        documentos = CSVLoader(path).load()
    else:
        continue
    # print(type(documentos))
    # print(len(documentos))
    # print(documentos[0].metadata)
    # print(documentos[0].page_content[:1000])
    docs.extend(documentos)
print(f"se cargaron {len(docs)}")
for doc in docs:
    print(doc.metadata)
    
# Fragmentar los archivos que sean necesarios en fragmento mas aptos para la busqueda semantica

from langchain_text_splitters import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 150
)

fragmentos = text_splitter.split_documents(docs)

print("La documentacion se fragmento en :", len(fragmentos))

for fragmento in fragmentos:
    print(fragmento.metadata)
    
# Para crear la base nececitamos los embeddings de openai
# necesitamos cargar la api y la base chroma
from dotenv import load_dotenv , find_dotenv

if load_dotenv(find_dotenv()):
    from langchain_openai import OpenAIEmbeddings
    from langchain_chroma import Chroma
    emb = OpenAIEmbeddings()
    BASE = Chroma (persist_directory="base", 
                    embedding_function=emb)
    print("Base de datos vacia creada en la carpeta base")
else:
    print("no se encontro el archivo .env")


# creamos un id para cada documento para poder modifcarlo luego si es necesario

ids =  []
for i, fragmento in enumerate(fragmentos):
    ids.append(f"id_{str(i)}_"+fragmento.metadata["source"])
#print("listas de ids para los docuentos :")
#print(*ids,sep="\n" )

doc_indexados =BASE.add_documents(documents=fragmentos, ids=ids)

print("listas de documentos indexados :")
print(*doc_indexados,sep="\n" )
