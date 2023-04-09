import streamlit as st
from streamlit_chat import Chat
from googlesearch import search

# Función para buscar sitios web de Streamlit
def search_streamlit_apps(query):
    results = []
    for url in search(query + " site:*.streamlit.app", num_results=10):
        results.append(url)
    return results

# Función para procesar los mensajes del usuario
def process_message(message):
    results = search_streamlit_apps(message)
    if results:
        response = "Resultados de la búsqueda:\n" + "\n".join(results)
    else:
        response = "No se encontraron resultados."
    return response

# Inicializar el chat
chat = Chat(process_message)

# Configurar la aplicación de Streamlit
st.title("Chatbot buscador de sitios *.streamlit.app")
chat.render()
