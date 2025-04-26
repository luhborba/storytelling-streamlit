import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="whitegrid")
st.set_page_config(page_title="Explore os Dados", page_icon="📈")
st.title("📊 Análise por Faixa Etária, Sexo e Classe")

df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

st.sidebar.header("🎛️ Filtros")

sexo = st.sidebar.selectbox("Filtrar por sexo:", options=["Todos", "male", "female"])

mapa_classe = {
    "Todas": None,
    "1ª Classe": 1,
    "2ª Classe": 2,
    "3ª Classe": 3
}
classe_legivel = st.sidebar.selectbox("Filtrar por classe:", options=list(mapa_classe.keys()))

tickets_unicos = df["Ticket"].dropna().unique().tolist()
tickets_selecionados = st.sidebar.multiselect("Filtrar por ticket:", options=tickets_unicos)

df_filtrado = df.copy()

if sexo != "Todos":
    df_filtrado = df_filtrado[df_filtrado["Sex"] == sexo]

if mapa_classe[classe_legivel] is not None:
    df_filtrado = df_filtrado[df_filtrado["Pclass"] == mapa_classe[classe_legivel]]

if tickets_selecionados:
    df_filtrado = df_filtrado[df_filtrado["Ticket"].isin(tickets_selecionados)]

bins = [0, 9, 19, 39, 59, 100]
labels = ['0–9', '10–19', '20–39', '40–59', '60+']
df_filtrado["Faixa Etária"] = pd.cut(df_filtrado["Age"], bins=bins, labels=labels)

fig1, ax1 = plt.subplots(figsize=(8, 5))
sns.countplot(data=df_filtrado, y="Faixa Etária", hue="Survived", palette="Set2", ax=ax1)
ax1.set_title("Distribuição de Sobreviventes por Faixa Etária", fontsize=14)
ax1.set_xlabel("Total de Passageiros")
ax1.set_ylabel("Faixa Etária")
ax1.legend(title="Sobreviveu", labels=["Não", "Sim"])

fig2, ax2 = plt.subplots(figsize=(7, 4))
sns.countplot(data=df_filtrado, x="Sex", hue="Survived", palette="muted", ax=ax2)
ax2.set_title("Distribuição de Sobreviventes por Sexo", fontsize=14)
ax2.set_xlabel("Sexo")
ax2.set_ylabel("Total")
ax2.legend(title="Sobreviveu", labels=["Não", "Sim"])

fig3, ax3 = plt.subplots(figsize=(7, 4))
sns.countplot(data=df_filtrado, x="Pclass", hue="Survived", palette="muted", ax=ax3)
ax3.set_title("Distribuição de Sobreviventes por Classe", fontsize=14)
ax3.set_xlabel("Classe")
ax3.set_ylabel("Total")
ax3.set_xticklabels(["1ª Classe", "2ª Classe", "3ª Classe"])
ax3.legend(title="Sobreviveu", labels=["Não", "Sim"])

col1, col2 = st.columns(2)

with col1:
    st.pyplot(fig1)

with col2:
    st.pyplot(fig2)

st.pyplot(fig3)

st.markdown("> 🎨 Cada gráfico conta uma história. Com elegância, clareza e propósito.")
