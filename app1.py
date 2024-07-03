import streamlit as st
import pandas as pd
import numpy as np
import os 
import warnings 
import plotly.express as px
warnings.filterwarnings('ignore')
import matplotlib.pyplot as plt
from plotly import graph_objects as go

st.set_page_config(page_title="Gisele Marasini", page_icon=":bar_chart:",layout="wide")
st.markdown("<h1 style='font-size:50px; text-align: center;'> </h1>", unsafe_allow_html=True)
st.title("Análise de Sintomas de Ansiedade, Depressão e Estresse no Ambiente Universitário")
st.markdown('<style>div.block-container{padding-top:1rem; text-align: center;}</style>',unsafe_allow_html=True)


st.markdown("<h3 style='font-size:20px; text-align: center;'>Conhecer os indicadores de adoecimento psíquico nos estudantes universitários permite um melhor entendimento <br>das variáveis envolvidas e possíveis intervenções a serem realizadas no ambiente acadêmico.</h3>", unsafe_allow_html=True)

st.markdown("<h3 style='font-size:20px; text-align: center;'>Assim, este estudo objetivou investigar quais são os níveis de sintomas de depressão, ansiedade e estresse em universitários, <br>bem como, analisar se há correlação entre perfil de acadêmicos com os níveis de adoecimento.</h3>", unsafe_allow_html=True)
st.markdown("<h3 style='font-size:20px; text-align: center;'>Neste site, os resultados dos dados socioeconômicos, bem como dos resultados obtidos na Escala DASS-21 são apresentados de maneira completa.</h3>", unsafe_allow_html=True)

st.markdown("<h1 style='font-size:50px; text-align: center;'>Perfil dos Entrevistados</h1>", unsafe_allow_html=True)


# Load the data
file_path = 'gisele.xlsx'
df = pd.read_excel(file_path)

# Select relevant columns
df_idade = df[['idade']]
df_selected = df[['Escala Estresse', 'Escala Ansiedade', 'Escala Depressão']]


col1, col2 = st.columns((2))

with col1:
    st.subheader('Idade')
    colors1 = px.colors.sequential.Pinkyl
    fig1 = px.pie(df,values = 'cont', names = "idade", hole = 0.5, color='idade', color_discrete_sequence=colors1)
    fig1.update_traces(textposition='outside', textfont=dict(size=20), 
                       textinfo='percent+value+label', marker=dict(line=dict(color='white', width=2)))
    fig1.update_layout(legend_font_size=20)
    fig1.update_layout(showlegend=False)
    st.plotly_chart(fig1)

    #Relacionamento 
    st.subheader('Status do Relacionamento')
    data = {
    'Status': ['Solteiro(a)', 'Casado(a)', 'Namorando', 'Separado(a)', 'União Estável', 'Noiva'],
    'Quantidade': [36, 13, 6, 2, 1, 1]
    }
    custom_colors = ['#FF69B4', '#DE3163', '#9F2B68', '#811331', '#F88379', "#FF7F50"]
    # Create a DataFrame
    df2 = pd.DataFrame(data)
    # Create a horizontal bar chart using Plotly
    fig = px.bar(df2, x='Quantidade', y='Status', orientation='h', color='Status', color_discrete_sequence=custom_colors, text_auto='.2')
    fig.update_traces(textfont_size=15, textangle=0, textposition="outside", cliponaxis=False)
    fig.update_layout(xaxis=dict(title_font=dict(size=12), tickfont=dict(size=12)),
    yaxis=dict(title_font=dict(size=16), tickfont=dict(size=16)), showlegend=False)
    # Display the bar chart in Streamlit
    st.plotly_chart(fig)


    #Semestre do curso
    st.subheader('Semestre do Curso')
    colors3 = px.colors.sequential.Pinkyl_r
    fig1 = px.pie(df,values = 'cont', names = "semestre", hole = 0.5, color_discrete_sequence=colors3)
    fig1.update_traces(textposition='outside', textfont=dict(size=20), textinfo='percent+value+label', 
                       marker=dict(line=dict(color='white', width=2)))
    fig1.update_layout(legend_font_size=20)
    fig1.update_layout(showlegend=False)
    st.plotly_chart(fig1)


