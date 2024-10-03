# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 14:58:18 2024

@author: Formation
"""


#-----------Projet Démineur----------VanessaM-------------------------

import random

class Grille:
    # Niveaux prédéfinis
    NIVEAUX = {
        'débutant': {'lignes': 9, 'colonnes': 9, 'bombes': 10},
        'intermédiaire': {'lignes': 16, 'colonnes': 16, 'bombes': 40},
        'difficile': {'lignes': 16, 'colonnes': 30, 'bombes': 99}
    }

    def __init__(self, niveau='débutant', lignes=None, colonnes=None, nombre_de_bombes=None):
        
        """
        Initialise la grille selon le niveau choisi ou des paramètres personnalisés.
        """
       
        print(f"Initialisation du niveau : {niveau}")
        
        
        config = self.NIVEAUX[niveau]
        self.lignes = config['lignes']
        self.colonnes = config['colonnes']
        self.nombre_de_bombes = config['bombes']
        
        print(f"Grille de {self.lignes} lignes et {self.colonnes} colonnes avec {self.nombre_de_bombes} bombes.")
        
        
        # Création de la grille
        self.grille = [[0 for _ in range(self.colonnes)] for _ in range(self.lignes)]
        
        print("Grille vide initialisée :")
        
     
    def afficher_grille(self):
        
        """
        Affiche la grille dans la console.
        """
        
        for ligne in self.grille:
            print(" ".join(str(cell) for cell in ligne))
        print("\n")  # Saut de ligne pour mieux voir la grille
        

    def placer_bombe_aleatoirement(self):
        
        """Permet de placer aléatoirement des bombes"""
        
        
        # Générer toutes les positions possibles dans la grille
        positions_possibles = [(i, j) for i in range(self.lignes) for j in range(self.colonnes)]

        # Sélectionner aléatoirement un nombre donné de positions
        positions_choisies = random.sample(positions_possibles, self.nombre_de_bombes)
        
        print(positions_choisies)
        
        for k in positions_choisies :
            
                self.grille[k[0]][k[1]]=-1
        
        
    

        
        
if __name__ == "__main__":
    
    
    # Demande au joueur de choisir un niveau
    niveau_choisi = input("Choisissez un niveau (débutant, intermédiaire, difficile) : ").lower()

    # Vérification du niveau choisi
    if niveau_choisi not in ['débutant', 'intermédiaire', 'difficile']:
        print("Niveau invalide. Par défaut, le niveau débutant sera utilisé.")
        niveau_choisi = 'débutant'

    # Initialisation de la grille en fonction du choix du joueur
    
    print(f"Vous avez choisi le niveau {niveau_choisi}.")
    grille = Grille(niveau_choisi)
    
    grille.afficher_grille()
    
    #Grille contenant les valeurs aléatoires des bombes
    
    grille.placer_bombe_aleatoirement()
    grille.afficher_grille()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
