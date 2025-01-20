from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv , find_dotenv

load_dotenv(find_dotenv())
emb = OpenAIEmbeddings()
BASE = Chroma (persist_directory="base", 
                embedding_function=emb)

# print (BASE.get())

# busqueda semantica
def busqueda_semantica(pregunta, k=5):
    res = ""
    fragmentos = BASE.max_marginal_relevance_search(pregunta, k=5)
    for doc in fragmentos:
        res += f"Fuente : {doc.metadata["source"]}\n" 
        res += doc.page_content + "\n\n"
    return res


if __name__ == "__main__":
    pregunta = input (">>>")
    # vamos a traer los 5 fragmentos mas relevantes para una pregunta

    contexto = busqueda_semantica(pregunta, k=5)
    print(contexto)
    
    # for i, doc in enumerate(fragmentos):
    #     print("fragmento Nº:" , i)
    #     print(doc.metadata["source"])
    #     print(fill(doc.page_content,80))