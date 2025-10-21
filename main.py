import streamlit as stt
from agente import (
    agente_explorador,
    agente_especialista_ambiental,
    agente_especialista_economia,
    agente_decisor,
    data_de_hoje,
)

st.set_page_config(layout="centered")
st.markdown(
    """
<style>
    /* Estilizar o texto dentro de todos os campos de input do Streamlit */
    .stTextInput > div > div > input {
        color: #26272B;
    }
</style>
""",
    unsafe_allow_html=True,
)  

st.title("🛍️ Clau: Seu Assistente de Compras Inteligentes")
st.image("clau.png", width=400)

st.write(
    "Digite o que você quer comprar e seu orçamento, e o Clau te ajudará a decidir!"
)

produto = st.text_input("O que você gostaria de comprar hoje?", "Tênis de Corrida")
orcamento = st.text_input("Qual seu orçamento disponível? (Ex: R$600)", "R$600")

if st.button("Obter Recomendações"):
    if produto and orcamento:
        with st.spinner(
            "Clau está pensando... Buscando as melhores opções para você! 🚀"
        ):
            lista_produtos = agente_explorador(produto, data_de_hoje)
            praticas_sustentaveis = agente_especialista_ambiental(
                produto, lista_produtos
            )
            aspectos_economicos = agente_especialista_economia(produto, lista_produtos)
            decisao = agente_decisor(
                produto, praticas_sustentaveis, aspectos_economicos, orcamento
            )
            st.markdown("---")
            st.subheader("🎉 Suas Recomendações do Clau:")
            st.markdown(decisao)

    else:
        st.warning("Por favor, preencha o tópico e o orçamento.")

st.markdown("---")
st.markdown("Desenvolvido com 💖 Vinicius Rocha")
