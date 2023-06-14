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
st.set_page_config( page_title='Visão Cidades', layout='wide')    

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


def RestCity_MostRegistered(df1):
    """
    Esta função tem por responsabilidade apresentar as cidades com mais restaurantes registrados, através de um dataframe
    """
    RestCity_MostRegistered = df1.loc[:, ['City','Countries', 'Restaurant ID']].groupby (['Countries', 'City']).nunique().reset_index()
    RestCity_MostRegistered = (RestCity_MostRegistered.loc[:, ['City', 'Countries', 'Restaurant ID']]                                                                                                           .groupby (['Restaurant ID'])
                                                      .max()
                                                      .reset_index())  
    RestCity_MostRegistered.columns = ['QUANTIDADE', 'CIDADE', 'PAIS']
    RestCity_MostRegistered = RestCity_MostRegistered.sort_values(by=['QUANTIDADE'], ascending=False).head(4).reset_index(drop=True)
            
    return (RestCity_MostRegistered)    


def City_NoteBelow_2_5(df1):
    """
    Esta função tem por responsabilidade apresentar as cidades com mais restaurantes com nota média abaixo de 2,5, através de um dataframe
    """
    City_NoteBelow_2_5 = df1.loc[df1['Aggregate rating'] < 2.5, ['Restaurant ID', 'City', 'Countries', 'Aggregate rating']]
    City_NoteBelow_2_5 = (City_NoteBelow_2_5.loc[:, ['City', 'Countries', 'Restaurant ID', 'Aggregate rating']]
                                            .groupby (['Countries', 'City', 'Aggregate rating']).nunique().reset_index())
    City_NoteBelow_2_5 = (City_NoteBelow_2_5.loc[:, ['City', 'Countries', 'Restaurant ID']]
                                            .groupby (['Restaurant ID']).max().reset_index())
    City_NoteBelow_2_5.columns = ['QUANTIDADE', 'CIDADE', 'PAIS']
    City_NoteBelow_2_5 = City_NoteBelow_2_5.sort_values(by=['QUANTIDADE'], ascending=False).head(4).reset_index(drop=True)

    return(City_NoteBelow_2_5)    


def City_NoteBelow_4(df1):
    """
    Esta função tem por responsabilidade apresentar as cidades com mais restaurantes com nota média acima de 4, através de um dataframe
    """
    City_NoteBelow_4 = df1.loc[df1['Aggregate rating'] > 4, ['Restaurant ID', 'Countries', 'City', 'Aggregate rating']]
    City_NoteBelow_4 = (City_NoteBelow_4.loc[:, ['City', 'Countries', 'Restaurant ID', 'Aggregate rating']]
                                        .groupby (['Countries', 'City', 'Aggregate rating']).nunique().reset_index())
    City_NoteBelow_4 = (City_NoteBelow_4.loc[:, ['City', 'Countries', 'Restaurant ID']]
                                        .groupby (['Restaurant ID']).max().tail(4).reset_index())
    City_NoteBelow_4.columns = ['QUANTIDADE', 'CIDADE', 'PAIS']
    City_NoteBelow_4 = City_NoteBelow_4.sort_values(by=['QUANTIDADE'], ascending=False).head(4).reset_index(drop=True)

    return(City_NoteBelow_4)    


def BigPrice_AverageTwo(df1):   
    """
    Esta função tem por responsabilidade apresentar as cidades com o prato para dois mais caro, através de um dataframe
    """
    BigPrice_AverageTwo = (df1.loc[:, ['City', 'Countries', 'Average Cost for two']]
                              .groupby (['City', 'Countries']).mean().reset_index())
    BigPrice_AverageMax = (np.round(BigPrice_AverageTwo.loc[:, ['City', 'Countries', 'Average Cost for two']]
                              .groupby (['Average Cost for two']).max().tail(4).reset_index(), 2))
    
    BigPrice_AverageMax.columns = ['CUSTO', 'CIDADE', 'PAIS']
    BigPrice_AverageMax = BigPrice_AverageMax.sort_values(by=['CUSTO'], ascending=False).head(4).reset_index(drop=True)
    
    return (BigPrice_AverageMax)
                

def CityHas_Table(df1):  
    """
    Esta função tem por responsabilidade apresentar as cidades que mais fazem reservas, através de um grafico de linhas
    """
    CityHas_Table = df1.loc[df1['Has Table booking'] == 1, ['Countries', 'City', 'Restaurant ID', 'Has Table booking']]
    CityHas_Table = CityHas_Table.loc[:, ['City', 'Countries', 'Restaurant ID']].groupby (['Countries', 'City']).nunique().reset_index()
    CityHas_Table = CityHas_Table.loc[:, ['City', 'Countries', 'Restaurant ID']].groupby (['Restaurant ID']).max().reset_index()    
    CityHas_Table.columns = ['QUANTIDADE', 'CIDADE', 'PAIS']
    CityHas_Table = CityHas_Table.sort_values(by=['QUANTIDADE', 'CIDADE'], ascending=True).tail(10).reset_index(drop=True)
    
    return (CityHas_Table)

def City_Cuisines(df1): 
    """
    Esta função tem por responsabilidade apresentar as cidades que mais possuem pratos culinários distintos, através de um gráfico de barras
    """
    City_Cuisines = df1.loc[:, ['City', 'Cuisines', 'Countries']].groupby (['Countries','City']).nunique().reset_index()
    City_Cuisines = City_Cuisines.loc[:, ['City', 'Countries', 'Cuisines']].groupby (['Cuisines']).max().reset_index()
    City_Cuisines.columns = ['PRATOS', 'CIDADE', 'PAIS']
    City_Cuisines = City_Cuisines.sort_values(by=['PRATOS'], ascending=False).head(4).reset_index(drop=True)
    
    return (City_Cuisines)
    
