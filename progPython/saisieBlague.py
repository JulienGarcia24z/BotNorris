#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 18:23:15 2020

@author: user
"""
#--- Import des librairies
from googletrans import Translator
from PIL import ImageTk, Image
from tkinter import *
import psycopg2
import conf

#---Tkinter
fenetre = Tk()
fenetre.title("Test requete sql")
fenetre.geometry("500x140")
trad = Translator()

#===FUNCTION DE SAISIE 

def queryData():

    fenetre.maxsize(500,140)
    fenetre.minsize(500,140)
#---Connexion
    connection = psycopg2.connect(user=conf.user,
                              password=conf.mdp,
                              host="localhost",
                              port="5433",
                              database=conf.bdd_name)
#---Récupére l'information du formulaire
    value = Entry(fenetre,text="Entrez un bout de mot")
    value.grid(row=6,column = 0)
    
    mot = value.get()
#---Récupére les données
    sql = connection.cursor()
    sql.execute(f"""SELECT joke
                    FROM "chuckJoke"
                    WHERE joke 
                    LIKE '%{mot}%' and LENGTH(joke) < 74
                    LIMIT 3;""")
    datas = sql.fetchall()
#---Ferme la connexion
    connection.close()
                
#---Boucle qui imprime les élèments etape par etape
    liste_blague = " "
    for element in datas:
        liste_blague += str(element[0]) + '\n'
    
    #---Label Text
    joke_label = Label(fenetre,text = liste_blague, justify = 'center')
    joke_label.grid(row=0,column=0,sticky="nsew")


#---Button
    get_btn = Button(fenetre, text='Valider', command = queryData)
    get_btn.grid(row=7, column=0, padx = 0, ipadx = 0,)
    
    
    fenetre.mainloop()
queryData()