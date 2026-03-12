# 📊 Data Science Projects

Repositório com projetos de Machine Learning aplicados a problemas reais, utilizando Python, Scikit-Learn e Streamlit para criação de interfaces interativas.

---

## 📑 Projeto 1: Classificação de Sobrevivência (Titanic)

### 📌 Descrição

Este projeto utiliza Machine Learning para prever se um passageiro do Titanic sobreviveria ou não ao naufrágio, com base em características como classe social, sexo, idade e tarifa paga.

### 🛠️ Tecnologias Utilizadas

| Tecnologia | Uso |
|---|---|
| **Python** | Linguagem principal |
| **Pandas** | Manipulação e limpeza de dados |
| **Scikit-Learn** | Treinamento do modelo `RandomForestClassifier` |
| **Joblib** | Salvamento do modelo treinado em arquivo `.pkl` |
| **Streamlit** | Criação da interface web interativa |

### 📁 Estrutura

```
titanic/
├── titanic.ipynb                  # Notebook de treinamento do modelo
├── app_titanic.py                 # Aplicação Streamlit
├── modelo_titanic.pkl             # Modelo treinado salvo
├── train.csv                      # Dataset de treino
├── test.csv                       # Dataset de teste
└── gender_submission.csv          # Exemplo de submissão
```

### 📊 Modelagem

O modelo foi treinado no Jupyter Notebook utilizando o dataset clássico do Titanic. As variáveis selecionadas foram:

- **Pclass** — Classe do passageiro (1ª, 2ª ou 3ª)
- **Sex** — Sexo do passageiro
- **Age** — Idade
- **SibSp** — Número de irmãos/cônjuges a bordo
- **Fare** — Tarifa paga pela passagem

**Pré-processamento:**
- Conversão de variáveis categóricas (`Sex`) para numéricas.
- Tratamento de valores nulos na coluna de Idade.

### ▶️ Como Executar

```bash
cd titanic
streamlit run app_titanic.py
```

---

## 📑 Projeto 2: Previsão de Saldo Bancário

### 📌 Descrição

Aplicação de regressão para estimar o saldo bancário final de um cliente após uma transação, analisando o comportamento do usuário e detalhes da operação.

### 🛠️ Tecnologias Utilizadas

| Tecnologia | Uso |
|---|---|
| **Python** | Linguagem principal |
| **Pandas** | Manipulação e análise de dados |
| **Scikit-Learn** | Treinamento do modelo `RandomForestRegressor` |
| **Joblib** | Salvamento do modelo treinado em arquivo `.pkl` |
| **Streamlit** | Interface para simulação de transações em tempo real |

### 📁 Estrutura

```
bank-fraud/
├── bank.ipynb                                          # Notebook de treinamento do modelo
├── app_bank.py                                         # Aplicação Streamlit
├── modelo_bancario.pkl                                 # Modelo treinado salvo
└── bank_transactions_data_2_augmented_clean_2.csv      # Dataset de transações
```

### 📊 Modelagem

Utilizando o dataset `bank_transactions_data_2_augmented_clean_2.csv`, o modelo aprendeu padrões baseados nas seguintes variáveis:

- **CustomerAge** — Idade do cliente
- **TransactionAmount** — Valor da transação
- **LoginAttempts** — Número de tentativas de login
- **TransactionDuration** — Duração da transação (em segundos)

O `RandomForestRegressor` foi escolhido pela sua capacidade de lidar com múltiplas variáveis de comportamento. O objetivo é fornecer uma estimativa de saldo para auxiliar no planejamento financeiro ou detecção de anomalias.

### ▶️ Como Executar

```bash
cd bank-fraud
streamlit run app_bank.py
```

---

## 🚀 Requisitos

Instale as dependências necessárias:

```bash
pip install pandas scikit-learn joblib streamlit
```

---

## 👤 Autor

Desenvolvido por **Kauã Félix**
