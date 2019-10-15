import requests,re
import pandas as pd
from bs4 import BeautifulSoup

#------------------------------Categoria Festas & diversão -------------
# get the data
data = requests.get('https://zebraurbana.com.br/?category=16&partner=')

# load data into bs4
soup = BeautifulSoup(data.content, 'html.parser')

itens=soup.find_all("figure",class_=re.compile("(col\-sm\-4)"))


cat_Festa_e_Diversao_TITULO=[a.find(class_=re.compile("^[Tt](i|I).le")).get_text() for a in itens]
cat_Festa_e_Diversao_PRECO_ANTIGO=[b.find(class_=re.compile("^(o|O).d")).get_text() for b in itens]
cat_Festa_e_Diversao_PRECO_PROMO=[c.find(class_=re.compile("^[nN](e|E)w")).get_text() for c in itens]




tabela_Festa_Diversao=pd.DataFrame({
    'Titulo':cat_Festa_e_Diversao_TITULO,
    'Preco antigo':cat_Festa_e_Diversao_PRECO_ANTIGO,
    'Preco na promocao':cat_Festa_e_Diversao_PRECO_PROMO,

   })

tabela_Festa_Diversao.to_csv('Festa_Diversão.csv')

#---------------------------------Outra pagina--------------------------------#


#------------------------------Categoria Beleza & Estética -------------


# get the data
data = requests.get('https://zebraurbana.com.br/?category=4&partner=')

# load data into bs4
soup = BeautifulSoup(data.content, 'html.parser')

itens=soup.find_all("figure",class_=re.compile("^c?o?l{1}\-[sS](m|m)\-4"))

''' ------------------HTML----------------
class="col-sm-4"
class="title"
class="old"
class="new"

----------------------REGEX-----------------
col-sm-4-------->^c?o?l{1}\-[sS](m|m)\-4
title----------->^[Tt](i|I).le
old------------->^(o|O).d
new------------->^[nN](e|E)w

'''
titulo=[a.find(class_=re.compile("^[Tt](i|I).le")).get_text() for a in itens]
preco_antigo=[b.find(class_=re.compile("^(o|O).d")).get_text() for b in itens]
preco_promo=[c.find(class_=re.compile("^[nN](e|E)w")).get_text() for c in itens]


tabela_Beleza_Cosmetica=pd.DataFrame({
    'Titulo':titulo,
    'Preco antigo':preco_antigo,
    'Preco na promocao':preco_promo,

   })
#print(tabela_Beleza_Cosmetica)
tabela_Beleza_Cosmetica.to_csv('beleza_Estetica.csv')
