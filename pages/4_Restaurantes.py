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
st.set_page_config( page_title='Visão Restaurantes', layout='wide')    

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


def MaxAggregate_Rating(df1):   
    """
    Esta função tem por responsabilidade apresentar os restaurantes com maior quantidade de avaliações, através de um dataframe
    """
    MaxAggregate_Rating = (df1.loc[:, ['Restaurant ID', 'Restaurant Name', 'Aggregate rating', 'Countries']]
                              .groupby (['Restaurant ID', 'Restaurant Name', 'Countries']).count().reset_index())
    MaxAggregate_Rating = (MaxAggregate_Rating.loc[:, ['Restaurant Name', 'Aggregate rating', 'Countries']]
                                              .groupby (['Aggregate rating', 'Restaurant Name']).max().reset_index())
    MaxAggregate_Rating.columns = ['QUANTIDADE', 'RESTAURANTE', 'PAIS']
    MaxAggregate_Rating = MaxAggregate_Rating.sort_values(by=['QUANTIDADE'], ascending=False).head(4).reset_index(drop=True)

    return(MaxAggregate_Rating) 
    

def Cuisine_Orden(df1):
    """
    Esta função tem por responsabilidade apresentar os restaurantes com maior valor de um prato para dois, através de um dataframe
    """
    Select_Rest = df1.loc[(df1['Average Cost for two'] != 0), ['Restaurant Name', 'City', 'Countries', 'Average Cost for two']]
    Rest_Average_Two = (Select_Rest.loc[:, ['Restaurant Name', 'City', 'Countries', 'Average Cost for two']]
                                   .groupby (['Average Cost for two', 'Restaurant Name', 'City', 'Countries']).max().reset_index())
    Cuisine_Orden = Rest_Average_Two.sort_values(by=['Average Cost for two', 'Countries'], ascending=False).reset_index(drop=True)
    Cuisine_Orden.columns = ['CUSTO', 'RESTAURANTE', 'CIDADE', 'PAIS']
    Cuisine_Orden = Cuisine_Orden.sort_values(by=['CUSTO'], ascending=False).head(4).reset_index(drop=True)
    
    return(Cuisine_Orden)


def OrderRating_Max(df1): 
    """
    Esta função tem por responsabilidade apresentar os restaurantes com maior nota média de avaliação, através de um dataframe
    """
    OrderRating_Max = (df1.loc[:, ['Restaurant Name', 'City', 'Countries', 'Aggregate rating']]
                              .groupby (['Aggregate rating', 'Restaurant Name', 'City', 'Countries']).mean().reset_index())
    #OrderRating_Max = AggregateRating_Max.sort_values(by=['Aggregate rating', 'Restaurant Name'], ascending=False)
    OrderRating_Max.columns = ['NOTA', 'RESTAURANTE', 'CIDADE', 'PAIS']
    OrderRating_Max = OrderRating_Max.sort_values(by=['NOTA'], ascending=False).head(4).reset_index(drop=True)
            
    return (OrderRating_Max)    
    

def Rest_OnLine(df1):  
    """
    Esta função tem por responsabilidade apresentar os restaurantes que possuem mais avaliações e aceitam pedidos On-Line, através de um dataframe
    """
    Rest_OnLine = df1.loc[df1['Has Online delivery'] == 1, ['Restaurant Name', 'Has Online delivery', 'Aggregate rating', 'City', 'Countries']] 
    Rest_OnLine = (Rest_OnLine.loc[:, ['Restaurant Name', 'Aggregate rating', 'City', 'Countries']]
                              .groupby (['Aggregate rating', 'Restaurant Name', 'City', 'Countries']).count().reset_index())
    Rest_OnLine.columns = ['NOTA', 'RESTAURANTE', 'CIDADE', 'PAIS']
    Rest_OnLine = Rest_OnLine.sort_values(by=['NOTA', 'RESTAURANTE'], ascending=False).head(4).reset_index(drop=True)
    
    return (Rest_OnLine)


def Cuisine_BR(df1):
    """
    Esta função tem por responsabilidade apresentar os restaurantes de culinária brasileira com menor nota de avaliação, através de um dataframe
    """
    Cuisine_BR = (df1.loc[(df1['Cuisines'] == 'Brazilian') & (df1['Countries'] == 'Brazil'), 
                              ['Countries', 'Cuisines', 'City', 'Aggregate rating', 'Restaurant Name']])
    Cuisine_BR = (Cuisine_BR.loc[:, ['Restaurant Name', 'City', 'Aggregate rating', 'Countries']]
                            .groupby (['Aggregate rating', 'Restaurant Name', 'City', 'Countries']).mean().reset_index())
    Cuisine_BR.columns = ['NOTA', 'RESTAURANTE', 'CIDADE', 'PAIS']
    Cuisine_BR = Cuisine_BR.sort_values(by=['NOTA'], ascending=True).head(4).reset_index(drop=True)
    
    return Cuisine_BR


