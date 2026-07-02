import streamlit as st
import google.generativeai as genai

# Configuração da API Key (pegando do Streamlit Secrets)
api_key = st.secrets.get("GOOGLE_API_KEY")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')

    st.title("Meu Coach de Inglês")
    st.write("Olá! Vamos praticar inglês? Escreva algo e eu ajudarei com a correção.")

    user_input = st.text_input("Digite sua frase em inglês:")

    if user_input:
        response = model.generate_content(f"Corrija esta frase em inglês e dê uma explicação breve: {user_input}")
        st.write(response.text)
else:
    st.error("Erro: A GOOGLE_API_KEY não foi encontrada nos Secrets do Streamlit.")