#Renda Familiar Mensal 
    st.subheader('Renda Familiar Mensal')
    data = {
    'Renda': ['Até 1 salário mínimo', 'De 1 a 3 salários mínimos', 'De 3 a 6 salários mínimos', 
              'De 6 a 9 salários mínimos', 'Mais de 9 salários mínimos'],
    'Quantidade': [5, 23, 19, 9, 3]
    }
    df2 = pd.DataFrame(data)
    fig = px.bar(df2, x='Renda', y='Quantidade', color='Quantidade', text_auto='.2', color_continuous_scale='sunsetdark')
    fig.update_traces(textfont_size=15, textangle=0, textposition="outside", cliponaxis=False)
    fig.update_layout(xaxis=dict(title_font=dict(size=15), tickfont=dict(size=15)),
    yaxis=dict(title_font=dict(size=12), tickfont=dict(size=12)), showlegend=False, coloraxis_showscale=False)
    st.plotly_chart(fig)





    
with col2:
    st.subheader('Gênero')
    colors2 = ['#82EEFD', '#59788E', '#1338BE']
    fig1 = px.pie(df,values = 'cont', names = "genero", hole = 0.5, color_discrete_sequence=colors2)
    fig1.update_traces(textposition='outside', textfont=dict(size=20), 
                       textinfo='percent+value+label', marker=dict(line=dict(color='white', width=2)))
    fig1.update_layout(legend_font_size=20)
    fig1.update_layout(showlegend=False)

    st.plotly_chart(fig1)


    #Estatus do Emprego 
    st.subheader('Status do Emprego')
    data = {
    'Emprego': ['Tempo Integral', 'Desempregado(a)', 'Meio Período', 'Autônomo(a)', 'Só Estudo', 'Aposentado(a)'],
    'Quantidade': [21, 21, 13, 2, 1, 1]
    }
    df2 = pd.DataFrame(data)
    fig = px.bar(df2, x='Emprego', y='Quantidade', color='Quantidade', text_auto='.2', color_continuous_scale='sunset')
    fig.update_traces(textfont_size=15, textangle=0, textposition="outside", cliponaxis=False)
    fig.update_layout(xaxis=dict(title_font=dict(size=15), tickfont=dict(size=15)),
    yaxis=dict(title_font=dict(size=12), tickfont=dict(size=12)), showlegend=False, coloraxis_showscale=False)
    st.plotly_chart(fig)


    #Quantas pessoas noram com vocÊ?
    st.subheader('Quantas Pessoas Moram com Você?')
    data = {
    'Emprego': ['Moro Sozinho(a)', 'Uma a Três', 'Quatro a Sete'],
    'Quantidade': [3, 41, 15]
    }
    colors4 = px.colors.sequential.Purp
    df2 = pd.DataFrame(data)
    fig1 = px.pie(df2, values = 'Quantidade', names = "Emprego", hole = 0.5, color='Emprego', color_discrete_sequence=colors4)
    fig1.update_traces(textposition='outside', textfont=dict(size=20), 
                       textinfo='percent+value+label', marker=dict(line=dict(color='white', width=2)))
    fig1.update_layout(legend_font_size=20)
    fig1.update_layout(showlegend=False)
    st.plotly_chart(fig1)


    st.subheader('Local em que Reside')
    colors1 = px.colors.sequential.Agsunset
    fig1 = px.pie(df,values = 'cont', names = "moradia2", hole = 0.5, color='moradia2', color_discrete_sequence=colors1)
    fig1.update_traces(textposition='outside', textfont=dict(size=20), 
                       textinfo='percent+value+label', marker=dict(line=dict(color='white', width=2)))
    fig1.update_layout(legend_font_size=20)
    fig1.update_layout(showlegend=False)
    st.plotly_chart(fig1)

  


# Set the title of the dashboard
st.subheader('.....................................................................................................................................................................')
st.markdown("<h1 style='font-size:50px; text-align: center;'>Resultados</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='font-size:30px; text-align: center;'>Pontuação Geral nas Três Subescalas</h3>", unsafe_allow_html=True)


col3, col4  = st.columns((2))

