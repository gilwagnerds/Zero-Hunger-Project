# ZERO HUNGER
## 1. PROBLEMA DE NEGÓCIO

A Zero Hunger é uma marketplace de restaurantes com core business em facilitar o encontro e também as negociações entre clientes e restaurantes. Dentre os quinze países participantes, seus restaurantes fazem o cadastro dentro da plataforma da Zero Hunger, que disponibiliza informações como nome do restaurante, sua localização, tipo de culinária, se oferece reservas, entregas on-line. Apresenta também faixa de preços, custo médio cobrado, a classificação recebida e as notas agregadas atribuídas aos restaurantes em seus serviços e produtos, entre outras informações. Contratado pela empresa como novo Cientista de Dados e tendo como base a estrutura de dados fornecida pela mesma, elencamos entender melhor o negócio para conseguir responder às perguntas do novo CEO da empresa, o senhor Kleiton Guerra. 

Este deseja identificar os pontos chave da empresa e elaborou uma série de perguntas, a nós oferecidas em busca de respostas. Isso inclui a identificação de padrões e tendências, a criação de modelos e algoritmos de aprendizado de máquina para prever comportamentos ou resultados futuros, e a criação de dashboards para apresentar os insights de maneira clara e concisa, para que, tanto o novo CEO da Zero Hunger, quanto toda a empresa ´possam tomar as melhores decisões estratégicas e alavancar ainda mais a Zero Hunger. A Zero Hunger possui um modelo de negócio chamado Marketplace, que fazer o intermédio do negócio entre clientes e restaurantes em várias cidades de diversos países e para o melhor entendimento de todo o negócio e tomar as melhores decisões, o CEO Kleiton Guerra gostaria de ver as seguintes métricas: 

#### GERAL

1. Quantos restaurantes únicos estão registrados?
2. Quantos países únicos estão registrados?
3. Quantas cidades únicas estão registradas?
4. Qual o total de avaliações feitas?
5. Qual o total de tipos de culinária registrados?

#### PAÍSES

1. Qual o país que possui mais cidades registradas?
2. Qual o país que possui mais restaurantes registrados?
3. Qual o país que possui mais restaurantes com o nível de preço igual a “4” registrados?
4. Qual o país que possui a maior quantidade de tipos de culinária distintos?
5. Qual o país que possui a maior quantidade de avaliações feitas?
6. Qual o país que possui a maior quantidade de restaurantes que fazem entrega?
7. Qual o país que possui a maior quantidade de restaurantes que aceitam reservas?
8. Qual o país que possui, na média, a maior quantidade de avaliações registrada?
9. Qual o nome do país que possui, na média, a maior nota média registrada?
10. Qual o nome do país que possui, na média, a menor nota média registrada?
11. Qual a média de preço de um prato para dois por país?

#### CIDADES

1. Qual a cidade que possui mais restaurantes registrados?
2. Qual a cidade que possui mais restaurantes com nota média acima de 4?
3. Qual a cidade que possui mais restaurantes com nota média abaixo de 2.5?
4. Qual o nome da cidade que possui o maior valor médio de um prato para dois?
5. Qual a cidade que possui a maior quantidade de tipos de culinária distintas?
6. Qual a cidade que possui a maior quantidade de restaurantes que fazem reservas?
7. Qual da cidade que possui a maior quantidade de restaurantes que fazem entregas?
8. Qual a cidade que possui a maior quantidade de restaurantes que aceitam pedidos online?

#### RESTAURANTES

1. O que possui a maior quantidade de avaliações.
2. O que possui a maior nota média.
3. O que possui o maior valor de um prato para duas pessoas.
4. O de culinária brasileira que possui a menor média de avaliação.
5. O de culinária brasileira (do Brasil), com a maior média de avaliação.
6. Os que aceitam pedido online e são na média, os que mais possuem avaliações. 
7. Os que fazem reservas e na média, possuem o maior valor médio de um prato para duas pessoas.
8. Os de culinária japonesa (dos Estados Unidos), que possuem um valor médio de prato para duas pessoas maior que as churrascarias americanas (BBQ)?

#### TIPOS DE CULINÁRIA

1. Restaurantes de culinária italiana, com maior e menor média de avaliação?
2. Restaurantes de culinária Americana, com maior e menor média de avaliação?
4. Restaurantes de culinária Árabe, com maior e menor média de avaliação?
7. Restaurantes de culinária Japonesa, com maior e menor média de avaliação?
8. Restaurantes de culinária Caseira, com maior e menor média de avaliação?
11. Qual o tipo de culinária que possui o maior valor médio de um prato para duas pessoas?
12. Qual o tipo de culinária que possui a maior nota média?
13. Qual o tipo de culinária que possui mais restaurantes que aceitam pedidos online e fazem entregas?

O objetivo desse projeto é criar um conjunto de gráficos e/ou tabelas que exibam essas métricas da melhor forma possível para o CEO.

## 2. PREMISSAS ASSUMIDAS PARA A ANÁLISE

1). A análise foi realizada com dados de 15 países, 125 cidades, 6942 restaurantes e o conjunto de dados que representam o contexto está disponível na plataforma do Kaggle. O link para acesso aos dados: https://www.kaggle.com/datasets/akashram/zomato-restaurants-autoupdated-dataset?resource=download&select=zomato.csv.

2). Marketplace foi o modelo de negócio assumido.

3). Totas as visões trazidas pela base dedados e destacadas pelas necessidades compartilhadas pelo CEO através das respectivas perguntas foram abordadas, ou seja: Visão Geral, Visão Países, Visão Cidades, Visão Restaurantes e Visão Culinárias. 

## 3. ESTRATÉGIA DA SOLUÇÃO.

