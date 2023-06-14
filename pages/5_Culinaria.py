#=========================================================================================================================================
                                                                #LIBRARIES E BIBLIOTECAS
#=========================================================================================================================================
from dash import Dash, html, dcc
from datetime import datetime
from haversine import haversine
from PIL import Image
from streamlit_folium import folium_static
from textwrap3 import wrap
import folium
import io
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import re
import streamlit as st

#=========================================================================================================================================
                                                    # Criando escalas de cores
#=========================================================================================================================================

PRETO =	'#000000'
CINZA_5 = '#1a191a'
CINZA_4 = '#3b3a3a'
CINZA_3 = '#585758'
CINZA_2 = '#7d7b7c'
CINZA_1 = '#adaaab'
MAGENTA_5 = '#3e0518'
MAGENTA_4 =	'#641832'
MAGENTA_3 = '#812d49'
MAGENTA_2 = '#a34d6a'
MAGENTA_1 = '#bb6a86'
VERMELHO_5 = '#881007'
VERMELHO_4 = '#982a21'
VERMELHO_3 = '#a6423a'
VERMELHO_2 = '#af615b'
VERMELHO_1 = '#bb8783'
VERMELHOCL_5 = '#f91605'
VERMELHOCL_4 = '#f93223'
VERMELHOCL_3 = '#fb564a'
VERMELHOCL_2 = '#fb7b71'
VERMELHOCL_1 =	'#fca49d'
AZUL_5 = '#0d0873'
AZUL_4 = '#110aa9'
AZUL_3 = '#1106f6'
AZUL_2 = '#534bf7'
AZUL_1 = '#7b75f6'
AZULCL_5 = '#025bff'
AZULCL_4 = '#2370fb'
AZULCL_3 = '#4987fa'
AZULCL_2 = '#70a1fb'
AZULCL_1 = '#9bbdfb'
VERDEESC_5 = '#1c3e08'
VERDEESC_4 = '#37641b'
VERDEESC_3 = '#4f7e32'
VERDEESC_2 = '#6a974e'
VERDEESC_1 = '#8ba57b'
VERDE_5 = '#034205'
VERDE_4 = '#05790a'
VERDE_3 = '#06ba0d'
VERDE_2 = '#11f31a'
VERDE_1 = '#6bfb71'
VERDECL_5 = '#07690b'
VERDECL_4 = '#217f25'
VERDECL_3 = '#459a48'
VERDECL_2 = '#5fab62'
VERDECL_1 = '#7ebf80'
LARANJA_5 =	'#b36d0a'
LARANJA_4 =	'#cd7c08'
LARANJA_3 =	'#ee8f08'
LARANJA_2 =	'#fba831'
LARANJA_1 = '#f9b85b'
AZULBB_5 = '#04b6b4'
AZULBB_4 = '#1dcbc9'
AZULBB_3 = '#3fd5d3'
AZULBB_2 =	'#67e5e4'
AZULBB_1 =	'#96f4f3'
AZVERD_5 = '#0cb25e'
AZVERD_4 = '#1cc46f'
AZVERD_3 = '#37dd89'
AZVERD_2 = '#5eeba4'
AZVERD_1 = '#8ff8c3'

Escal_CINZA = [CINZA_5, CINZA_4, CINZA_3, CINZA_2, CINZA_1]
Escal_MAGENTA = [MAGENTA_5, MAGENTA_4, MAGENTA_3, MAGENTA_2, MAGENTA_1]
Escala_VERMELHO = [VERMELHO_5, VERMELHO_4, VERMELHO_3, VERMELHO_2, VERMELHO_1]
Escal_VERMELHOCL = [VERMELHOCL_5, VERMELHOCL_4, VERMELHOCL_3, VERMELHOCL_2, VERMELHOCL_1]
Escal_AZUL = [AZUL_5, AZUL_4, AZUL_3, AZUL_2, AZUL_1]
Escal_AZULCL = [AZULCL_5, AZULCL_4, AZULCL_3, AZULCL_2, AZULCL_1]
Escal_VERDEESC = [VERDEESC_5, VERDEESC_4, VERDEESC_3, VERDEESC_2, VERDEESC_1]
Escal_VERDE = [VERDE_5, VERDE_4, VERDE_3, VERDE_2, VERDE_1]
Escal_VERDECL = [VERDECL_5, VERDECL_4, VERDECL_3, VERDECL_2, VERDECL_1]
Escal_LARANJA = [LARANJA_5, LARANJA_4, LARANJA_3, LARANJA_2, LARANJA_1]
Escal_AZULBB = [AZULBB_5, AZULBB_4, AZULBB_3, AZULBB_2, AZULBB_1]
Escal_AZVERD = [AZVERD_5, AZVERD_4, AZVERD_3, AZVERD_2, AZVERD_1]

