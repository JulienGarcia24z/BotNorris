#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Created on 2020 @author: Jgarcia """

#------------------------------SCRAPING
#@===============================================================   
# 1) Zone de librairie.

from bs4 import BeautifulSoup as btf
import requests
import psycopg2
import conf
import time




# 2)@===============================================================>  
connection = psycopg2.connect(user=conf.user,
                              password=conf.mdp,
                              host="localhost",
                              port="5433",
                              database=conf.bdd_name)
sql = connection.cursor()
#--Date-->

date = time.strftime("%A %d %B %Y à %Hh%M")

# 3) Function connexion & récupération des informations des pages html.
def get_page(page):

    url = f"https://chucknorrisfacts.net/facts.php?page={page}";
    user_agent = {"User-Agent": "Julien"}
    
    requete = requests.get(url, headers = user_agent)
    html_Soup = btf(requete.content, "lxml")
    
    #--Select mon block sujet--> 
    contenu = html_Soup.select('#content > div:nth-of-type(n+2)')
    
    #--Boucle qui affiche les élèments une par une
    for element in contenu:
        #----- Liste des variables-->
        joke = element.select_one('p') #-----Blagues-->
        identifiant = element.select_one("ul")
        #--->
        rate = element.select_one("span.out5Class") #----- Notes-->
        vote = element.select_one("span.votesClass") #----- Nb_vote-->
       
        #-----CONDITION (Si il n'y a pas de valeur None affiche ces valeurs)-->

        if joke is not None:
            int_id = identifiant['id'][6:]
            new_vote = vote.text[:-6]

            #------Insert données dans les deux tables------------->
            sql.execute("""INSERT INTO public."chuckJoke" VALUES (%s, %s)""",(int_id, joke.text))
            sql.execute("""INSERT INTO public."chuckDate" VALUES (%s, %s, %s, %s)""",(int_id, date, rate.text, new_vote))
            
            connection.commit()
      
#@===============================================================           
# 4) ---Exécute la function selon le nombre de page souhaitée

url ="https://chucknorrisfacts.net/facts";
user_agent = {"User-Agent": "Julien"}
requete = requests.get(url, headers = user_agent)
html_Soup = btf(requete.content, "lxml")

block = html_Soup.select('div:nth-of-type(23) > a')
numberPage = len(block) 
#----------------------------
print(numberPage)
print("---")
compte = 0

for page in range(0,numberPage):
    #get_page(page)
    
    compte = compte +1
    print(compte)
connection.close()
print("Ready !")


