import streamlit as st
import pandas as pd
import joblib

# Carregar o modelo
model = joblib.load('modelo_bancario.pkl')

st.title("💰 Previsão de Saldo Bancário")
st.markdown("Simule uma transação e veja o impacto no saldo da conta.")

# Criando campos de entrada baseados no dataset
age = st.number_input("Idade do Cliente", 18, 100, 30)
amount = st.number_input("Valor da Transação", 0.0, 10000.0, 500.0)
logins = st.slider("Tentativas de Login", 1, 5, 1)
duration = st.number_input("Duração da Transação (segundos)", 1, 1000, 60)

if st.button("Calcular Saldo Estimado"):
    # Organizar dados
    entrada = pd.DataFrame([[age, amount, logins, duration]], 
                          columns=['CustomerAge', 'TransactionAmount', 'LoginAttempts', 'TransactionDuration'])
    
    # Predição
    predicao = model.predict(entrada)[0]
    
    st.subheader(f"Saldo Estimado: R$ {predicao:,.2f}")
    
    # Estética de Banco
    if predicao < 1000:
        st.warning("Atenção: Saldo previsto abaixo do limite de segurança.")
    else:
        st.success("Transação processada com sucesso.")