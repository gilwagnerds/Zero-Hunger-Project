import streamlit as st
from PIL import Image                        #biblioteca usada para se importar as imagens das páginas

st.set_page_config(                          #esta função unirá as páginas buscando-as na página 'pages'
    page_title="Home", layout='wide')


#Trazendo a imagem da nossa logo para a junção da nossa página

#image_path = '/Users/usuario 1/gilwagner/repos/ftc_programacao_python/'     
image = Image.open( 'logo.jpg' )                               
st.sidebar.image( image, width=230 )

#Aqui determinamos as mesmas medidas da página lateral feita por nós nas très páginas anteriores, sem os filtros
st.sidebar.markdown( '# Zero Hunger' )
st.sidebar.markdown( '### The place where customers and restaurants meet' )
st.sidebar.markdown( """---""" )    

st.write( '# Zero Hunger Analytical Dashboard')            #Aqui estamos colocando um título na nossa apresentação inicial da página

st.markdown(                                           #Aqui trazemos as instruções para uso da página e suas funcionalidades. 
    """
    Zero Hunger é uma marketplace de restaurantes com  "CORE BUSSINES"  em facilitar o encontro e negociações de clientes 
    e restaurantes. O Analytical Dashboard foi construído para entender melhor o negócio através de  uma análise de dados 
    da empresa, com geração de dashboards, possibilitando a tomada de melhores decisões estratégicas parais a Zero Hunger.
    
    ### Como utilizar esse Analytical Dashboard?
    - Visão Geral:
        - Apresenta as informações gerais relativas aos restaurantes, países, cidades, avaliações e pratos.
    - Visão Países:
        - Países com maior número de restaurantes, pratos, médias de avalição, notas e valores;
        - Preços médios de pratos por pais / com mais cidades registradas, entre outras informações
    - Visão Cidades:
        - Cidades com restaurantes com média entre 4 e 2,5;
        - Que mais fazem reservas / entregam e aceitam pedidos On-line / Que possuem mais restaurantes, entre outras informações.
    - Visão Restaurantes:
        - Restaurantes com maior e menor médias de avaliação / Maior valor de um prato para dois;
        - Que mais aceitam entregas e possuem melhores avaliações, entre outas informações.
    - Visão Culinária:
        - Informações gerais sobre as culinárias Italiana, Americana, Árabe, Japonesa e Caseira;
        - Restaurantes com maior e menor avaliações por culinária / Maiores e menores valores por prato, entre outras informações. 
        
    ### Ask for Help
    - Time de Data Science no Discord
        -@gillgner
    """ )