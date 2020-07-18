#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[ ]:





# In[ ]:





# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[ ]:


def q1():
    return black_friday.shape
    


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[ ]:


def q2():
    #Primeiro corte com mulheres na faixa de idade desejada
    mulheres = black_friday.query('Gender=="F" and Age=="26-35"')
    #Fazendo o count da coluna Gender
    contagem = mulheres['Gender'].count()
    return int(contagem)
    


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[ ]:


def q3():
    return black_friday["User_ID"].nunique()
    


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[ ]:


def q4():
    #retornando os tipos únicos de variáveis no dataset
    return int(black_friday.dtypes.nunique())
    


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[ ]:


def q5():
    #Pega o número de linhas do dataset com pelo menos um valor nan / pelo total de linhas
    return float(black_friday.isna().any(axis=1).sum() / len(black_friday))
    


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[ ]:


def q6():
    # usando o comando 'black_friday.isna().sum()' podemos descobrir a coluna com mais valores nan
    return int(black_friday['Product_Category_3'].isna().sum())
    


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[ ]:


def q7():
    #Para descobrir o valor que mais se repete usamos a função .mode(). .item() serve pra retornar somente o valor,
    #sem o index
    return black_friday['Product_Category_3'].mode().item()
    


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[ ]:


def q8():
    #Fazemos a normalização por min e max e depois tiramos a media da series que será retornada
    purchase_normalizada=(black_friday['Purchase']-black_friday['Purchase'].min())/(black_friday['Purchase'].max()-black_friday['Purchase'].min())
    return purchase_normalizada.mean()
    


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[45]:


def q9():
    # formula normalização -> variavel - sua média /  desvio padrão
    normalizado = (black_friday['Purchase'] - black_friday['Purchase'].mean()) / black_friday['Purchase'].std()
    #Aplicando uma função para selecionar o intervalo entre -1 e 1
    return int(sum(list(map(lambda x: 1 if x >= -1 and x <= 1 else 0,normalizado))))
    


# # Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[ ]:


def q10():
    #Fazemos o primeiro corte no dataset, pegando somente as colunas que precisamos
    categorias = black_friday[['Product_Category_2', 'Product_Category_3']]
    #Agora realizamos uma segundo corte para pegar somente as linhas em que a categoria_2 tem valores na 
    categoria_2_na = categorias[categorias['Product_Category_2'].isna()]
    #Comparamos se nas linhas onde a categoria_2 tem valores na, isso acontece tambem na categoria_3
    return categoria_2_na['Product_Category_2'].equals(categoria_2_na['Product_Category_3'])           
    

