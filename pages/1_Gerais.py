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


#  AJUSTANDO NOSSOS GRÁFICOS A ÁREA TOTAL DE NOSSOS CONTAINERS-------------------------------------------------------------------------------------------
#Aqui estamos expandindo apresentação de nossos gráfico a toda área de nosso container. 
st.set_page_config( page_title='Visão Geral', layout='wide')    

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

def Geo_Map_Color(df1): 
    """ 
        Esta função tem por responsabilidade retornar a localização dos restaurantes a partir de um gráfico de mapa por sua classificação de cores
    """ 
    AggregateRating_Max = (df1.loc[:, ['City', 'Restaurant ID', 'Restaurant Name', 'Rating color', 'Latitude', 'Longitude']]
                              .groupby (['Restaurant ID', 'Restaurant Name', 'Rating color', 'City'])
                              .mean()
                              .reset_index())
    AggregateRating_Max = AggregateRating_Max.head(700)
    map = folium.Map()
    for index, location_info in AggregateRating_Max.iterrows():
        folium.Marker( [location_info['Latitude'], location_info['Longitude']],
                        popup=location_info[['City', 'Restaurant Name']]).add_to( map )
    
    
    folium_static( map, width=1024, height=500 )
       
    return(map)    


#========================================================================================================================================================
#                                    INICIO DA ESTRUTURA LÓGICA DO CÓDIGO - CONSTRUINDO O STREAMLIT -  A VISÃO GERAL
#========================================================================================================================================================

# IMPORT DATASET 
df = pd.read_csv( 'dataset/zomato.csv' )
df1 = df

# CRIANDO COLUNA COLORS 
df1 = colors( df1 )

# CRIANDO COLUNA PAÍSES 
df1 = paises( df1 )

# CRIANDO COLUNA TIPOS DE PREÇO 
df1 = price_tye( df1 )


#========================================================================================================================================================
#                                                         CRIANDO A BARRA LATERAL (função sidebar) 
#======================================================================================================================================================== 

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


#========================================================================================================================================================
#                                                       CRIANDO O CORPO DO STREAMLIT (função sidebar)
#========================================================================================================================================================

# CRIANDO ABAS NO CORPO PRINCIPAL DA TELA DO MEU STREAMLIT ---------------------------------------------------------------------------------------------- 

#a função st.tabs criará as abas passadas através de uma lista, os nomes das tags que queremos criar
tab1 = st.tabs( ['GERAL'] )


with st.container():
    st.header( 'INFORMAÇÕES - GERAIS' )
    st.markdown( """---""" )
        
    col1, col2, col3, col4, col5 = st.columns(5, gap='large')          #Aqui defino que meu container terá 4 colunas. A distancia 'large'
      
    with col1:                                                         #Aqui definirei o que estará dentro da primeira coluna
        Rest_unique = df1['Restaurant ID'].nunique()
        st.markdown('##### RESTAURANTES')
        col1.metric('Registrados', Rest_unique)                 #col(x).metric irá apresentar o resultado recebido pela variávl max_age
       
    with col2:
        Countries_unique = df1['Country Code'].nunique()
        st.markdown('##### PAÍSES')
        col2.metric('Registrados', Countries_unique)
            
    with col3:
        Citys_unique = df1['City'].nunique()
        st.markdown('##### CIDADES')
        col3.metric('Resgistradas', Citys_unique)
            
    with col4:
        Total_ratings = df1['Votes'].sum()
        st.markdown('##### AVALIAÇÕES')
        col4.metric('Registradas',Total_ratings)
            
    with col5:
        Total_cuisines = df1['Cuisines'].nunique()
        st.markdown('##### PRATOS')
        col5.metric('Registrados',Total_cuisines)

st.markdown( """---""" )

with st.container():
    st.header( 'LOCALIZAÇÃO CENTRAL - Restaurantes por classificação' )
    map = Geo_Map_Color(df1)    
    map

st.markdown( """---""" )