CinMage = [CINZA_5, CINZA_4, CINZA_3, CINZA_2, CINZA_1, MAGENTA_5, MAGENTA_4, MAGENTA_3, MAGENTA_2, MAGENTA_1]
CinVerm = [CINZA_5, CINZA_4, CINZA_3, CINZA_2, CINZA_1, VERMELHO_5, VERMELHO_4, VERMELHO_3, VERMELHO_2, VERMELHO_1]
CinVermCL = [CINZA_5, CINZA_4, CINZA_3, CINZA_2, CINZA_1, VERMELHOCL_5, VERMELHOCL_4, VERMELHOCL_3, VERMELHOCL_2, VERMELHOCL_1]
CinZul = [CINZA_5, CINZA_4, CINZA_3, CINZA_2, CINZA_1, AZUL_5, AZUL_4, AZUL_3, AZUL_2, AZUL_1]
CinZulCL = [CINZA_5, CINZA_4, CINZA_3, CINZA_2, CINZA_1, AZULCL_5, AZULCL_4, AZULCL_3, AZULCL_2, AZULCL_1]
CinVerESC = [CINZA_5, CINZA_4, CINZA_3, CINZA_2, CINZA_1, VERDEESC_5, VERDEESC_4, VERDEESC_3, VERDEESC_2, VERDEESC_1]
CinVer = [CINZA_5, CINZA_4, CINZA_3, CINZA_2, CINZA_1, VERDE_5, VERDE_4, VERDE_3, VERDE_2, VERDE_1]
CinVerCL = [CINZA_5, CINZA_4, CINZA_3, CINZA_2, CINZA_1, VERDECL_5, VERDECL_4, VERDECL_3, VERDECL_2, VERDECL_1]
CinLaranj = [LARANJA_1, LARANJA_5, LARANJA_3, LARANJA_2, LARANJA_1, CINZA_5, CINZA_4, CINZA_3, CINZA_2, CINZA_1]
CinAzuBB = [CINZA_5, CINZA_4, CINZA_3, CINZA_2, CINZA_1, AZULBB_5, AZULBB_4, AZULBB_3, AZULBB_2, AZULBB_1]
CinAzVerd = [AZVERD_5, AZVERD_5, AZVERD_3, AZVERD_2, AZVERD_1, CINZA_5, CINZA_4, CINZA_3, CINZA_2, CINZA_1]
Especial_3 = [CINZA_1, CINZA_4, CINZA_2, AZULBB_5, AZULBB_3, AZULBB_1]
Especial_2 = [VERMELHO_1, VERMELHO_2, VERMELHO_5, VERMELHO_4] 



#  AJUSTANDO NOSSOS GRÁFICOS A ÁREA TOTAL DE NOSSOS CONTAINERS-------------------------------------------------------------------------------------------
#Aqui estamos expandindo apresentação de nossos gráfico a toda área de nosso container. 
st.set_page_config( page_title='Visão Culinária', layout='wide')    

#========================================================================================================================================================
                                                                             #FUNÇÕES
#========================================================================================================================================================
# Usamos df1.loc passando a coluna desejada para a comparação como linha e o nome da coluna a ser criada como coluna
# Ao final, todas as linhas comparadadas dentro da coluna criada, recebem o valor determinado.
# Como parâmetro de entrada a função recebe df1 e o retorno é o próprio df1 com a nova coluna criada e valores determinados
def colors(df1): 

    df1.loc[df1['Rating color'] == "3F7E00", 'Colors'] = "darkgreen"
    df1.loc[df1['Rating color'] == "5BA829", 'Colors'] = "green"    
    df1.loc[df1['Rating color'] == "9ACD32", 'Colors'] = "lightgreen"
    df1.loc[df1['Rating color'] == "CDD614", 'Colors'] = "orange"
    df1.loc[df1['Rating color'] == "FFBA00", 'Colors'] = "red"
    df1.loc[df1['Rating color'] == "CBCBC8", 'Colors'] = "darkred"
    df1.loc[df1['Rating color'] == "FF7800", 'Colors'] = "darkred"
   
    return(df1)



# Usamos df1.loc passando a coluna desejada para a comparação como linha e o nome da coluna a ser criada como coluna
# Ao final, todas as linhas comparadadas dentro da coluna criada, recebem o valor determinado.
# Como parâmetro de entrada a função recebe df1 e o retorno é o próprio df1 com a nova coluna criada e valores determinados

def paises(df1): 

    df1.loc[df1['Country Code'] == 1, 'Countries'] = "India"
    df1.loc[df1['Country Code'] == 14, 'Countries'] = "Austrália"
    df1.loc[df1['Country Code'] == 30, 'Countries'] = "Brazil"
    df1.loc[df1['Country Code'] == 37, 'Countries'] = "Canada"
    df1.loc[df1['Country Code'] == 94, 'Countries'] = "Indonesia"
    df1.loc[df1['Country Code'] == 148, 'Countries'] = "New Zeland"
    df1.loc[df1['Country Code'] == 162, 'Countries'] = "Filippines"
    df1.loc[df1['Country Code'] == 166, 'Countries'] = "Qatar"
    df1.loc[df1['Country Code'] == 184, 'Countries'] = "Singapure"
    df1.loc[df1['Country Code'] == 189, 'Countries'] = "South Africa"
    df1.loc[df1['Country Code'] == 191, 'Countries'] = "Sri Lanka"
    df1.loc[df1['Country Code'] == 208, 'Countries'] = "Turkey"
    df1.loc[df1['Country Code'] == 214, 'Countries'] = "United Arab Emirates"
    df1.loc[df1['Country Code'] == 215, 'Countries'] = "England"
    df1.loc[df1['Country Code'] == 216, 'Countries'] = "United States of America"
    
    return(df1)


# Usamos df1.loc passando a coluna desejada para a comparação como linha e o nome da coluna a ser criada como coluna
# Ao final, todas as linhas comparadadas dentro da coluna criada, recebem o valor determinado.
# Como parâmetro de entrada a função recebe df1 e o retorno é o próprio df1 com a nova coluna criada e valores determinados

def price_tye(df1):

    df1.loc[df1['Price range'] == 1, 'Price tye'] = "cheap"
    df1.loc[df1['Price range'] == 2, 'Price tye'] = "normal"
    df1.loc[df1['Price range'] == 3, 'Price tye'] = "expansive"
    df1.loc[df1['Price range'] == 4, 'Price tye'] = "high price"

    return(df1)


