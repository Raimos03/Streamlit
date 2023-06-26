import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import plotly.graph_objects as go
import plotly.express as px

import numpy as np

st.header("Dashboard World Pentaho")
st.text("Base World - Pedro Lima - 26-06-2023")



st.header("Respostas elencadas:")
st.markdown('\n##### 1 - Quais países possuem expectativa de vida maior que 73 anos com porcentagem maior  que 70% de uma unica lingua no continente europeu?')
#st.markdown('\n##### 2 - Pergunta 2?')

st.text("Populacao x Pais")


st.sidebar.text("Selecao:")
dtfiltro= pd.read_excel("Paises-idade-60-2.xlsx",index_col=0)

st.bar_chart(dtfiltro.sort_values(['Population']),x=["Name","Language"],y="Population")






columns2 = []
columns2.append(dtfiltro.index.name)

for x in range(1,len(dtfiltro.columns)):
    columns2.append(dtfiltro.columns[x])

dtf2= dtfiltro[["CountryCode","Language","Percentage"]].sort_values(by="Percentage",ascending=False)

i=0
datatable=[]
datatable.append(columns2)
for x in dtf2.values:
   inicio=dtf2.index[i]
   n,m,a=x
   #print(n,m,a)
   datatable.append([inicio,n,m,a])
   i+=1
    
st.text("Tabela")
fig = ff.create_table(datatable, height_constant=20)

st.plotly_chart(fig)


labelx2 = list(dtf2.index)
labelx22=["Percentage"]

valuey2 = [list(dtf2["Percentage"].values)]
labelxCode=[list(dtf2["CountryCode"].values)]

st.text("Grafico de Dispersao")
fig2 = ff.create_distplot(valuey2,labelx22)
st.plotly_chart(fig2)


###figura 3
dtf2["Nome"]=dtf2.index




st.text("Lingua por pais")
fig3 = px.bar(dtf2, x='Nome', y='Percentage',
             hover_data=['CountryCode', 'Language'], color='Language',
             labels={'pop':'Porcentagem por Pais'}, height=560)

fig4 = px.bar(dtf2, x='Language', y='Percentage',
             hover_data=['CountryCode', 'Language'], color='Nome',
             labels={'pop':'Porcentagem por Pais'}, height=600)




opcao = st.sidebar.selectbox(
    "Selecione uma opcao",("Porcentagem por país","Porcentagem por lingua")
)

if opcao == "Porcentagem por lingua":
    st.plotly_chart(fig4)

elif opcao =="Porcentagem por país":
    st.plotly_chart(fig3)