O painel estratégico foi desenvolvido utilizando as métricas que refletem as cinco principais visões do modelo de negócio da empresa:
1. Visão Geral. 
2. Visão País
3. Visão Cidades. 
4. Visão Restaurantes
5. Visão Tipos de Culinária. 

Cada visão é representada pelo seguinte conjunto de métricas.

#### 1. INFORMAÇÕES GERAIS.

1. Restaurantes registrados.
2. Países registrados.
3. Cidades registradas.
4. Quantidade de avaliações registradas.
5. Pratos registrados.
6. Localização central – (Restaurantes por classificação).

#### 2. INFORMAÇÕES PAÍSES.

1. Com mais cidades registradas;
2. Com maior número de restaurantes;
3. Com mais restaurantes nível 4;
4. Com mais números de pratos;
5. Com maior número de avaliações;
6. Com mais restaurantes que entregam;
7. Com o número dos restaurantes que mais fazem reservas;
8. Com as maiores notas médias;
9. Com as menores notas médias; 
10. Com o preço médio de um prato para dois por país.

#### 3. INFORMAÇÕES CIDADES.

1. Com maior valor médio de um prato para dois;
2. Com mais restaurantes nota acima de 4;
3. Com mais restaurantes nota abaixo de 2,5;
4. Com maior número de restaurantes registrados;
5. Com mais restaurantes que fazer reservas;
6. Que possuem restaurantes com maior número de pratos distintos;
7. Que possuem mais restaurantes que fazem entregas;
8. Que possuem mais restaurantes que aceitam pedidos on-line.

#### 4.	INFORMAÇÕES RESTAURANTES.

1. Com a maior nota de avaliação; 
2. Com a maior quantidade de avaliações; 
3. De culinária brasileira com as menores notas de avaliação; 
4. Que mais possuem avaliações e aceitam pedidos on-line; 
5. Brasileiros (Culinária Brasileira), com maior média de avaliação; 
6. Os que possuem maior valor médio de um prato para dois e fazem entregas; 
7. Americanos (de culinária Japonesa) com valor médio de um prato para dois; 
8. Churrascarias americanas com valor médio de prato para dois menor que os restaurantes americanos de culinária japonesa. 

#### 5. INFORMAÇÕES TIPOS DE CULINÁRIA.

1. Culinária Italiana - Restaurantes com maior e menor média de avaliação.
2. Culinária Americana - Restaurantes com maior e menor média de avaliação.
3. Culinária Árabe - Restaurantes com maior e menor média de avaliação.
4. Culinária Japonesa - Restaurantes com maior e menor média de avaliação.
5. Culinária Caseira - Restaurantes com maior e menor média de avaliação.
6. Outras informações;
  
  i)	Os dez maiores valores médios de um prato para dois
  
  ii)	As dez maiores notas médias (por tipo de prato)
  
  iii)	Os dez tipos de pratos que possuem mais restaurantes que aceitam pedidos on-line e fazem entregas. 

## 4. TOP FOUR INSIGHTS DE DADOS

1. Em um ranking dos dez primeiros restaurantes que aceitam pedidos online e fazem entregas, encontraremos os mesmos distribuídos entre três países apenas (Filippines, Índia, United Aráb. Emirates) e todos eles (sem exceção), oferecem a culinária Americana como opção aos seus clientes. 
   
2. A média de valores cobrado por cada restaurante em seus pratos deverá ser realizada e analisada, não de uma forma global, como solicitado pelo CEO através de suas perguntas. Mas sim de uma forma regional (por cada país), pois a avaliação feita utilizando moedas distintas não retratam com clareza as características únicas para esse tipo de análise. Os valores obtidos, ao serem comparados, se tornam ineficazes e insignificantes em suas ações quanto à tomada de decisões estratégicas, pois com dados globais perde-se a referência da comparação por se ter como base da análise moedas distintas. A análise global (por países) deverá então partir da adoção de uma moeda única. Caso contrário, a análise deverá seguir o escopo regional, com moedas únicas a cada país.

3. Observou-se que dentre os 6.942 restaurantes cadastrados, 417 destes possuem nível de preço igual a ‘4’ e estão localizados nos Estados Unidos, o que representa 6% do total. 

4.  Em contrapartida a Índia é o país que possui o maior número de avaliações (3.507) quanto aos serviços e produtos de seus restaurantes e também possui a maior quantidade de restaurantes cadastrados que aceitas reservas (256) e outros (2.177) que realizam entregas. 

## 5. O PRODUTO FINAL DO PROJETO

Painel online, hospedado em um Cloud e disponível para acesso em qualquer dispositivo conectado à internet. O painel pode ser acessado através desse link: https://gilwagnerds-zero-hunger-home-gb8wb6.streamlit.app 

## 6. CONCLUSÃO

O objetivo desse projeto é criar um conjunto de gráficos e/ou tabelas que exibam essas métricas da melhor forma possível para o CEO. Após a conclusão e apresentação das informações obtidas pela análise realizada, observamos a necessidade das seguintes mudanças junto ao escopo total:

a)	A inclusão de uma análise regional por pais, observando melhor suas características e ressaltando suas mais significativas particularidades. 

b)	Um redimensionamento junto às métricas, ajustando o escopo sugerido com a abrangência da utilização de novos dados, tais como: “Price Tye”, “Votes”, “Rating text”, “Price Range”, “Locality”, que não foram objeto das perguntas do CEO. 

c)	Junto a estes novos dados sugerimos um melhor refinamento quanto a identificação de padrões e tendências, aumentando o universo proposto para as medidas estratégicas e modelos de toma de decisão mais eficazes e eficientes. 

## 7. PROXIMOS PASSOS

1. Reduzir o número de métricas.
2. Criar novos filtros.
3. Incluir dados existentes e não utilizados à uma nova análise.
3. Adicionar novas visões de negócio.