def Select_Rest(df1, culinaria): 
    """
    Esta função tem por responsabilidade apresentar os restaurantes de diversas culinárias com maior e menor média de avaliação, deatravés de um dataframe. O mesmo irá         receber um dataframe e uma variável que definirá qual a culinária escolhida
    """
    # Definimos aqui os 5 restaurantes com notas máximas
    Select_Rest = df1.loc[(df1['Cuisines'] == culinaria), ['Restaurant Name', 'Aggregate rating']]
    Select_Max = Select_Rest.loc[:,['Restaurant Name', 'Aggregate rating']].groupby (['Aggregate rating']).max().reset_index()  
    Select_Max = Select_Max.sort_values(by=['Aggregate rating'], ascending=False).head(5).reset_index(drop=True)
    Select_Max.columns = ['NOTA MAXIMA', 'RESTAURANTES_MAX']
    
    # Definimos aqui os 5 restaurantes com notas minimas
    Select_Min = Select_Rest.loc[:,['Restaurant Name', 'Aggregate rating']].groupby (['Aggregate rating']).min().reset_index()  
    Select_Min = Select_Min.sort_values(by=['Aggregate rating'], ascending=True).head(5).reset_index(drop=True)
    Select_Min.columns = ['NOTA MINIMA', 'RESTAURANTES_MIN']
    
    # Fazenis aqui a união dos dois dataframes com a função pd.merge usando how='inner' para preservar todos os dados em duas planilhas similares
    Select_Total = pd.merge(Select_Min, Select_Max, left_index=True, right_index=True, how='inner')
    
    # Aqui vamos tratar nosso dataframe com a função style (.highlight - para destacar os valores máximos e minimos / .set_caption - para incluir o titulo do gráfico
    # e .set_table_styles para definir o tratamento de forma, tamanho, centralização do mesmo / .format para tratar os valores dentro das colunas NOTA MINIMA e MAXIMA.
    Select_Total = ( Select_Total.style.highlight_min(subset=['NOTA MINIMA'], color=VERDE_4, props='background-color: #f91605; color: white')
                                 .highlight_max(subset=['NOTA MAXIMA'], color=VERDE_4, props='background-color: #06ba0d; color: white')
                                 .set_caption('CULINÁRIA ITALIANA - Tabela de Avaliações')
                                 .set_table_styles([{ 'selector': 'caption', 'props': 'font-size: 20px; font-weight: Bold ; text-align: center'}])
                                 .format({'NOTA MINIMA': '{:.2f}', 'NOTA MAXIMA': '{:.2f}'}) )
    
    return (Select_Total)


def Select_Rest_Two(df1, culinaria): 
    """
    Esta função tem por responsabilidade apresentar os restaurantes de diversas culinárias com maior e menor média de avaliação, deatravés de um dataframe. O mesmo irá         receber um dataframe e uma variável que definirá qual a culinária escolhida
    """
    # Definimos aqui os 5 restaurantes com notas máximas
    Select_Rest = df1.loc[(df1['Cuisines'] == culinaria), ['Restaurant Name', 'Aggregate rating']]
    Select_Max = Select_Rest.loc[:,['Restaurant Name', 'Aggregate rating']].groupby (['Aggregate rating']).max().reset_index()  
    Select_Max = Select_Max.sort_values(by=['Aggregate rating'], ascending=False).head(3).reset_index(drop=True)
    Select_Max.columns = ['NOTA MAXIMA', 'RESTAURANTES_MAX']
    
    # Definimos aqui os 5 restaurantes com notas minimas
    Select_Min = Select_Rest.loc[:,['Restaurant Name', 'Aggregate rating']].groupby (['Aggregate rating']).min().reset_index()  
    Select_Min = Select_Min.sort_values(by=['Aggregate rating'], ascending=True).head(3).reset_index(drop=True)
    Select_Min.columns = ['NOTA MINIMA', 'RESTAURANTES_MIN']
    
    # Fazenis aqui a união dos dois dataframes com a função pd.merge usando how='inner' para preservar todos os dados em duas planilhas similares
    Select_Total = pd.merge(Select_Min, Select_Max, left_index=True, right_index=True, how='inner')
    
    # Aqui vamos tratar nosso dataframe com a função style (.highlight - para destacar os valores máximos e minimos / .set_caption - para incluir o titulo do gráfico
    # e .set_table_styles para definir o tratamento de forma, tamanho, centralização do mesmo / .format para tratar os valores dentro das colunas NOTA MINIMA e MAXIMA.
    Select_Total = ( Select_Total.style.highlight_min(subset=['NOTA MINIMA'], color=VERDE_4, props='background-color: #f91605; color: white')
                                 .highlight_max(subset=['NOTA MAXIMA'], color=VERDE_4, props='background-color: #06ba0d; color: white')
                                 .set_caption('CULINÁRIA ITALIANA - Tabela de Avaliações')
                                 .set_table_styles([{ 'selector': 'caption', 'props': 'font-size: 20px; font-weight: Bold ; text-align: center'}])
                                 .format({'NOTA MINIMA': '{:.2f}', 'NOTA MAXIMA': '{:.2f}'}) )
    return (Select_Total)


def Select_Rest_Three(df1):
    """
    Esta função tem por responsabilidade apresentar os restaurantes de diversas culinárias com maior e menor média de avaliação, deatravés de um dataframe. O mesmo irá         receber um dataframe e uma variável que definirá qual a culinária escolhida
    """
    Select_Rest =( df1.loc[(df1['Restaurant ID'] == 6007184) | (df1['Restaurant ID'] == 5904119) | (df1['Restaurant ID'] == 18442162) | 
                  (df1['Restaurant ID'] == 18286221) | (df1['Restaurant ID'] == 5914190), ['Cuisines', 'Restaurant Name', 'Aggregate rating']] )
    Select_Max = Select_Rest.loc[:,['Restaurant Name', 'Aggregate rating']].groupby (['Aggregate rating']).max().reset_index()  
    Select_Max = Select_Max.sort_values(by=['Aggregate rating'], ascending=False).head(2).reset_index(drop=True)
    Select_Max.columns = ['NOTA MAXIMA', 'RESTAURANTES_MAX']

    Select_Min = Select_Rest.loc[:,['Restaurant Name', 'Aggregate rating']].groupby (['Aggregate rating']).min().reset_index()  
    Select_Min = Select_Min.sort_values(by=['Aggregate rating'], ascending=True).head(2).reset_index(drop=True)
    Select_Min.columns = ['NOTA MINIMA', 'RESTAURANTES_MIN']

    Select_Total = pd.merge(Select_Min, Select_Max, left_index=True, right_index=True, how='inner')
    
    # Aqui vamos tratar nosso dataframe com a função style (.highlight - para destacar os valores máximos e minimos / .set_caption - para incluir o titulo do gráfico
    # e .set_table_styles para definir o tratamento de forma, tamanho, centralização do mesmo / .format para tratar os valores dentro das colunas NOTA MINIMA e MAXIMA.
    Select_Total = ( Select_Total.style.highlight_min(subset=['NOTA MINIMA'], color=VERDE_4, props='background-color: #f91605; color: white')
                                 .highlight_max(subset=['NOTA MAXIMA'], color=VERDE_4, props='background-color: #06ba0d; color: white')
                                 .set_caption('CULINÁRIA ITALIANA - Tabela de Avaliações')
                                 .set_table_styles([{ 'selector': 'caption', 'props': 'font-size: 20px; font-weight: Bold ; text-align: center'}])
                                 .format({'NOTA MINIMA': '{:.2f}', 'NOTA MAXIMA': '{:.2f}'}) )

    return (Select_Total)