def Cuisine_BR2(df1):
    """
    Esta função tem por responsabilidade apresentar os restaurantes de culinária brasileira com maior nota de avaliação, através de um gráfico de barras
    """
    Cuisine_BR2 = (df1.loc[(df1['Cuisines'] == 'Brazilian') & (df1['Countries'] == 'Brazil'), 
                               ['Countries', 'Cuisines', 'City', 'Aggregate rating', 'Restaurant Name']])
    Cuisine_BR2 = (Cuisine_BR2.loc[:, ['Restaurant Name', 'City', 'Aggregate rating', 'Countries']]
                              .groupby (['Aggregate rating', 'Restaurant Name', 'City', 'Countries']).mean().reset_index())
    Cuisine_BR2.columns = ['NOTA', 'RESTAURANTE', 'CIDADE', 'PAIS']
    Cuisine_BR2 = Cuisine_BR2.sort_values(by=['NOTA', 'RESTAURANTE'], ascending=False).head(4).reset_index(drop=True)
    cores = ['green', 'blue', 'yellow', 'red']
    fig = px.bar(Cuisine_BR2, x='NOTA', y='RESTAURANTE', color=cores, orientation='h', width=950)
                 
    return (fig)


def Reserve_On(df1):
    """
    Esta função tem por responsabilidade apresentar os restaurantes que possuem maior preço médio de um prato para dois e fazem reserva, através de um gráfico de barras
    """
    Reserve_On = df1.loc[(df1['Has Table booking'] == 1), ['Restaurant Name', 'Countries', 'Average Cost for two']]
    Reserve_Mean = Reserve_On.loc[:, ['Restaurant Name', 'Countries', 'Average Cost for two']].groupby (['Countries', 'Restaurant Name']).mean().reset_index()
    Reserve_Max = Reserve_Mean.loc[:, ['Restaurant Name', 'Countries', 'Average Cost for two']].groupby (['Average Cost for two']).max().tail(15).reset_index()
    Reserve_Max.columns = ['CUSTO', 'RESTAURANTE', 'PAIS']
    Reserve_Max = Reserve_Max.sort_values(by=['CUSTO'], ascending=False).head(4).reset_index(drop=True)
    cores = ['green', 'blue', 'yellow', 'red']
    fig = px.bar(Reserve_Max, x='RESTAURANTE', y='CUSTO', color=cores, orientation='v', width=950)
    
    return (fig)
    

def UsaJapanese_Average(df1):            
    """
    Esta função tem por responsabilidade apresentar os restaurantes americanos (culinária japonesa) com prato pra dois de valor médio maior que as churrascarias(BBQ)
    """
    UsaJapanese_Average = (df1.loc[(df1['Cuisines'] == 'Japanese') & (df1['Countries'] == 'United States of America'), 
                                  ['Average Cost for two', 'Restaurant Name', 'Cuisines']])
    UsaJapanese_AverageNunique = (UsaJapanese_Average.loc[:, ['Average Cost for two', 'Restaurant Name', 'Cuisines']]
                                                     .groupby (['Average Cost for two', 'Restaurant Name', 'Cuisines']).nunique().reset_index())
    UsaJapanese_AverageMean = np.round(UsaJapanese_AverageNunique['Average Cost for two'].mean(), 2)
      
    return(UsaJapanese_AverageMean)
    
    
