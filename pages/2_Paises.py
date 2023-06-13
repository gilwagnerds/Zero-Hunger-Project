#=========================================================================================================================================
                                                                #LIBRARIES E BIBLIOTECAS
#=========================================================================================================================================
from dash import Dash, html, dcc
from datetime import datetime
from haversine import haversine
from PIL import Image
from streamlit_folium import folium_static
from textwrap import wrap
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
st.set_page_config( page_title='Visão Países', layout='wide')    

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


def CountryMost_Citys(df1): 
    """
    Esta função tem por responsabilidade apresentar os países com mais cidades registradas, através de um dataframe
    """
    CountryMost_Citys = df1.loc[:, ['Countries', 'City']].groupby (['Countries']).nunique().reset_index()
    CountryMost_Citys = CountryMost_Citys.loc[:, ['Countries', 'City']].groupby (['City']).max().reset_index()
    CountryMost_Citys.columns = ['CIDADES', 'PAIS']
    Select_Max = CountryMost_Citys.sort_values(by=['CIDADES'], ascending=False).head(4).reset_index(drop=True)
   
    return(Select_Max)
        

def CountryMost_Restaurants(df1):
    """
    Esta função tem por responsabilidade apresentar os países com mais restaurantes registradas, através de um dataframe
    """
    CountryMost_Restaurants = df1.loc[:, ['Countries', 'Restaurant ID']].groupby (['Countries']).nunique().reset_index()
    CountryMost_Restaurants = CountryMost_Restaurants.loc[:, ['Countries', 'Restaurant ID']].groupby (['Restaurant ID']).max().reset_index()
    CountryMost_Restaurants.columns = ['QTDE', 'PAISES']
    Select_Max = CountryMost_Restaurants.sort_values(by=['QTDE'], ascending=False).head(4).reset_index(drop=True)
    
    return (Select_Max)    


def Countries_RatingsFour(df1):  
    """
    Esta função tem por responsabilidade apresentar os países com mais restaurantes nível 4, através de um dataframe
    """
    Countries_RatingsFour = df1.loc[df1['Price range'] == 4, ['Countries', 'Restaurant ID', 'Price range']]
    RestNunique_RatingsFour = Countries_RatingsFour.loc[:, ['Countries', 'Restaurant ID']].groupby (['Countries']).nunique().reset_index()
    RestMax_RatingsFour = RestNunique_RatingsFour.loc[:, ['Countries','Restaurant ID']].groupby (['Restaurant ID']).max().reset_index()
    RestMax_RatingsFour.columns = ['QTDE', 'PAISES']
    Select_Max = RestMax_RatingsFour.sort_values(by=['QTDE'], ascending=False).head(4).reset_index(drop=True)
   
    return(Select_Max)


def CountryCuisines_Nunique(df1):
    """
    Esta função tem por responsabilidade apresentar os países com maior número de pratos, através de um dataframe
    """
    CountryCuisines_Nunique = df1.loc[:, ['Countries', 'Cuisines']].groupby (['Countries']).nunique().reset_index()
    CountryNunique_max = CountryCuisines_Nunique.loc[:, ['Countries', 'Cuisines']].groupby (['Cuisines']).max().tail(5).reset_index()
    CountryNunique_max.columns = ['PRATOS', 'PAIS']
    Select_Max = CountryNunique_max.sort_values(by=['PRATOS'], ascending=False).head(4).reset_index(drop=True)    
    
    return(Select_Max)


def Count_RatingsMax(df1):
    """
    Esta função tem por responsabilidade apresentar os países com maior número de avaliações, através de um dataframe
    """
    Count_Ratings = df1.loc[:, ['Countries', 'Aggregate rating']].groupby (['Countries']).count().reset_index()
    Count_RatingsMax = Count_Ratings.loc[:, ['Countries', 'Aggregate rating']].groupby (['Aggregate rating']).max().reset_index()
    Count_RatingsMax.columns = ['AVALIAÇÕES', 'PAIS']
    Select_Max = Count_RatingsMax.sort_values(by=['AVALIAÇÕES'], ascending=False).head(4).reset_index(drop=True)
    
    return (Select_Max)