def Select_Topten_Cuisines(df1):
    """
    Esta função tem por responsabilidade apresentar os dez maiores valores médios de um prato para duas pessoas, através de um dataframe
    """
    Select_Rest = df1.loc[:, ['Cuisines', 'Average Cost for two', 'Currency']].groupby (['Cuisines', 'Currency']).mean().reset_index()
    Cuisines_Top = np.round(Select_Rest.loc[:, ['Cuisines', 'Average Cost for two', 'Currency']].groupby (['Cuisines']).max().reset_index(),2)
    Cuisines_Top = Cuisines_Top.sort_values(by=['Average Cost for two'], ascending=False).reset_index(drop=True).head(10)
    Cuisines_Top.columns = ['PRATOS', 'CUSTO PARA DOIS', 'MOEDA']
    
    return (Cuisines_Top)

        
def Select_Topten_Mean(df1): 
    """
    Esta função tem por responsabilidade apresentar os dez maiores notas médias por tipo de prato, através de um dataframe
    """
    Select_Rest = df1.loc[:, ['Cuisines', 'Aggregate rating']].groupby (['Cuisines']).mean().reset_index()
    Cuisines_Top = Select_Rest.loc[:, ['Cuisines', 'Aggregate rating']].groupby (['Cuisines']).max().reset_index()
    Cuisines_Top = Cuisines_Top.sort_values(by=['Aggregate rating'], ascending=False).reset_index(drop=True).head(10)
    Cuisines_Top.columns = ['PRATOS', 'NOTA MEDIA']    
                
    return (Cuisines_Top)


def CuisinesTop_TenDelivery(df1): 
    """
    Esta função tem por responsabilidade apresentar os dez tipos de pratos que aceitam pedidos e fazem entregas, através de um dataframe
    """
    Select_Rest = (df1.loc[(df1['Is delivering now'] == 1) & (df1['Has Online delivery'] == 1), 
                               ['Restaurant ID', 'Cuisines', 'Is delivering now', 'Has Online delivery']])
    Cuisines_Top = Select_Rest.loc[:, ['Restaurant ID', 'Cuisines']].groupby (['Cuisines']).count().head(10).reset_index()
    Cuisines_Top.columns = ['PRATOS', 'Nº RESTAURANTES']
    Cuisines_Top = Cuisines_Top.sort_values(by=['PRATOS'], ascending=True)
            
    return (Cuisines_Top)


def Graphic_Statistic(df1):  
    """
        Esta função tem por responsabilidade apresentar os dez tipos de pratos que aceitam pedidos e fazem entregas, através de um grafico de pizza plotly.express
    """
    Select_Rest =( df1.loc[(df1['Is delivering now'] == 1) & (df1['Has Online delivery'] == 1), 
                               ['Restaurant ID', 'Cuisines', 'Is delivering now', 'Has Online delivery']] )
    Cuisines_Top = Select_Rest.loc[:, ['Restaurant ID', 'Cuisines']].groupby (['Cuisines']).count().head(10).reset_index()
    #Cuisines_Top.columns = ['PRATOS', 'Nº RESTAURANTES']
    Cuisines_Top = Cuisines_Top.sort_values(by=['Cuisines'], ascending=True).head(10) 
    fig = go.Figure( data=[ go.Pie( labels=Cuisines_Top['Cuisines'], values=Cuisines_Top['Restaurant ID'], pull=[0.1, 0, 0])])
          
    return (fig)