def CityDelivery_Now(df1):
    """
    Esta função tem por responsabilidade apresentar as cidades com mais restaurantes que fazem entregas, através de um gráfico de barras
    """
    CityDelivery_Now = df1.loc[df1['Is delivering now'] == 1, ['Countries', 'City', 'Restaurant ID', 'Is delivering now']]
    CityDelivery_Now = CityDelivery_Now.loc[:, ['City', 'Countries', 'Restaurant ID']].groupby (['Countries', 'City']).nunique().reset_index()
    CityDelivery_Now = CityDelivery_Now.loc[:, ['City', 'Countries', 'Restaurant ID']].groupby (['Restaurant ID']).max().tail(5).reset_index()
    CityDelivery_Now.columns = ['QUANTIDADE', 'CIDADE', 'PAIS']
    CityDelivery_Now = CityDelivery_Now.sort_values(by=['QUANTIDADE'], ascending=False).head(4).reset_index(drop=True)
    
    return (CityDelivery_Now)            
    

def CityBigger_Delivery(df1):
    """
    Esta função tem por responsabilidade apresentar as cidades com mais restaurantes que aceitam pedidos on-line, através de um gráfico de barras
    """
    CityBigger_Delivery = df1.loc[df1['Has Online delivery'] == 1, ['Countries', 'City', 'Restaurant ID', 'Has Online delivery']]
    CityBigger_Delivery = (CityBigger_Delivery.loc[:, ['City', 'Countries', 'Restaurant ID', 'Has Online delivery']]
                                              .groupby (['Countries', 'City']).nunique().reset_index())
    CityBigger_Delivery = (CityBigger_Delivery.loc[:, ['City', 'Countries', 'Restaurant ID']]
                                              .groupby (['Restaurant ID']).max().tail(5).reset_index())    
    CityBigger_Delivery.columns = ['QUANTIDADE', 'CIDADE', 'PAIS']
    CityBigger_Delivery =  CityBigger_Delivery.sort_values(by=['QUANTIDADE'], ascending=False).head(4).reset_index(drop=True)
    
    return (CityBigger_Delivery)            
    
    
    
    

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
tab1 = st.tabs( ['CIDADES'] )

st.header( 'INFORMAÇÕES - CIDADES' )
st.markdown( """---""" )
    
with st.container():
        
    with st.container():
        col1, col2 = st.columns(2, gap='small')          
 
        with col1:
            st.markdown('###### COM MAIOR VALOR MÉDIO PRATO PARA 2')  
            BigPrice_AverageTwo = BigPrice_AverageTwo(df1)
            st.dataframe(BigPrice_AverageTwo, width=353, height=178, use_container_width=False)
              
        with col2:
            st.markdown('###### COM MAIS RESTAURANTES NOTA MÉDIA ACIMA 4')
            City_NoteBelow_4 = City_NoteBelow_4(df1)
            st.dataframe(City_NoteBelow_4, width=434, height=178, use_container_width=False)
    
with st.container():
        col1, col2 = st.columns(2, gap='small') 
            
        with col1:
            st.markdown('###### COM MAIS RESTAURANTES NOTA MÉDIA ABAIXO 2,5')
            City_NoteBelow_2_5 = City_NoteBelow_2_5(df1)
            st.dataframe(City_NoteBelow_2_5, width=353, height=178, use_container_width=False)
              
        with col2:
            st.markdown('###### COM MAIOR NÚMERO DE RESTAURANTES REGISTRADOS')
            RestCity_MostRegistered = RestCity_MostRegistered(df1)
            st.dataframe(RestCity_MostRegistered, width=434, height=178, use_container_width=False)
    
st.markdown( """---""" )
    
with st.container():
        st.markdown('##### COM MAIS RESTAURANTES QUE FAZEM RESERVAS')
        CityHas_Table = CityHas_Table(df1)
        fig = px.line(CityHas_Table, x='QUANTIDADE', y='CIDADE')
        st.plotly_chart( fig, use_container_width=True)
   
        st.markdown( """---""" )
    
with st.container():
    col1, col2 = st.columns(2, gap='small')         

    with col1:
        st.markdown('###### QUE POSSUEM MAIS TIPOS DE PRATOS DISTINTOS')
        City_Cuisines = City_Cuisines(df1)
        fig = px.bar(City_Cuisines, x='PRATOS', y='CIDADE', color='PAIS')                                   
        st.plotly_chart( fig, use_container_width=True )
            
    with col2:
        st.markdown('###### QUE POSSUEM MAIS RESTAURANTES QUE ENTREGAM')
        CityDelivery_Now = CityDelivery_Now(df1)
        fig = px.bar(CityDelivery_Now, x='CIDADE', y='QUANTIDADE', color='PAIS')                                   
        st.plotly_chart( fig, use_container_width=True )
            
st.markdown( """---""" )

with st.container():
    st.markdown('##### COM MAIS RESTAURANTES QUE ACEITAM PEDIDOS ON-LINE')
    CityBigger_Delivery = CityBigger_Delivery(df1)          
    fig = px.bar(CityBigger_Delivery, x='QUANTIDADE', y='CIDADE', color='PAIS')                                   
    st.plotly_chart( fig, use_container_width=True )
       
st.markdown( """---""" )    
    
    

     