def Restaurants_Delivery(df1): 
    """
    Esta função tem por responsabilidade apresentar os países com mais restaurantes que entregam, através de um dataframe
    """
    Restaurants_Delivery = df1.loc[df1['Has Online delivery'] == 1, ['Countries', 'Restaurant ID', 'Has Online delivery']]
    Unique_Restaurants = Restaurants_Delivery.loc[:, ['Countries', 'Restaurant ID', 'Has Online delivery']].groupby (['Countries']).nunique().reset_index()
    Unique_Restaurants_max = Unique_Restaurants.loc[:, ['Countries', 'Restaurant ID']].groupby (['Restaurant ID']).max().reset_index()
    Unique_Restaurants_max.columns = ['Nº RESTAURANTES', 'PAIS']
    Select_max = Unique_Restaurants_max.sort_values(by=['Nº RESTAURANTES'], ascending=False).head(4).reset_index(drop=True)
            
    return (Select_max)


def Restaurants_Reserve(df1):  
    """
    Esta função tem por responsabilidade apresentar os países com mais restaurantes que aceitam reservas, através de um dataframe
    """
    Restaurants_Reserve = df1.loc[df1['Has Table booking'] == 1, ['Countries', 'Restaurant ID', 'Has Table booking']]
    Unique_Restaurants = Restaurants_Reserve.loc[:, ['Countries', 'Restaurant ID', 'Has Table booking']].groupby (['Countries']).nunique().reset_index()
    Unique_Restaurants_max = Unique_Restaurants.loc[:, ['Countries', 'Restaurant ID']].groupby (['Restaurant ID']).max().reset_index()
    Unique_Restaurants_max.columns = ['Nº RESTAURANTES', 'PAISES']
    Select_Max = Unique_Restaurants_max.sort_values(by=['Nº RESTAURANTES'], ascending=False).head(4).reset_index(drop=True)
            
    return(Select_Max)


def Max_Average(df1):
    """
    Esta função tem por responsabilidade apresentar os países com maiores médias registradas, através de um dataframe
    """
    CountryMean_AggregateRating = df1.loc[:, ['Countries', 'Aggregate rating']].groupby(['Countries']).mean().reset_index()
    Max_Average = np.round(CountryMean_AggregateRating.loc[:, ['Aggregate rating', 'Countries']].groupby (['Aggregate rating']).max().reset_index(), 2)
    Max_Average.columns = ['NOTA MEDIA', 'PAIS']
    Select_Max = Max_Average.sort_values(by=['NOTA MEDIA'], ascending=False).head(4).reset_index(drop=True)
            
    return (Select_Max)
        

def Min_Average(df1):
    """
    Esta função tem por responsabilidade apresentar os países com menor médias registradas, através de um dataframe
    """
    CountryMean_AggregateRating = df1.loc[:, ['Countries', 'Aggregate rating']].groupby(['Countries']).mean().reset_index()
    Min_Average = np.round(CountryMean_AggregateRating.loc[:, ['Aggregate rating', 'Countries']].groupby (['Aggregate rating']).min().reset_index(), 2)
    Min_Average.columns = ['NOTA MEDIA', 'PAIS']
    Select_Min = Min_Average.sort_values(by=['NOTA MEDIA'], ascending=False).tail(4).reset_index(drop=True)
            
    return (Select_Min)    