def Usa_Mean_AverageNunique(df1):            
    """
    Esta função tem por responsabilidade apresentar os restaurantes americanos (culinária japonesa) com prato pra dois de valor médio maior que as churrascarias(BBQ)
    """
    UsaJapanese_Average = (df1.loc[(df1['Cuisines'] == 'Japanese') & (df1['Countries'] == 'United States of America'), 
                                  ['Average Cost for two', 'Restaurant Name', 'Cuisines']])
    UsaJapanese_AverageNunique = (UsaJapanese_Average.loc[:, ['Average Cost for two', 'Restaurant Name', 'Cuisines']]
                                                     .groupby (['Average Cost for two', 'Restaurant Name', 'Cuisines']).nunique().reset_index())
    UsaJapanese_AverageMean = np.round(UsaJapanese_AverageNunique['Average Cost for two'].mean(), 2)
    
    Usa_Mean_Average = (df1.loc[(df1['Cuisines'] == 'BBQ') & (df1['Countries'] == 'United States of America'), 
                               ['Restaurant Name', 'Cuisines', 'Countries', 'Average Cost for two', 'Currency']])
    Usa_Mean_AverageNunique =( Usa_Mean_Average.loc[:, ['Restaurant Name', 'Cuisines', 'Average Cost for two', 'Currency']]
                                               .groupby (['Average Cost for two', 'Restaurant Name', 'Cuisines', 'Currency']).nunique().reset_index())
    
    valores_procurados = (Usa_Mean_AverageNunique.loc[(Usa_Mean_AverageNunique['Average Cost for two'] <= UsaJapanese_AverageMean), 
                                                     ['Average Cost for two', 'Restaurant Name', 'Cuisines', 'Currency']])
    
    valores_procurados.columns = ['CUSTO', 'RESTAURANTE', 'PRATOS', 'MOEDA']
    valores_procurados = valores_procurados.sort_values(by=['CUSTO'], ascending=False).reset_index(drop=True)
    CORES = ['Blackbody','Bluered','Blues','Cividis','Earth','Electric','Greens','Greys','Hot','Jet']
    fig = px.bar(valores_procurados, x='CUSTO', y='RESTAURANTE', color=CORES, barmode='group', labels='DÓLAR', orientation='h', width=550)
    
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
tab1 = st.tabs( ['RESTAURANTES'] )

st.header( 'INFORMAÇÕES - RESTAURANTES' )
st.markdown( """---""" )
    
with st.container():
        st.markdown('###### COM A MAIOR NOTA MÉDIA DE AVALIAÇÃO')
        OrderRating_Max = OrderRating_Max(df1)
        st.dataframe(OrderRating_Max, width=854, height=178, use_container_width=False) 
                
               
with st.container():
        col1, col2 = st.columns(2, gap='small') 
            
        with col1:
            st.markdown('###### COM MAIOR QUANTIDADE DE AVALIAÇÕES')  
            MaxAggregate_Rating = MaxAggregate_Rating(df1)
            st.dataframe(MaxAggregate_Rating, width=363, height=178, use_container_width=False)
            
        with col2:        
            st.markdown('###### CULINÁRIA BRASILEIRA COM MENOR MÉDIA DE AVALIAÇÃO')   
            Cuisine_BR = Cuisine_BR(df1)
            st.dataframe(Cuisine_BR, width=393, height=178, use_container_width=False)
 
with st.container():            
        st.markdown('###### COM MAIOR VALOR DE UM PRATO PARA DOIS')
        Cuisine_Orden =  Cuisine_Orden(df1)
        st.dataframe(Cuisine_Orden, width=854, height=178, use_container_width=False)
                 
               
with st.container():
        st.markdown('###### QUE MAIS POSSUEM AVALIAÇÕES E ACEITAM PEDIDOS ON-LINE')
        Rest_OnLine = Rest_OnLine(df1)
        st.dataframe(Rest_OnLine, width=854, height=178, use_container_width=False)    
            

with st.container():
        st.markdown('###### BRASILEIROS (CULINÁRIA BRASILEIRA) COM MAIOR MÉDIA DE AVALIAÇÃO')
        fig = Cuisine_BR2(df1)
        st.plotly_chart(fig) 
                            
with st.container():
        st.markdown('###### TEM MAIOR VALOR MÉDIO DE UM PRATO PARA DOIS E FAZEM RESERVA') 
        Rest_OnLine = Reserve_On(df1)
        #st.dataframe(Rest_OnLine, width=854, height=178, use_container_width=False)
        fig = Reserve_On(df1)
        st.plotly_chart(fig)
              
with st.container():
        col1, col2 = st.columns(2, gap='medium')
            
        with col1:
            st.markdown('###### AMERICANOS  DE CULINÁRIA JAPONESA')
            UsaJapanese_Average =  UsaJapanese_Average(df1)
            col1.metric('Valor médio de um prato para dois', UsaJapanese_Average, 'dolares')
            
        with col2: 
            st.markdown('###### CHURRASCARIAS AMERICANAS COM VALOR MÉDIO DE PRATO PARA DOIS MENOR QUE OS AMERICANOS DE CULINÁRIA JAPONESA')    
            #Usa_Mean_AverageNunique = Usa_Mean_AverageNunique(df1) 
            #st.dataframe(Usa_Mean_AverageNunique, width=474, height=388, use_container_width=False)
            fig = Usa_Mean_AverageNunique(df1)
            st.plotly_chart(fig)
            
            

st.markdown( """---""" )
    
    
    
