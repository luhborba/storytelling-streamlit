import streamlit as st
import pandas as pd

st.set_page_config(page_title="História do Titanic", layout="centered")

st.title("O Titanic: Uma História Contada em Dados")
st.markdown("**Explore os dados dos passageiros do Titanic e descubra padrões ocultos.**")

df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

bins = [0, 9, 19, 39, 59, 100]
labels = ['0–9', '10–19', '20–39', '40–59', '60+']
df["Faixa Etária"] = pd.cut(df["Age"], bins=bins, labels=labels)

classe_nome = {1: "Primeira Classe", 2: "Segunda Classe", 3: "Terceira Classe"}
df["Classe Nomeada"] = df["Pclass"].map(classe_nome)

st.subheader("👥 Visão Geral dos Passageiros")

col1, col2, col3 = st.columns(3)
col1.metric("Total de Passageiros", df.shape[0])
col2.metric("Homens", df[df["Sex"] == "male"].shape[0])
col3.metric("Mulheres", df[df["Sex"] == "female"].shape[0])

col4, col5, col6 = st.columns(3)
col4.metric("1ª Classe", df[df["Classe Nomeada"] == "Primeira Classe"].shape[0])
col5.metric("2ª Classe", df[df["Classe Nomeada"] == "Segunda Classe"].shape[0])
col6.metric("3ª Classe", df[df["Classe Nomeada"] == "Terceira Classe"].shape[0])

st.subheader("📈 Taxas de Sobrevivência por Grupo")

def taxa_sobrevivencia_por_grupo(df, coluna, valor):
    total = df[df[coluna] == valor].shape[0]
    sobreviventes = df[(df[coluna] == valor) & (df["Survived"] == 1)].shape[0]
    return (sobreviventes / total * 100) if total > 0 else 0

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Sobrevivência - Mulheres", f"{taxa_sobrevivencia_por_grupo(df, 'Sex', 'female'):.1f}%")
col2.metric("Sobrevivência - Homens", f"{taxa_sobrevivencia_por_grupo(df, 'Sex', 'male'):.1f}%")
col3.metric("1ª Classe", f"{taxa_sobrevivencia_por_grupo(df, 'Classe Nomeada', 'Primeira Classe'):.1f}%")
col4.metric("2ª Classe", f"{taxa_sobrevivencia_por_grupo(df, 'Classe Nomeada', 'Segunda Classe'):.1f}%")
col5.metric("3ª Classe", f"{taxa_sobrevivencia_por_grupo(df, 'Classe Nomeada', 'Terceira Classe'):.1f}%")

st.markdown("### 🎂 Sobrevivência por Faixa Etária")
col6, col7, col8, col9, col10 = st.columns(5)
for i, faixa in enumerate(labels):
    col = [col6, col7, col8, col9, col10][i]
    taxa = taxa_sobrevivencia_por_grupo(df, "Faixa Etária", faixa)
    col.metric(f"Faixa {faixa}", f"{taxa:.1f}%")

st.markdown("**Explore a aba ao lado para ver a distribuição por faixa etária.**")
