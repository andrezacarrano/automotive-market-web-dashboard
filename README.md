# 🚗 Car Sales Dashboard
Este projeto consiste no desenvolvimento e implementação de uma aplicação web interativa para exploração de dados de anúncios de veículos usados nos EUA, integrando análise de dados e engenharia de software.
Este é um aplicativo interativo desenvolvido com [Streamlit](https://streamlit.io/) para explorar dados de anúncios de carros usados nos Estados Unidos. Ele permite visualizar distribuições e relações entre variáveis como quilometragem, preço, ano do modelo, tipo de combustível, entre outros.
Este projeto consiste no desenvolvimento e implementação de uma aplicação web interativa para exploração de dados de anúncios de veículos usados nos EUA, integrando análise de dados e engenharia de software.

1. Objetivo do projeto
Desenvolvimento de um dashboard dinâmico para análise exploratória de dados (EDA) do mercado automóvel. O foco é permitir que utilizadores finais visualizem distribuições de preços, quilometragem e correlações entre variáveis de forma intuitiva, utilizando ferramentas de visualização interativa e infraestrutura em nuvem.

2. Resultado
Disponibilização de aplicação pública: Implementação de dashboard funcional hospedado em nuvem.

Análise Visual Interativa: Criação de histogramas e gráficos de dispersão que respondem a inputs do utilizador em tempo real.

Acesso Online: 🔗 Aceder ao Dashboard no Render

3. Ferramentas utilizadas
Linguagem: Python 3.8+

Bibliotecas: Streamlit, Pandas, Plotly Express.

DevOps & Cloud: Git, GitHub, Render (Hospedagem).

Ambiente: VS Code e Virtualenv (Ambientes Virtuais).

4. O que aprendi (Competências Desenvolvidas)
Engenharia de Software para Dados: Gestão de ambientes virtuais, estruturação de ficheiros de configuração (config.toml) e gestão de dependências (requirements.txt).

Cloud Deployment: Execução de ciclos de implementação automática (Continuous Deployment) via Render.

Visualização de Dados Interativa: Construção de gráficos dinâmicos com Plotly que superam as limitações de visualizações estáticas.

Linguagem Nominal e Padronização: Documentação técnica focada em resultados e processos, alinhada com as melhores práticas do mercado de tecnologia.

5. Melhorias futuras
Filtros Avançados: Implementação de seleções por marca, modelo e ano de fabrico na barra lateral.

Métricas de KPI: Inclusão de indicadores de preço médio e volume de anúncios por categoria.

Otimização de Performance: Implementação de cache de dados para acelerar o carregamento da aplicação em grandes volumes.

## 💻 Como executar localmente

1. Clone o repositório:

git clone https://github.com/andrezacarrano/car-sales-dashboard.git

# Aceda à pasta
cd car-sales-dashboard

# Instale as dependências
pip install -r requirements.txt

# Execute a aplicação
streamlit run app.py

##Estrutura do projeto
car-sales-dashboard/
├── app.py
├── vehicles_us.csv
├── requirements.txt
├── .streamlit/
│   └── config.toml
├── notebooks/
│   └── EDA.ipynb
└── README.md

---

##Requisitos
Python 3.8+
Streamlit
Pandas
Plotly

---

##Fonte dos dados
O conjunto de dados vehicles_us_csv contém informações sobre anúncios de carros usados nos EUA, incluindo preço, ano, modelo, tipo de combustível, quilometragem, entre outros.

---

##Demonstração
Acesse o app online:
 https://car-sales-dashboard-iauy.onrender.com/

---

Autora: Andreza Carrano LinkedIn | GitHub