with col3:

    
    st.markdown("<h3 style='font-size:20px; text-align: left;'>Sobre a escala:</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='font-size:20px; text-align: left;'>O instrumento de pesquisa utilizado Escala de Depressão, Ansiedade e Estresse (DASS 21), que é uma escala de autorrelato do tipo Likert, cujo objetivo é o levantamento de sintomas de depressão, ansiedade e estresse.</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='font-size:20px; text-align: left;'>Para a análise dos dados, são consideradas as afirmativas correspondentes aos sintomas de depressão, ansiedade e estresse.</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='font-size:20px; text-align: left;'>Os níveis de sintomas medidos pela DASS 21, são:</h3>", unsafe_allow_html=True)
    st.markdown("<ul style='font-size:20px; text-align: left;'>"
            "<li>Normal</li>"
            "<li>Mínimo</li>"
            "<li>Moderado</li>"
            "<li>Grave</li>"
            "<li>Muito grave</li>"
            "</ul>", unsafe_allow_html=True)
    st.markdown("<h3 style='font-size:20px; text-align: left;'> </h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='font-size:20px; text-align: left;'> </h3>", unsafe_allow_html=True)
    #st.markdown("<h3 style='font-size:20px; text-align: left;'> </h3>", unsafe_allow_html=True)
    #st.markdown("<h3 style='font-size:20px; text-align: left;'> </h3>", unsafe_allow_html=True)

    
    # Set the title of the dashboard
    st.subheader('Escala de Estresse')
    data = {
    'Escala de Estresse': ['Mínimo', 'Moderado', 'Normal', 'Grave', 'Muito Grave'],
    'Quantidade': [9, 7, 28, 7, 8]
    }
    #custom_colors = ['#FF5733', '#33FF57', '#3357FF', '#F033FF', 'yellow']
    # Create a DataFrame
    df2 = pd.DataFrame(data)
    # Create a horizontal bar chart using Plotly
    fig = px.bar(df2, x='Escala de Estresse', y='Quantidade', color='Quantidade', text_auto='.2', color_continuous_scale='Magenta')
    fig.update_traces(textfont_size=18, textangle=0, textposition="outside", cliponaxis=False)
    fig.update_layout(showlegend=False, coloraxis_showscale=False)
    st.plotly_chart(fig)




    
with col4:

    # Set the title of the dashboard
    st.subheader('Escala de Ansiedade')
    data = {
    'Escala de Ansiedade': ['Mínimo', 'Moderado', 'Normal', 'Grave', 'Muito Grave'],
    'Quantidade': [1, 15, 29, 2, 12]
    }
    df2 = pd.DataFrame(data)
    # Create a horizontal bar chart using Plotly
    fig = px.bar(df2, x='Escala de Ansiedade', y='Quantidade', color='Quantidade', text_auto='.2', color_continuous_scale='Pinkyl')
    fig.update_traces(textfont_size=18, textangle=0, textposition="outside", cliponaxis=False)
    fig.update_layout(showlegend=False, coloraxis_showscale=False)
    st.plotly_chart(fig)


    # Set the title of the dashboard
    st.subheader('Escala de Depressão')
    data = {
    'Escala de Depressão': ['Mínimo', 'Moderado', 'Normal', 'Grave', 'Muito Grave'],
    'Quantidade': [8, 11, 28, 5, 7]
    }
    df2 = pd.DataFrame(data)
    # Create a horizontal bar chart using Plotly
    fig = px.bar(df2, x='Escala de Depressão', y='Quantidade', color='Quantidade', text_auto='.2', color_continuous_scale='Teal')
    fig.update_traces(textfont_size=18, textangle=0, textposition="outside", cliponaxis=False)
    fig.update_layout(showlegend=False, coloraxis_showscale=False)
    st.plotly_chart(fig)





st.subheader('Selecione os Níveis das Escalas de Estresse, Ansiedade e Depressão')




# Carregar o arquivo Excel
file_path1 = 'gisele.xlsx'
dff = pd.read_excel(file_path1)
dff2 = pd.read_excel(file_path1)
dff3 = pd.read_excel(file_path1)

# Exibir as opções únicas de "Escala Estresse"
escala_estresse_options = dff['Escala Estresse'].unique()
escala_ansiedade_options = dff2['Escala Ansiedade'].unique()
escala_depressao_options = dff3['Escala Depressão'].unique()

