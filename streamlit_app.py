import openai
import os
import streamlit as st
from streamlit_chat import Chat
from googlesearch import search

# Cargar la clave API de OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

def search_streamlit_apps(query):
    results = []
    for url in search(query + " site:*.streamlit.app", num_results=10):
        results.append(url)
    return results

def get_gpt3_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

def process_message(message):
    if message.lower().startswith("buscar:"):
        query = message[7:].strip()
        results = search_streamlit_apps(query)
        if results:
            response = "Resultados de la búsqueda:\n" + "\n".join(results)
        else:
            response = "No se encontraron resultados."
    else:
        prompt = f"Usuario: {message}\nChatbot:"
        response = get_gpt3_response(prompt)
    return response

chat = Chat(process_message)

st.title("Chatbot combinado: buscador de sitios *.streamlit.app y GPT-3")
chat.render()