def Graphic_Italian(df1):  
    """
    Esta função tem por responsabilidade apresentar os restaurantes de diversas culinárias com maior e menor média de avaliação, deatravés de um gráfico de barras. O mesmo     irá receber um dataframe e uma variável que definirá qual a culinária escolhida
    """
    # Definimos aqui os 5 restaurantes com notas máximas
    Select_Rest = df1.loc[(df1['Cuisines'] == 'Italian'), ['Restaurant Name', 'Aggregate rating']]
    Select_Max = Select_Rest.loc[:,['Restaurant Name', 'Aggregate rating']].groupby (['Aggregate rating']).max().reset_index()  
    Select_Max = Select_Max.sort_values(by=['Aggregate rating'], ascending=False).head(5).reset_index(drop=True)
    Select_Max.columns = ['NOTA', 'RESTAURANTE']
    # Definimos aqui os 5 restaurantes com notas minimas
    Select_Min = Select_Rest.loc[:,['Restaurant Name', 'Aggregate rating']].groupby (['Aggregate rating']).min().reset_index()  
    Select_Min = Select_Min.sort_values(by=['Aggregate rating'], ascending=True).head(5).reset_index(drop=True)
    Select_Min.columns = ['NOTA', 'RESTAURANTE']
    # Fazenis aqui a união dos dois dataframes com a função pd.merge usando how='inner' para preservar todos os dados em duas planilhas similares
    Select_Total = pd.concat([Select_Min, Select_Max], ignore_index = True)  
    #Criando o gráfico
    fig, ax = plt.subplots(figsize=(15, 4))                                                  # Definindo o tamanho do gráfico                 
    ax.bar(Select_Total['RESTAURANTE'], Select_Total['NOTA'], color=CinMage)                 # Definindo as informações do eixo x e y e definindo as cores       
    plt.xlabel('RESTAURANTES', weight='bold')                                                # Destacando as informações trazidas pelos eixos x       
    plt.ylabel('AVALIAÇÕES', weight='bold')                                                  # Destacando as informações trazidas pelos eixos y      
    ax.spines['right'].set_visible(False)                                                    # Removendo grids e traços do lado direito
    ax.spines['left'].set_visible(False)                                                     # Removendo grids e traços do lado esquerdo       
    ax.spines['top'].set_visible(False)                                                      # Removendo grids e traços acima       
    #ax.spines['bottom'].set_visible(False)                                                  # Removendo grids e traços abaixo

    plt.text(x=2.00, y=6.3, s='RESTAURANTES DE CULINÁRIA ITALIANA', fontsize=16, color=MAGENTA_3, weight='bold')     # Definindo o Título do Gráfico
    plt.text(x=7.50, y=5.3, s='MAIORES MÉDIAS DE AVALIAÇÃO', fontsize=8, color=MAGENTA_3, weight='bold')             # Definindo informação das maiores médias
    plt.text(x=-0.70, y=5.3, s='MENORES MÉDIAS DE AVALIAÇÃO', fontsize=8, color=CINZA_4, weight='bold')              # Definindo informação das menores médias              

    labels = Select_Total['RESTAURANTE'].tolist()                               # Buscando o tamanho da lista das strings do eixo x p/tratamento e apresentação
    labels = ['\n'.join(wrap(l, 12)) for l in labels]                           # A função wrap vai inserir um \n a cada 12 caracteres - (ajustando o tamanho)
    plt.xticks(range(len(labels)), labels, rotation=0, color=PRETO);            # plt.xticks usa o labels p/ajustar os nomes ao tamanho correto de cada barra do eixo x 
    #plt.gca().axes.get_yaxis().set_visible(False)                              # Remnovendo o eixo y
    #plt.gca().axes.get_xaxis().set_visible(False)                              # Remnovendo o eixo x
    #.set_axis_off()                                                            # Removendo todos os eixos juntos
                                    
    return (fig)


def Graphic_American(df1):  
    """
    Esta função tem por responsabilidade apresentar os restaurantes de diversas culinárias com maior e menor média de avaliação, deatravés de um gráfico de barras. O mesmo     irá receber um dataframe e uma variável que definirá qual a culinária escolhida
    """
    # Definimos aqui os 5 restaurantes com notas máximas
    Select_Rest = df1.loc[(df1['Cuisines'] == 'American'), ['Restaurant Name', 'Aggregate rating']]
    Select_Max = Select_Rest.loc[:,['Restaurant Name', 'Aggregate rating']].groupby (['Aggregate rating']).max().reset_index()  
    Select_Max = Select_Max.sort_values(by=['Aggregate rating'], ascending=False).head(5).reset_index(drop=True)
    Select_Max.columns = ['NOTA', 'RESTAURANTE']
    # Definimos aqui os 5 restaurantes com notas minimas
    Select_Min = Select_Rest.loc[:,['Restaurant Name', 'Aggregate rating']].groupby (['Aggregate rating']).min().reset_index()  
    Select_Min = Select_Min.sort_values(by=['Aggregate rating'], ascending=True).head(5).reset_index(drop=True)
    Select_Min.columns = ['NOTA', 'RESTAURANTE']
    # Fazenis aqui a união dos dois dataframes com a função pd.merge usando how='inner' para preservar todos os dados em duas planilhas similares
    Select_Total = pd.concat([Select_Min, Select_Max], ignore_index = True)   
    #Criando o gráfico
    fig, ax = plt.subplots(figsize=(15, 4))                                                  # Definindo o tamanho do gráfico                 
    ax.bar(Select_Total['RESTAURANTE'], Select_Total['NOTA'], color=CinAzVerd)               # Definindo as informações do eixo x e y e definindo as cores       
    plt.xlabel('RESTAURANTES', weight='bold')                                                # Destacando as informações trazidas pelos eixos x       
    plt.ylabel('AVALIAÇÕES', weight='bold')                                                  # Destacando as informações trazidas pelos eixos y      
    ax.spines['right'].set_visible(False)                                                    # Removendo grids e traços do lado direito
    ax.spines['left'].set_visible(False)                                                     # Removendo grids e traços do lado esquerdo       
    ax.spines['top'].set_visible(False)                                                      # Removendo grids e traços acima       
    #ax.spines['bottom'].set_visible(False)                                                  # Removendo grids e traços abaixo

    plt.text(x=2.00, y=6.3, s='RESTAURANTES DE CULINÁRIA ITALIANA', fontsize=16, color=AZVERD_4, weight='bold')      # Definindo o Título do Gráfico
    plt.text(x=7.50, y=5.3, s='MAIORES MÉDIAS DE AVALIAÇÃO', fontsize=8, color=CINZA_4, weight='bold')               # Definindo informação das maiores médias
    plt.text(x=-0.70, y=5.3, s='MENORES MÉDIAS DE AVALIAÇÃO', fontsize=8, color=AZVERD_4, weight='bold')             # Definindo informação das menores médias              
   
    labels = Select_Total['RESTAURANTE'].tolist()                               # Buscando o tamanho da lista das strings do eixo x p/tratamento e apresentação
    labels = ['\n'.join(wrap(l, 12)) for l in labels]                           # A função wrap vai inserir um \n a cada 12 caracteres - (ajustando o tamanho)
    plt.xticks(range(len(labels)), labels, rotation=0, color=PRETO);            # plt.xticks usa o labels p/ajustar os nomes ao tamanho correto de cada barra do eixo x 
    #plt.gca().axes.get_yaxis().set_visible(False)                              # Remnovendo o eixo y
    #plt.gca().axes.get_xaxis().set_visible(False)                              # Remnovendo o eixo x
    #.set_axis_off()                                                            # Removendo todos os eixos juntos
                                    
    return (fig)