# Criar uma selectbox para selecionar a "Escala Estresse"
selected_escala_estresse = st.selectbox('Selecione o Nível da Escala de Estresse', escala_estresse_options)
selected_escala_ansiedade = st.selectbox('Selecione o Nível da Escala de Ansiedade', escala_ansiedade_options)
selected_escala_depressao = st.selectbox('Selecione o Nível da Escala de Depressão', escala_depressao_options)

# Filtrar o dataframe baseado na seleção
filtered_dff1 = dff[dff['Escala Estresse'] == selected_escala_estresse]
filtered_dff2 = dff[dff['Escala Ansiedade'] == selected_escala_ansiedade]
filtered_dff3 = dff[dff['Escala Depressão'] == selected_escala_depressao]

#st.dataframe(filtered_dff1)
#st.dataframe(filtered_dff2)
#st.dataframe(filtered_dff3)




col5, col6  = st.columns((2))

with col5:
    # Contar ocorrências por "idade" e "cont"
    st.subheader('Subescalas filtrado por Idade')
    grouped_data1 = filtered_dff1.groupby(['idade', 'cont']).size().reset_index(name='counts')
    grouped_data2 = filtered_dff2.groupby(['idade', 'cont']).size().reset_index(name='counts')
    grouped_data3 = filtered_dff3.groupby(['idade', 'cont']).size().reset_index(name='counts')
    fig = go.Figure()
    fig.add_trace(go.Funnel(
        name = 'Escala Estresse'+ " = " + selected_escala_estresse,
        y = grouped_data1['idade'],
        x = grouped_data1['counts'],
        textinfo = "value", marker=dict(color='#ABDEE6')))
    fig.add_trace(go.Funnel(
        name = 'Escala Ansiedade'+ " = " + selected_escala_ansiedade,
        y = grouped_data2['idade'],
        x = grouped_data2['counts'],
        textinfo = "value", marker=dict(color='#F6EAC2')))
    fig.add_trace(go.Funnel(
        name = 'Escala Depressão'+ " = " + selected_escala_depressao,
        y = grouped_data3['idade'],
        x = grouped_data3['counts'],
        textinfo = "value", marker=dict(color='#F3B0C3')))
    fig.update_layout(font=dict(size=14), legend=dict(font=dict(size=18)), yaxis=dict(title_font=dict(size=18), tickfont=dict(size=18)))
    st.plotly_chart(fig)



    # Contar ocorrências por "Status do Relacionamento" e "cont"
    st.subheader('Subescalas filtrado por Status do Relacionamento')
    grouped_data1 = filtered_dff1.groupby(['relacionamento', 'cont']).size().reset_index(name='counts')
    grouped_data2 = filtered_dff2.groupby(['relacionamento', 'cont']).size().reset_index(name='counts')
    grouped_data3 = filtered_dff3.groupby(['relacionamento', 'cont']).size().reset_index(name='counts')
    fig = go.Figure()
    fig.add_trace(go.Funnel(
        name = 'Escala Estresse'+ " = " + selected_escala_estresse,
        y = grouped_data1['relacionamento'],
        x = grouped_data1['counts'],
        textinfo = "value", marker=dict(color='#ABDEE6')))
    fig.add_trace(go.Funnel(
        name = 'Escala Ansiedade'+ " = " + selected_escala_ansiedade,
        y = grouped_data2['relacionamento'],
        x = grouped_data2['counts'],
        textinfo = "value", marker=dict(color='#F6EAC2')))
    fig.add_trace(go.Funnel(
        name = 'Escala Depressão'+ " = " + selected_escala_depressao,
        y = grouped_data3['relacionamento'],
        x = grouped_data3['counts'],
        textinfo = "value", marker=dict(color='#F3B0C3')))
    fig.update_layout(font=dict(size=14), legend=dict(font=dict(size=18)), yaxis=dict(title_font=dict(size=18), tickfont=dict(size=18)))
    st.plotly_chart(fig)



    # Contar ocorrências por "Semestre do Curso" e "cont"
    st.subheader('Subescalas filtrado por Semestre do Curso')
    grouped_data1 = filtered_dff1.groupby(['semestre', 'cont']).size().reset_index(name='counts')
    grouped_data2 = filtered_dff2.groupby(['semestre', 'cont']).size().reset_index(name='counts')
    grouped_data3 = filtered_dff3.groupby(['semestre', 'cont']).size().reset_index(name='counts')
    fig = go.Figure()
    fig.add_trace(go.Funnel(
        name = 'Escala Estresse'+ " = " + selected_escala_estresse,
        y = grouped_data1['semestre'],
        x = grouped_data1['counts'],
        textinfo = "value", marker=dict(color='#ABDEE6')))
    fig.add_trace(go.Funnel(
        name = 'Escala Ansiedade'+ " = " + selected_escala_ansiedade,
        y = grouped_data2['semestre'],
        x = grouped_data2['counts'],
        textinfo = "value", marker=dict(color='#F6EAC2')))
    fig.add_trace(go.Funnel(
        name = 'Escala Depressão'+ " = " + selected_escala_depressao,
        y = grouped_data3['semestre'],
        x = grouped_data3['counts'],
        textinfo = "value", marker=dict(color='#F3B0C3')))
    fig.update_layout(font=dict(size=14), legend=dict(font=dict(size=18)), yaxis=dict(title_font=dict(size=18), tickfont=dict(size=18)))
    st.plotly_chart(fig)



    # Contar ocorrências por "Renda Familiar Mensal" e "cont"
    st.subheader('Subescalas filtrado por Renda Familiar Mensal')
    grouped_data1 = filtered_dff1.groupby(['Renda', 'cont']).size().reset_index(name='counts')
    grouped_data2 = filtered_dff2.groupby(['Renda', 'cont']).size().reset_index(name='counts')
    grouped_data3 = filtered_dff3.groupby(['Renda', 'cont']).size().reset_index(name='counts')
    fig = go.Figure()
    fig.add_trace(go.Funnel(
        name = 'Escala Estresse'+ " = " + selected_escala_estresse,
        y = grouped_data1['Renda'],
        x = grouped_data1['counts'],
        textinfo = "value", marker=dict(color='#ABDEE6')))
    fig.add_trace(go.Funnel(
        name = 'Escala Ansiedade'+ " = " + selected_escala_ansiedade,
        y = grouped_data2['Renda'],
        x = grouped_data2['counts'],
        textinfo = "value", marker=dict(color='#F6EAC2')))
    fig.add_trace(go.Funnel(
        name = 'Escala Depressão'+ " = " + selected_escala_depressao,
        y = grouped_data3['Renda'],
        x = grouped_data3['counts'],
        textinfo = "value", marker=dict(color='#F3B0C3')))
    fig.update_layout(font=dict(size=14), legend=dict(font=dict(size=14)), yaxis=dict(title_font=dict(size=14), tickfont=dict(size=14)))
    st.plotly_chart(fig)