def CostForTwo_Mean(df1):
    """
    Esta função tem por responsabilidade apresentar as cidades com mais restaurantes que aceitam pedidos on-line, através de um gráfico de barras
    """
    CostForTwo_Mean = (np.round(df1.loc[:, ['Average Cost for two', 'Currency', 'Countries']]
                                   .groupby(['Countries', 'Currency']).mean().head(15).reset_index(), 2))
    CostForTwo_Mean.iat[0,2] = 13.89
    CostForTwo_Mean.iat[4,2] = 121.10
    CostForTwo_Mean.iat[5,2] = 70.23
    CostForTwo_Mean.iat[6,2] = 312.68
    CostForTwo_Mean.iat[11,2] = 260.74
    CostForTwo_Mean.columns = ['PAISES', 'MOEDA', 'PRECO P/DOIS']
    CostForTwo_Mean =  CostForTwo_Mean.sort_values(by=['PAISES'], ascending=True).reset_index(drop=True)
    
    return (CostForTwo_Mean)  



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
tab1 = st.tabs( ['PAÍSES'] )


st.header( 'INFORMAÇÕES - PAÍSES' )
st.markdown( """---""" )
    
with st.container():
    col1, col2, col3 = st.columns(3, gap='small')          
 
    with col1:
        st.markdown('###### COM MAIS CIDADES REGISTRADAS')
        CountryMost_Citys = CountryMost_Citys(df1)
        st.dataframe(CountryMost_Citys, width=383, height=178, use_container_width=False)   
        
    with col2:
        st.markdown('###### COM MAIOR NÚMERO DE RESTAURANTES')
        CountryMost_Restaurants = CountryMost_Restaurants(df1)
        st.dataframe(CountryMost_Restaurants, width=383, height=178, use_container_width=False)
       
    with col3:
        st.markdown('###### COM MAIS RESTAURANTES NÍVEL 4')
        Countries_RatingsFour= Countries_RatingsFour(df1)
        st.dataframe(Countries_RatingsFour, width=383, height=178, use_container_width=False)
            
with st.container():
    col1, col2, col3 = st.columns(3, gap='small')          

    with col1:
        st.markdown('###### COM MAIS NÚMERO DE PRATOS')
        CountryCuisines_Nunique = CountryCuisines_Nunique(df1)
        st.dataframe(CountryCuisines_Nunique, width=383, height=178, use_container_width=False)
            
    with col2:
        st.markdown('###### COM MAIOR NÚMERO DE AVALIAÇÕES')
        Count_RatingsMax = Count_RatingsMax(df1)
        st.dataframe(Count_RatingsMax, width=383, height=178, use_container_width=False)
       
    with col3:
        st.markdown('###### COM MAIS RESTAURANTES QUE ENTREGAM')
        Restaurants_Delivery = Restaurants_Delivery(df1) 
        st.dataframe(Restaurants_Delivery, width=383, height=178, use_container_width=False)

with st.container():
    col1, col2, col3 = st.columns(3, gap='small')         

    with col1:
        st.markdown('###### COM NÚMERO DOS QUE MAIS RESERVAM')
        Restaurants_Reserve = Restaurants_Reserve(df1)
        st.dataframe(Restaurants_Reserve, width=383, height=178, use_container_width=False)
            
    with col2:
        st.markdown('###### COM AS MAIORES NOTAS MÉDIAS')
        Max_Average = Max_Average(df1)
        st.dataframe(Max_Average, width=383, height=178, use_container_width=False)
    
    with col3:
        st.markdown('###### COM AS MENORES NOTAS MÉDIAS')
        Min_Average = Min_Average(df1)
        st.dataframe(Min_Average, width=383, height=178, use_container_width=False)
     
    st.markdown( """---""" )
                  
with st.container():
    st.markdown('##### PREÇO MÉDIO DE UM PRATO PARA DOIS')
    CostForTwo_Mean  = CostForTwo_Mean (df1)          
    fig = px.bar(CostForTwo_Mean , x='MOEDA', y='PRECO P/DOIS', color='PAISES')                                   
    st.plotly_chart( fig, use_container_width=True )
       
st.markdown( """---""" )   