def Graphic_Arabian(df1):  
    """
    Esta função tem por responsabilidade apresentar os restaurantes de diversas culinárias com maior e menor média de avaliação, deatravés de um gráfico de barras. O mesmo     irá receber um dataframe e uma variável que definirá qual a culinária escolhida
    """
    # Definimos aqui os 5 restaurantes com notas máximas
    Select_Rest = df1.loc[(df1['Cuisines'] == 'Arabian'), ['Restaurant Name', 'Aggregate rating']]
    Select_Max = Select_Rest.loc[:,['Restaurant Name', 'Aggregate rating']].groupby (['Aggregate rating']).max().reset_index()  
    Select_Max = Select_Max.sort_values(by=['Aggregate rating'], ascending=False).head(3).reset_index(drop=True)
    Select_Max.columns = ['NOTA', 'RESTAURANTE']
    # Definimos aqui os 5 restaurantes com notas minimas
    Select_Min = Select_Rest.loc[:,['Restaurant Name', 'Aggregate rating']].groupby (['Aggregate rating']).min().reset_index()  
    Select_Min = Select_Min.sort_values(by=['Aggregate rating'], ascending=True).head(3).reset_index(drop=True)
    Select_Min.columns = ['NOTA', 'RESTAURANTE']
    # Fazenis aqui a união dos dois dataframes com a função pd.merge usando how='inner' para preservar todos os dados em duas planilhas similares
    Select_Total = pd.concat([Select_Min, Select_Max], ignore_index = True)   
    #Criando o gráfico
    fig, ax = plt.subplots(figsize=(15, 4))                                                  # Definindo o tamanho do gráfico                 
    ax.bar(Select_Total['RESTAURANTE'], Select_Total['NOTA'], color=Especial_3)               # Definindo as informações do eixo x e y e definindo as cores       
    plt.xlabel('RESTAURANTES', weight='bold')                                                # Destacando as informações trazidas pelos eixos x       
    plt.ylabel('AVALIAÇÕES', weight='bold')                                                  # Destacando as informações trazidas pelos eixos y      
    ax.spines['right'].set_visible(False)                                                    # Removendo grids e traços do lado direito
    ax.spines['left'].set_visible(False)                                                     # Removendo grids e traços do lado esquerdo       
    ax.spines['top'].set_visible(False)                                                      # Removendo grids e traços acima       
    #ax.spines['bottom'].set_visible(False)                                                  # Removendo grids e traços abaixo

    plt.text(x=1.20, y=6.3, s='RESTAURANTES DE CULINÁRIA ÁRABE', fontsize=16, color=AZULBB_5, weight='bold')         # Definindo o Título do Gráfico
    plt.text(x=4.30, y=5.3, s='MAIORES MÉDIAS DE AVALIAÇÃO', fontsize=8, color=AZULBB_5, weight='bold')              # Definindo informação das maiores médias
    plt.text(x=-0.50, y=5.3, s='MENORES MÉDIAS DE AVALIAÇÃO', fontsize=8, color=CINZA_4, weight='bold')              # Definindo informação das menores médias              

    labels = Select_Total['RESTAURANTE'].tolist()                               # Buscando o tamanho da lista das strings do eixo x p/tratamento e apresentação
    labels = ['\n'.join(wrap(l, 12)) for l in labels]                           # A função wrap vai inserir um \n a cada 12 caracteres - (ajustando o tamanho)
    plt.xticks(range(len(labels)), labels, rotation=0, color=PRETO);            # plt.xticks usa o labels p/ajustar os nomes ao tamanho correto de cada barra do eixo x 
    #plt.gca().axes.get_yaxis().set_visible(False)                              # Remnovendo o eixo y
    #plt.gca().axes.get_xaxis().set_visible(False)                              # Remnovendo o eixo x
    #.set_axis_off()                                                            # Removendo todos os eixos juntos
                                    
    return (fig)



def Graphic_Japanese(df1):  
    """
    Esta função tem por responsabilidade apresentar os restaurantes de diversas culinárias com maior e menor média de avaliação, deatravés de um gráfico de barras. O mesmo     irá receber um dataframe e uma variável que definirá qual a culinária escolhida
    """
    # Definimos aqui os 5 restaurantes com notas máximas
    Select_Rest = df1.loc[(df1['Cuisines'] == 'Japanese'), ['Restaurant Name', 'Aggregate rating']]
    Select_Max = Select_Rest.loc[:,['Restaurant Name', 'Aggregate rating']].groupby (['Aggregate rating']).max().reset_index()  
    Select_Max = Select_Max.sort_values(by=['Aggregate rating'], ascending=False).head(5).reset_index(drop=True)
    Select_Max.columns = ['NOTA', 'RESTAURANTE']
    # Definimos aqui os 5 restaurantes com notas minimas
    Select_Min = Select_Rest.loc[:,['Restaurant Name', 'Aggregate rating']].groupby (['Aggregate rating']).min().reset_index()  
    Select_Min = Select_Min.sort_values(by=['Aggregate rating'], ascending=True).head(5).reset_index(drop=True)
    Select_Min.columns = ['NOTA', 'RESTAURANTE']
    # Fazenis aqui a união dos dois dataframes com a função pd.merge usando how='inner' para preservar todos os dados em duas planilhas similares
    Select_Total = pd.concat([Select_Min, Select_Max], ignore_index = True)   
    #Criando o gráfico
    fig, ax = plt.subplots(figsize=(15, 4))                                                  # Definindo o tamanho do gráfico                 
    ax.bar(Select_Total['RESTAURANTE'], Select_Total['NOTA'], color=CinLaranj)               # Definindo as informações do eixo x e y e definindo as cores       
    plt.xlabel('RESTAURANTES', weight='bold')                                                # Destacando as informações trazidas pelos eixos x       
    plt.ylabel('AVALIAÇÕES', weight='bold')                                                  # Destacando as informações trazidas pelos eixos y      
    ax.spines['right'].set_visible(False)                                                    # Removendo grids e traços do lado direito
    ax.spines['left'].set_visible(False)                                                     # Removendo grids e traços do lado esquerdo       
    ax.spines['top'].set_visible(False)                                                      # Removendo grids e traços acima       
    #ax.spines['bottom'].set_visible(False)                                                  # Removendo grids e traços abaixo
    
    plt.text(x=2.00, y=6.3, s='RESTAURANTES DE CULINÁRIA JAPONESA', fontsize=16, color=CINZA_3, weight='bold')       # Definindo o Título do Gráfico
    plt.text(x=7.50, y=5.3, s='MAIORES MÉDIAS DE AVALIAÇÃO', fontsize=8, color=LARANJA_4, weight='bold')             # Definindo informação das maiores médias
    plt.text(x=-0.70, y=5.3, s='MENORES MÉDIAS DE AVALIAÇÃO', fontsize=8, color=CINZA_4, weight='bold')              # Definindo informação das menores médias 
    
    labels = Select_Total['RESTAURANTE'].tolist()                               # Buscando o tamanho da lista das strings do eixo x p/tratamento e apresentação
    labels = ['\n'.join(wrap(l, 12)) for l in labels]                           # A função wrap vai inserir um \n a cada 12 caracteres - (ajustando o tamanho)
    plt.xticks(range(len(labels)), labels, rotation=0, color=PRETO);            # plt.xticks usa o labels p/ajustar os nomes ao tamanho correto de cada barra do eixo x 
    #plt.gca().axes.get_yaxis().set_visible(False)                              # Remnovendo o eixo y
    #plt.gca().axes.get_xaxis().set_visible(False)                              # Remnovendo o eixo x
    #.set_axis_off()                                                            # Removendo todos os eixos juntos
                                    
    return (fig)