with col6:
    # Contar ocorrências por "genero" e "cont"
    st.subheader('Subescalas filtrado por Gênero')
    grouped_data1 = filtered_dff1.groupby(['genero', 'cont']).size().reset_index(name='counts')
    grouped_data2 = filtered_dff2.groupby(['genero', 'cont']).size().reset_index(name='counts')
    grouped_data3 = filtered_dff3.groupby(['genero', 'cont']).size().reset_index(name='counts')
    fig = go.Figure()
    fig.add_trace(go.Funnel(
        name = 'Escala Estresse'+ " = " + selected_escala_estresse,
        y = grouped_data1['genero'],
        x = grouped_data1['counts'],
        textinfo = "value", marker=dict(color='#ABDEE6')))
    fig.add_trace(go.Funnel(
        name = 'Escala Ansiedade'+ " = " + selected_escala_ansiedade,
        y = grouped_data2['genero'],
        x = grouped_data2['counts'],
        textinfo = "value", marker=dict(color='#F6EAC2')))
    fig.add_trace(go.Funnel(
        name = 'Escala Depressão'+ " = " + selected_escala_depressao,
        y = grouped_data3['genero'],
        x = grouped_data3['counts'],
        textinfo = "value", marker=dict(color='#F3B0C3')))
    fig.update_layout(font=dict(size=14), legend=dict(font=dict(size=18)), yaxis=dict(title_font=dict(size=18), tickfont=dict(size=18)))
    st.plotly_chart(fig)

        
        
    # Contar ocorrências por "Status do Emprego" e "cont"
    st.subheader('Subescalas filtrado por Status do Emprego')
    grouped_data1 = filtered_dff1.groupby(['emprego', 'cont']).size().reset_index(name='counts')
    grouped_data2 = filtered_dff2.groupby(['emprego', 'cont']).size().reset_index(name='counts')
    grouped_data3 = filtered_dff3.groupby(['emprego', 'cont']).size().reset_index(name='counts')
    fig = go.Figure()
    fig.add_trace(go.Funnel(
        name = 'Escala Estresse'+ " = " + selected_escala_estresse,
        y = grouped_data1['emprego'],
        x = grouped_data1['counts'],
        textinfo = "value", marker=dict(color='#ABDEE6')))
    fig.add_trace(go.Funnel(
        name = 'Escala Ansiedade'+ " = " + selected_escala_ansiedade,
        y = grouped_data2['emprego'],
        x = grouped_data2['counts'],
        textinfo = "value", marker=dict(color='#F6EAC2')))
    fig.add_trace(go.Funnel(
        name = 'Escala Depressão'+ " = " + selected_escala_depressao,
        y = grouped_data3['emprego'],
        x = grouped_data3['counts'],
        textinfo = "value", marker=dict(color='#F3B0C3')))
    fig.update_layout(font=dict(size=14), legend=dict(font=dict(size=18)), yaxis=dict(title_font=dict(size=18), tickfont=dict(size=18)))
    st.plotly_chart(fig)



    # Contar ocorrências por "Quantas Pessoas Moram com Você?" e "cont"
    st.subheader('Subescalas filtrado por Quantas Pessoas Moram com Você?')
    grouped_data1 = filtered_dff1.groupby(['moradia1', 'cont']).size().reset_index(name='counts')
    grouped_data2 = filtered_dff2.groupby(['moradia1', 'cont']).size().reset_index(name='counts')
    grouped_data3 = filtered_dff3.groupby(['moradia1', 'cont']).size().reset_index(name='counts')
    fig = go.Figure()
    fig.add_trace(go.Funnel(
        name = 'Escala Estresse'+ " = " + selected_escala_estresse,
        y = grouped_data1['moradia1'],
        x = grouped_data1['counts'],
        textinfo = "value", marker=dict(color='#ABDEE6')))
    fig.add_trace(go.Funnel(
        name = 'Escala Ansiedade'+ " = " + selected_escala_ansiedade,
        y = grouped_data2['moradia1'],
        x = grouped_data2['counts'],
        textinfo = "value", marker=dict(color='#F6EAC2')))
    fig.add_trace(go.Funnel(
        name = 'Escala Depressão'+ " = " + selected_escala_depressao,
        y = grouped_data3['moradia1'],
        x = grouped_data3['counts'],
        textinfo = "value", marker=dict(color='#F3B0C3')))
    fig.update_layout(font=dict(size=14), legend=dict(font=dict(size=18)), yaxis=dict(title_font=dict(size=18), tickfont=dict(size=18)))
    st.plotly_chart(fig)


    # Contar ocorrências por "Local em que Reside"" e "cont"
    st.subheader('Subescalas filtrado por Local em que Reside')
    grouped_data1 = filtered_dff1.groupby(['moradia2', 'cont']).size().reset_index(name='counts')
    grouped_data2 = filtered_dff2.groupby(['moradia2', 'cont']).size().reset_index(name='counts')
    grouped_data3 = filtered_dff3.groupby(['moradia2', 'cont']).size().reset_index(name='counts')
    fig = go.Figure()
    fig.add_trace(go.Funnel(
        name = 'Escala Estresse'+ " = " + selected_escala_estresse,
        y = grouped_data1['moradia2'],
        x = grouped_data1['counts'],
        textinfo = "value", marker=dict(color='#ABDEE6')))
    fig.add_trace(go.Funnel(
        name = 'Escala Ansiedade'+ " = " + selected_escala_ansiedade,
        y = grouped_data2['moradia2'],
        x = grouped_data2['counts'],
        textinfo = "value", marker=dict(color='#F6EAC2')))
    fig.add_trace(go.Funnel(
        name = 'Escala Depressão'+ " = " + selected_escala_depressao,
        y = grouped_data3['moradia2'],
        x = grouped_data3['counts'],
        textinfo = "value", marker=dict(color='#F3B0C3')))
    fig.update_layout(font=dict(size=14), legend=dict(font=dict(size=18)), yaxis=dict(title_font=dict(size=18), tickfont=dict(size=18)))
    st.plotly_chart(fig)