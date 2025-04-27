# 📖 Storytelling com Streamlit: Explorando o Titanic

Este projeto usa **Streamlit** para criar uma experiência interativa de **storytelling baseada em dados** reais do Titanic.  
O objetivo é **contar histórias visuais** e **explorar padrões ocultos** sobre os passageiros que embarcaram nessa jornada histórica.

---

## 🔥 Sobre o Projeto

- **História Contada em Dados**: Apresenta métricas e insights sobre passageiros, sexo, classes e faixas etárias.
- **Exploração Visual**: Permite filtrar dados e visualizar sobrevivência por sexo, classe e idade através de gráficos.
- **Interatividade**: Usuário pode aplicar filtros para uma análise mais direcionada.

Tudo construído com **Streamlit**, utilizando **Python**, **Pandas**, **Seaborn** e **Matplotlib**.

---

## 📂 Estrutura

O projeto contém duas principais páginas:

- **Página 1 - História do Titanic**  
  Uma narrativa inicial com visão geral dos passageiros e taxa de sobrevivência em diferentes grupos.

- **Página 2 - Explore os Dados**  
  Área para explorar os dados em mais detalhes, com filtros por sexo, classe e ticket, além de visualizações gráficas.

---

## 🚀 Como Rodar o Projeto

1. Clone o repositório:

```bash
git clone https://github.com/luhborba/storytelling-streamlit.git
cd storytelling-streamlit
```

2. Instale as dependências com Poetry:

```bash
poetry install
```

3. Ative o ambiente:

```bash
poetry shell
```

4. Execute o projeto:

```bash
streamlit run Página_Inicial.py
```


storytelling-streamlit/
├── Pages
├──├── 1_Explore_os_Dados.py   # 2º Página - Explore os Dados
├── Página_Inicial.py          # Página principal - História do Titanic
├── Explore.py                 # Página de exploração interativa
├── README.md                  # Arquivo de documentação
├── pyproject.toml             # Configurações do Poetry
└── ...