def Graphic_Caseira(df1):  
    """
    Esta função tem por responsabilidade apresentar os restaurantes de diversas culinárias com maior e menor média de avaliação, deatravés de um gráfico de barras. O mesmo     irá receber um dataframe e uma variável que definirá qual a culinária escolhida
    """
    # Definimos aqui os 5 restaurantes com notas máximas
    Select_Rest = (df1.loc[(df1['Restaurant ID'] == 6007184) | (df1['Restaurant ID'] == 5904119) | (df1['Restaurant ID'] == 18442162) | 
                  (df1['Restaurant ID'] == 18286221) | (df1['Restaurant ID'] == 5914190), ['Cuisines', 'Restaurant Name', 'Aggregate rating']] )
    Select_Max = Select_Rest.loc[:,['Restaurant Name', 'Aggregate rating']].groupby (['Aggregate rating']).max().reset_index()  
    Select_Max = Select_Max.sort_values(by=['Aggregate rating'], ascending=False).head(2).reset_index(drop=True)
    Select_Max.columns = ['NOTA', 'RESTAURANTE']
    # Definimos aqui os 5 restaurantes com notas minimas
    Select_Min = Select_Rest.loc[:,['Restaurant Name', 'Aggregate rating']].groupby (['Aggregate rating']).min().reset_index()  
    Select_Min = Select_Min.sort_values(by=['Aggregate rating'], ascending=True).head(2).reset_index(drop=True)
    Select_Min.columns = ['NOTA', 'RESTAURANTE']
    # Fazenis aqui a união dos dois dataframes com a função pd.merge usando how='inner' para preservar todos os dados em duas planilhas similares
    Select_Total = pd.concat([Select_Min, Select_Max], ignore_index = True)   

    #Criando o gráfico
    fig, ax = plt.subplots(figsize=(15, 4))                                                  # Definindo o tamanho do gráfico                 
    ax.bar(Select_Total['RESTAURANTE'], Select_Total['NOTA'], color=Especial_2)              # Definindo as informações do eixo x e y e definindo as cores       
    plt.xlabel('RESTAURANTES', weight='bold')                                                # Destacando as informações trazidas pelos eixos x       
    plt.ylabel('AVALIAÇÕES', weight='bold')                                                  # Destacando as informações trazidas pelos eixos y      
    ax.spines['right'].set_visible(False)                                                    # Removendo grids e traços do lado direito
    ax.spines['left'].set_visible(False)                                                     # Removendo grids e traços do lado esquerdo       
    ax.spines['top'].set_visible(False)                                                      # Removendo grids e traços acima       
    #ax.spines['bottom'].set_visible(False)                                                  # Removendo grids e traços abaixo
    
    plt.text(x=0.60, y=6.3, s='RESTAURANTES DE CULINÁRIA CASEIRA', fontsize=16, color=VERMELHOCL_4, weight='bold')       # Definindo o Título do Gráfico
    plt.text(x=2.60, y=5.3, s='MAIORES MÉDIAS DE AVALIAÇÃO', fontsize=8, color=VERMELHO_5, weight='bold')                # Definindo informação das maiores médias
    plt.text(x=-0.30, y=5.3, s='MENORES MÉDIAS DE AVALIAÇÃO', fontsize=8, color=VERMELHO_3, weight='bold')               # Definindo informação das menores médias         

    labels = Select_Total['RESTAURANTE'].tolist()                               # Buscando o tamanho da lista das strings do eixo x p/tratamento e apresentação
    labels = ['\n'.join(wrap(l, 12)) for l in labels]                           # A função wrap vai inserir um \n a cada 12 caracteres - (ajustando o tamanho)
    plt.xticks(range(len(labels)), labels, rotation=0, color=PRETO);            # plt.xticks usa o labels p/ajustar os nomes ao tamanho correto de cada barra do eixo x 
    #plt.gca().axes.get_yaxis().set_visible(False)                              # Remnovendo o eixo y
    #plt.gca().axes.get_xaxis().set_visible(False)                              # Remnovendo o eixo x
    #.set_axis_off()                                                            # Removendo todos os eixos juntos
                                    
    return (fig)


#=========================================================================================================================================
#                                    INICIO DA ESTRUTURA LÓGICA DO CÓDIGO - CONSTRUINDO O STREAMLIT -  A VISÃO GERAL
#=========================================================================================================================================

# IMPORT DATASET 
df = pd.read_csv( 'dataset/zomato.csv' )
df1 = df

# CRIANDO COLUNA COLORS 
df1 = colors( df1 )

