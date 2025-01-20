from dotenv import load_dotenv , find_dotenv
load_dotenv(find_dotenv())

from config import *
from consulta_base import busqueda_semantica
from collections import deque
import openai
cliente = openai.Client()

def memoria (historial):
    cola = deque(maxlen=MEMORIA)
    for mensaje in historial:
        cola.append(mensaje)
    messages = list(cola)
    messages.insert(0,{"role": "system", "content":PROMPT_SISTEMA})
    return messages

def consulta(pregunta, historial):
    mensajes = memoria(historial)
    contexto = busqueda_semantica(pregunta,k=DOCUMENTOS)
    prompt = f"""
    PREGUNTA:
    {pregunta}
    CONTEXTO:
    {contexto}
    Siempre responde en el idioma de la pregunta
    """
    mensajes.append({"role": "user", "content":prompt})
    response = cliente.chat.completions.create(
        model = MODELO,
        temperature = 0.0,
        messages = mensajes
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    mem = []
    while True:
        if (pregunta := input(">>>")) == "salir": break
        mem.append({"role":"user","content":pregunta})
        respuesta = consulta(pregunta,mem)
        print("bot :", respuesta)
        mem.append({"role":"assistant","content":respuesta})

        
        
        
            
