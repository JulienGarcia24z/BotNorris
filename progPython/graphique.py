#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""@author: Garcia Julien"""
#---------------------------------------------------AFFICHAGE---GRAPHIQUE----> 
import saisieBlague
from tkinter import *
from PIL import ImageTk,Image
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import psycopg2
import conf


connection = psycopg2.connect(user=conf.user,
                              password=conf.mdp,
                              host="localhost",
                              port="5433",
                              database=conf.bdd_name)

def liste_function():
    sql = connection.cursor()
# Valeur entre 1 et 2
    def valeurEntreUnEtDeux():
        #@---------------------
        sql.execute("""SELECT rates, votes, joke FROM "chuckDate"as D
                    INNER JOIN "chuckJoke" as J
                    ON J.id = D.id 
                    WHERE rates BETWEEN 
                    1 and 2;""")
                    
        get_data = sql.fetchall()
        return get_data
        #@----------------------
    #----Execute    
    datas = valeurEntreUnEtDeux()
    df = pd.DataFrame(datas,dtype=float)
    
    #-----Selectionne une blague au hasar
    
    unEtDeux = df[0].count()
    
    #@=====================================================================
    
    # Valeur entre 2 et 3
    def valeurEntreDeuxEtTrois():
        #@---------------------
        sql.execute("""SELECT rates, votes, joke FROM "chuckDate"as D
                    INNER JOIN "chuckJoke" as J
                    ON J.id = D.id 
                    WHERE rates BETWEEN 
                    2 and 3;""")
                    
        get_data = sql.fetchall()
        return get_data
        #@----------------------
    #----Execute    
    datas = valeurEntreDeuxEtTrois()
    df = pd.DataFrame(datas,dtype=float)
    
    deuxEtTrois = df[0].count()
    
    #@=====================================================================
    # Valeur entre 3 et 4
    def valeurEntreTroisEtQuatre():
        #@---------------------
        sql.execute("""SELECT rates, votes, joke FROM "chuckDate"as D
                    INNER JOIN "chuckJoke" as J
                    ON J.id = D.id 
                    WHERE rates BETWEEN 
                    3 and 4;""")
                    
        get_data = sql.fetchall()
        return get_data
        #@---------------------- 
    #----Execute    
    datas = valeurEntreTroisEtQuatre()
    df = pd.DataFrame(datas,dtype=float)
    
    troisEtQuatre = df[0].count()
    #@=====================================================================
    # Valeur entre 4 et 5
    def valeurEntreQuatreEtCinq():
        #@---------------------
        sql.execute("""SELECT rates, votes, joke FROM "chuckDate"as D
                    INNER JOIN "chuckJoke" as J
                    ON J.id = D.id 
                    WHERE rates BETWEEN 
                    4 and 5;""")
                    
        get_data = sql.fetchall()
        return get_data
        #@----------------------
    #----Execute    
    datas = valeurEntreQuatreEtCinq()
    df = pd.DataFrame(datas,dtype=float)

    quatreEtCinq = df[0].count()

    sql = connection.close()  
    
    print("Graphique")
    def graphOrizontal():
        x = np.array(['Notes 1 à 2','Notes 2 à 3','Notes 3 à 4', 'Notes 4 à 5'])
        y = np.array([unEtDeux, deuxEtTrois, troisEtQuatre, quatreEtCinq])
        
        plt.xlim(0,troisEtQuatre + 500)
        plt.barh(x, y, color="grey")
        
        plt.xlabel("Nombre de votes")

        for index, value in enumerate(y):
            plt.text(value, index, str(value,))
        plt.savefig('img/imgFig.png', dpi= 75, bbox_inches='tight')
    graphOrizontal()

#-----------Graph
    def graph():
        fenetre = Tk()
        fenetre.title("Graphique des votes")
        fenetre.geometry("500x600")
        fenetre.configure(background='white')
        
        fenetre.maxsize(500,400)
        fenetre.minsize(500,400)
        #--Label Text : Notation blagues...
        votreText = StringVar()
        labeltext = Label(fenetre,textvariable = votreText)
        labeltext.config(font=("Arial", 20), bg="white")
        votreText.set("Notation des blagues ChuckNorris")
        
        labeltext.grid(padx=100, pady=100)
        labeltext.pack()
        
        # ----CANVAS-----------
        
        # Chemin de mon image
        img = ImageTk.PhotoImage(Image.open("img/imgFig.png"))
        
        #Créer mon canvas
        canvas = Canvas(fenetre,width=460, height=320, bg ="white", highlightthickness=0 )
        # Lecture de mon image et change sa position
        # Positions
        x = 220
        y = 150
        canvas.create_image(x, y ,image=img)
        # Execution de mon canvas
        canvas.pack()
        # -----FIN CANVAS-------
        
        fenetre.mainloop()
#---Excusion graph
    graph()

#---- Champ Saisie 


liste_function()