# CRIANDO COLUNA PAÍSES 
df1 = paises( df1 )

# CRIANDO COLUNA TIPOS DE PREÇO 
df1 = price_tye( df1 )


#=========================================================================================================================================
#                                                         CRIANDO A BARRA LATERAL (função sidebar) 
#=========================================================================================================================================

st.markdown('# MARKET PLACE - FOME ZERO')


# Anexando uma imagem ao meu sidebar (barra lateral) do layout
# A variável image_path receberá o caminho de onde meu arquivo alvo.jpg está (deve ser dentro da mesma pasta onde estão os demais arquivos
# A variável image receberá a função Image.open abrindo o arquivo guardado na variável acima
# st.sidebar.image é a função que receberá o arquivo aberto e o tamanho dele (width) e executará o processo

image_path = 'logo.jpg'                                    
image = Image.open( image_path )
st.sidebar.image( image, width=220 )


#  CRIANDO BOTÕES NA LATERAL DO LAYOUT USANDO 'sidebar.markdown' ----------------------------------------------------------------------------------------

st.sidebar.markdown( '# Zero Hunger' )
st.sidebar.markdown( '### The place where customers and restaurants meet' )
st.sidebar.markdown( """---""" )                              # A função st.sidebar.markdown("""---""") vai determinar uma linha de separação
#st.dataframe( df1 )                                          # Para vermos o df1 dentro do streamlit usamos st.dataframe e definimos df1 como variável



#=========================================================================================================================================
#                                                       CRIANDO O CORPO DO STREAMLIT (função sidebar)
#=========================================================================================================================================

# CRIANDO ABAS NO CORPO PRINCIPAL DA TELA DO MEU STREAMLIT -------------------------------------------------------------------------------

#a função st.tabs criará as abas passadas através de uma lista, os nomes das tags que queremos criar
tab1 = st.tabs( ['CULINÁRIA'] )

st.header( 'INFORMAÇÕES - CULINÁRIA' )
st.markdown( """---""" )
    
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs( ['ITALIANA', 'AMERICANA', 'ÁRABE', 'JAPONESA' , 'CASEIRA', 'OUTRAS INFORMAÇÕES'] )
    
with tab1:
    with st.container():
        st.markdown('####  CULINÁRIA ITALIANA')
        st.markdown('#####  Restaurantes com maior e menor média de avaliação')
        culinaria = 'Italian'
        Select_Total = Select_Rest(df1, culinaria)
        st.dataframe(Select_Total, width=900, height=212, use_container_width=True) 
            
    with st.container():        
        st.markdown('##### Gráfico de Avaliações')   
        fig = Graphic_Italian(df1)
        st.pyplot(fig)
                
with tab2:
    with st.container():
        st.markdown('####  CULINÁRIA AMERICANA')
        st.markdown('#####  Restaurantes com maior e menor média de avaliação')
        culinaria = 'American'
        Select_Total = Select_Rest(df1, culinaria)
        st.dataframe(Select_Total, width=900, height=212, use_container_width=True) 
                
    with st.container():        
        st.markdown('##### Gráfico de Avaliações')   
        fig = Graphic_American(df1)
        st.pyplot(fig)      
            
with tab3:
    with st.container():
        st.markdown('####  CULINÁRIA ÁRABE')
        st.markdown('#####  Restaurantes com maior e menor média de avaliação')
        culinaria = 'Arabian'
        Select_Total = Select_Rest_Two(df1, culinaria)
        st.dataframe(Select_Total, width=900, height=144, use_container_width=True) 
                
    with st.container():        
        st.markdown('##### Gráfico de Avaliações')   
        fig = Graphic_Arabian(df1)
        st.pyplot(fig)     
                
with tab4:
    with st.container():
        st.markdown('####  CULINÁRIA JAPONESA')
        st.markdown('#####  Restaurantes com maior e menor média de avaliação')
        culinaria = 'Japanese'
        Select_Total = Select_Rest(df1, culinaria)
        st.dataframe(Select_Total, width=900, height=213, use_container_width=True) 
                
    with st.container():        
        st.markdown('##### Gráfico de Avaliações')   
        fig = Graphic_Japanese(df1)
        st.pyplot(fig)  
                   
with tab5:
    with st.container():
        st.markdown('####  CULINÁRIA CASEIRA')
        st.markdown('#####  Restaurantes com maior e menor média de avaliação')
        Select_Total = Select_Rest_Three(df1)
        st.dataframe(Select_Total, width=900, height=106, use_container_width=True) 
                
    with st.container():        
        st.markdown('##### Gráfico de Avaliações')   
        fig = Graphic_Caseira(df1)
        st.pyplot(fig)  
            
with tab6:
    st.markdown('###  OUTRAS INFORMAÇÕES')
    with st.container():
        col1, col2 = st.columns(2, gap='small')
            
        with col1:
            st.markdown('###### OS DEZ MAIORES VALORES MÉDIOS - (prato para duas pessoas)')
            Cuisines_Top = Select_Topten_Cuisines(df1)
            st.dataframe(Cuisines_Top, width=480, height=390, use_container_width=True)
                
        with col2:
            st.markdown('######  AS DEZ MAIORES NOTAS MÉDIAS - (por tipo de prato)')
            Cuisines_Top = Select_Topten_Mean(df1)
            st.dataframe(Cuisines_Top, width=480, height=390, use_container_width=True)
    st.markdown( """---""" )
                
    with st.container():   
        st.markdown('######  OS DEZ TIPOS DE PRATO QUE POSSUEM MAIS RESTAURANTES QUE ACEITAM PEDIDOS ON LINE E FAZEM ENTREGAS')
        Cuisines_Top = CuisinesTop_TenDelivery(df1)
        st.dataframe(Cuisines_Top, width=480, height=390, use_container_width=True)
                
    with st.container():
        st.markdown('###### GRAFICO ANALITICO ESTATISTICO (%)') 
        fig = Graphic_Statistic(df1) 
        st.plotly_chart(fig)
        
st.markdown( """---""" )
